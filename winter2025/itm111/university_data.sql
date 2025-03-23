-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema university_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema university_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `university_data` DEFAULT CHARACTER SET utf8 ;
USE `university_data` ;

-- -----------------------------------------------------
-- Table `university_data`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`students` (
  `students_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gender` ENUM('M', 'F') NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(2) NOT NULL,
  `birthdate` DATE NOT NULL,
  PRIMARY KEY (`students_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`colleges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`colleges` (
  `colleges_id` INT NOT NULL AUTO_INCREMENT,
  `college` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`colleges_id`),
  UNIQUE INDEX `college_UNIQUE` (`college` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`departments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`departments` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `departments_code` VARCHAR(45) NOT NULL,
  `departments_name` VARCHAR(45) NOT NULL,
  `colleges_id` INT NOT NULL,
  INDEX `fk_departments_colleges1_idx` (`colleges_id` ASC) VISIBLE,
  PRIMARY KEY (`department_id`),
  UNIQUE INDEX `departments_code_UNIQUE` (`departments_code` ASC) VISIBLE,
  UNIQUE INDEX `departments_name_UNIQUE` (`departments_name` ASC) VISIBLE,
  CONSTRAINT `fk_departments_colleges1`
    FOREIGN KEY (`colleges_id`)
    REFERENCES `university_data`.`colleges` (`colleges_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `courses_num` SMALLINT NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `credits` TINYINT NOT NULL,
  `department_id` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_courses_departments1_idx` (`department_id` ASC) VISIBLE,
  UNIQUE INDEX `course_title_UNIQUE` (`course_title` ASC) VISIBLE,
  CONSTRAINT `fk_courses_departments1`
    FOREIGN KEY (`department_id`)
    REFERENCES `university_data`.`departments` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`terms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`terms` (
  `term_id` INT NOT NULL AUTO_INCREMENT,
  `term_year` YEAR NOT NULL,
  `term_season` ENUM('Spring', 'Summer', 'Fall', 'Winter') NOT NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`faculty`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`faculty` (
  `faculty_id` INT NOT NULL AUTO_INCREMENT,
  `faculty_fname` VARCHAR(45) NOT NULL,
  `faculty_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`sections`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`sections` (
  `section_id` INT NOT NULL AUTO_INCREMENT,
  `section_num` TINYINT NOT NULL,
  `section_capacity` TINYINT NOT NULL,
  `term_id` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`section_id`),
  INDEX `fk_sections_terms1_idx` (`term_id` ASC) VISIBLE,
  INDEX `fk_sections_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  INDEX `fk_sections_courses1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_sections_terms1`
    FOREIGN KEY (`term_id`)
    REFERENCES `university_data`.`terms` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sections_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `university_data`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sections_courses1`
    FOREIGN KEY (`course_id`)
    REFERENCES `university_data`.`courses` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`enrollments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `university_data`.`enrollments` (
  `section_id` INT NOT NULL,
  `students_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `students_id`),
  INDEX `fk_sections_has_students_students1_idx` (`students_id` ASC) VISIBLE,
  INDEX `fk_sections_has_students_sections1_idx` (`section_id` ASC) VISIBLE,
  CONSTRAINT `fk_sections_has_students_sections1`
    FOREIGN KEY (`section_id`)
    REFERENCES `university_data`.`sections` (`section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sections_has_students_students1`
    FOREIGN KEY (`students_id`)
    REFERENCES `university_data`.`students` (`students_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
