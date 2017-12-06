-- Model: New Model    Version: 1.0

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`student_sex`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`student_sex` (
  `student_name` VARCHAR(45) NOT NULL,
  `student_sex` VARCHAR(45) NULL,
  PRIMARY KEY (`student_name`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`student` (
  `vk_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `home_town` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`vk_id`),
    CONSTRAINT `fk_student_student_sex`
    FOREIGN KEY (`name`)
      REFERENCES `mydb`.`student_sex` (`student_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
