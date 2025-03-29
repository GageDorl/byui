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

USE university_data;

INSERT INTO colleges(college)
VALUES ('College of Physical Science and Engineering'),
('College of Business and Communication'),
('College of Language and Letters');

SELECT * FROM colleges;

INSERT INTO departments(departments_code, departments_name, colleges_id)
VALUES ('CIT', 'Computer Information Technology', 1),
('ECON', 'Economics', 2),
('HUM', 'Humanities and Philosophy', 3);

SELECT * FROM departments;

INSERT INTO courses(courses_num, course_title, credits, department_id)
VALUES (111, 'Into to Database', 3, 1),
(388, 'Econometrics', 4, 2),
(150, 'Micro Economics', 3, 2),
(376, 'Classical Heritage', 2, 3);

SELECT * FROM courses;

SELECT college, departments_name as department, departments_code, courses_num, course_title, credits
FROM courses cr
JOIN departments d on cr.department_id = d.department_id
JOIN colleges c on d.colleges_id = c.colleges_id;

INSERT INTO terms(term_year, term_season)
VALUES (2019, 'Fall'),
(2018, 'Winter');

SELECT * FROM terms;

INSERT INTO faculty(faculty_fname, faculty_lname)
VALUES ('Marty', 'Morring'),
('Nate', 'Norris'), 
('Ben','Barrus'),
('John','Jensen'),
('Bill','Barney');

SELECT * FROM faculty;

INSERT INTO sections(section_num, section_capacity, term_id, faculty_id, course_id)
VALUES (1, 30, 1, 1, 1),
(1, 50, 1, 2, 3),
(2, 50, 1, 2, 3),
(1, 35, 1, 3, 2),
(1, 30, 1, 4, 4),
(2, 30, 2, 1, 1),
(3, 35, 2, 5, 1),
(1, 50, 2, 2, 3),
(2, 50, 2, 2, 3),
(1, 30, 2, 4, 4);

SELECT * FROM sections;

SELECT section_id, term_year, term_season, CONCAT(departments_code," ", courses_num) as course, section_num as section, faculty_fname, faculty_lname, section_capacity as capacity
FROM sections s
JOIN courses c ON s.course_id = c.course_id
JOIN faculty f ON s.faculty_id = f.faculty_id
JOIN departments d ON c.department_id = d.department_id
JOIN terms t ON s.term_id = t.term_id
ORDER BY section_id;

INSERT INTO students(first_name, last_name, gender, city, state, birthdate)
VALUES ('Paul','Miller','M','Dallas','TX', '1996-02-22'),
('Katie','Smith','F','Provo','UT', '1995-07-22'),
('Kelly','Jones','F','Provo','UT','1998-06-22'),
('Devon','Merrill','M','Mesa','AZ','2000-07-22'),
('Mandy','Murdock','F','Topeka','KS','1996-11-22'),
('Alece','Adams','F','Rigby','ID','1997-05-22'),
('Bryce', 'Carlson','M','Bozeman','TN','1997-11-22'),
('Preston','Larsen','M','Decatur','TN','1996-09-22'),
('Julia','Madsen','F','Rexburg','ID','1998-09-22'),
('Susan','Sorensen','F','Mesa','AZ','1998-08-09');

SELECT * FROM students;

INSERT INTO enrollments(section_id, students_id)
VALUES (6, 7),
(7,6),
(7,2),
(7,10),
(4,10),
(9,9),
(2,4),
(3,4),
(5,4),
(5,10),
(1,1),
(1,3),
(8,9),
(10,6);

SELECT e.section_id, e.students_id, first_name, CONCAT('enrolling in ', departments_code," ", courses_num), concat(term_season,' ',term_year), concat('Section ', section_num)
FROM enrollments e
JOIN students st ON e.students_id = st.students_id
JOIN sections s ON e.section_id = s.section_id
JOIN courses c on s.course_id = c.course_id
JOIN departments d on c.department_id = d.department_id
JOIN terms t on s.term_id = t.term_id
ORDER BY first_name;

DELETE FROM enrollments WHERE section_id = 2 and students_id = 7;


INSERT INTO enrollments (section_id, students_id)
VALUES
(8,7);
