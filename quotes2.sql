-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema quotes2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema quotes2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `quotes2` DEFAULT CHARACTER SET utf8 ;
USE `quotes2` ;

-- -----------------------------------------------------
-- Table `quotes2`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quotes2`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `alias` VARCHAR(45) NULL,
  `email` VARCHAR(75) NULL,
  `password` VARCHAR(255) NULL,
  `birthday` DATE NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quotes2`.`Quotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quotes2`.`Quotes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `author` VARCHAR(75) NULL,
  `message` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Quotes_Users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_Quotes_Users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `quotes2`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quotes2`.`Favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quotes2`.`Favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `quote_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Favorites_Users1_idx` (`user_id` ASC),
  INDEX `fk_Favorites_Quotes1_idx` (`quote_id` ASC),
  CONSTRAINT `fk_Favorites_Users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `quotes2`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Favorites_Quotes1`
    FOREIGN KEY (`quote_id`)
    REFERENCES `quotes2`.`Quotes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
