-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema art_gallery
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema art_gallery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `art_gallery` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `art_gallery` ;

-- -----------------------------------------------------
-- Table `art_gallery`.`artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art_gallery`.`artist` (
  `artist_id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(20) NOT NULL,
  `mname` VARCHAR(20) NULL DEFAULT NULL,
  `lname` VARCHAR(25) NOT NULL,
  `dob` INT NOT NULL,
  `dod` INT NULL DEFAULT NULL,
  `country` VARCHAR(25) NOT NULL,
  `local_artist` ENUM('y', 'n') NULL DEFAULT NULL,
  PRIMARY KEY (`artist_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `art_gallery`.`artwork`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art_gallery`.`artwork` (
  `artwork_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(50) NOT NULL,
  `artyear` INT NOT NULL,
  `period` VARCHAR(25) NULL DEFAULT NULL,
  `arttype` VARCHAR(20) NULL DEFAULT NULL,
  `artfile` VARCHAR(25) NOT NULL,
  `artist_id` INT NOT NULL,
  PRIMARY KEY (`artwork_id`),
  INDEX `fk_artwork_artist1_idx` (`artist_id` ASC) VISIBLE,
  CONSTRAINT `fk_artwork_artist1`
    FOREIGN KEY (`artist_id`)
    REFERENCES `art_gallery`.`artist` (`artist_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `art_gallery`.`keyword`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art_gallery`.`keyword` (
  `keyword_id` INT NOT NULL AUTO_INCREMENT,
  `keyword` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`keyword_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `art_gallery`.`artwork_has_keyword`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `art_gallery`.`artwork_has_keyword` (
  `artwork_id` INT NOT NULL,
  `keyword_id` INT NOT NULL,
  PRIMARY KEY (`artwork_id`, `keyword_id`),
  INDEX `fk_artwork_has_keyword_keyword1_idx` (`keyword_id` ASC) VISIBLE,
  INDEX `fk_artwork_has_keyword_artwork1_idx` (`artwork_id` ASC) VISIBLE,
  CONSTRAINT `fk_artwork_has_keyword_artwork1`
    FOREIGN KEY (`artwork_id`)
    REFERENCES `art_gallery`.`artwork` (`artwork_id`),
  CONSTRAINT `fk_artwork_has_keyword_keyword1`
    FOREIGN KEY (`keyword_id`)
    REFERENCES `art_gallery`.`keyword` (`keyword_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

USE art_gallery;

INSERT INTO artist (fname, mname, lname, dob, dod, country, local_artist) VALUES 
	('Vincent' , NULL , 'van Gogh', 1853, 1890, 'France', 'n'),
	('Rembrandt', 'Harmenszoon', 'van Rijn', 1606, 1669, 'Netherlands','n'),
	('Leonardo', NULL, 'da Vinci', 1452, 1519, 'Italy', 'n'),
	('Venture', 'Lonzo', 'Coy', 1965, NULL, 'United States', 'y'),
	('Deborah', NULL, 'Gill', 1970, NULL, 'United States', 'y'),
	('Claude', NULL, 'Monet', 1840, 1926, 'France', 'n'),
	('Pablo', NULL, 'Picasso', 1904, 1973, 'Spain', 'n'),
	('Michelangelo', 'di Lodovico', 'Simoni', 1475, 1564, 'Itlay', 'n');
    
SELECT * FROM artist;

INSERT INTO artwork (title, artyear, period, arttype, artfile, artist_id) VALUES
	('Irises', 1889, 'Impressionism', 'Oil', 'irises.jpg', 1),
    ('The Starry Night', 1889, 'Post-Impressionism', 'Oil', 'staryynight.jpg', 1),
    ('Sunflowers', 1888, 'Post-Impressionism', 'Oil', 'sunflowers.jpg', 1),
    ('Night Watch', 1642, 'Baroque', 'Oil', 'nightwatch.jpg', 2),
    ('Storm on the Sea of Galilee', 1633, 'Dutch Golden Age', 'Oil', 'stormgalilee.jpg', 2),
    ('Head of a Woman', 1508, 'High Renaissance', 'Oil', 'headwoman.jpg', 3),
    ('Last Supper', 1498, 'Renaissance', 'Tempre', 'lastsupper.jpg', 3),
    ('Mona Lisa', 1517, 'Renaissance', 'Oil', 'monalisa.jpg', 3),
    ('Hillside Stream', 2005, 'Modern', 'Oil', 'hillsidestream.jpg', 4),
    ('Old Barn', 1992, 'Modern', 'Oil', 'oldbarn.jpg', 4),
    ('Beach Baby', 1999, 'Modern', 'Watercolor', 'beachbaby.jpg', 5),
    ('Woman in the Garden', 1866, 'Impressionism', 'Oil', 'womengarden.jpg', 6),
    ('Old Guitarist', 1904, 'Modern', 'Oil', 'guitarist.jpg', 7);

SELECT * FROM artwork;

INSERT INTO keyword (keyword) VALUES 
    ('flowers'),
    ('blue'),
    ('landscape'),
    ('girl'),
    ('people'),
	('battle'),
    ('boat'),
    ('water'),
    ('Christ'),
    ('food'),
    ('baby');
    
SELECT * FROM keyword;

INSERT INTO artwork_has_keyword (artwork_id, keyword_id) VALUES
	(1,1),
    (2,2),
    (2,3),
    (3,1),
    (4,4),
    (4,5),
    (4,6),
    (5,7),
    (5,8),
    (5,5),
    (5,9),
    (6,4),
    (6,5),
    (7,10),
    (7,5),
    (7,9),
    (8,4),
    (8,5),
    (9,8),
    (9,3),
    (10,3),
    (11,8),
    (11,5),
    (11,11),
    (12,3),
    (12,5),
    (12,1),
    (13,2),
    (13,5);
    
SELECT * FROM artwork_has_keyword;