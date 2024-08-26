-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema anotacoes
-- -----------------------------------------------------
-- Esquema de anotações em imagens reconhecidas por redes neurais artificiais, parte do desafio técnico da RoboticTech.
DROP SCHEMA IF EXISTS `anotacoes` ;

-- -----------------------------------------------------
-- Schema anotacoes
--
-- Esquema de anotações em imagens reconhecidas por redes neurais artificiais, parte do desafio técnico da RoboticTech.
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `anotacoes` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `anotacoes` ;

-- -----------------------------------------------------
-- Table `anotacoes`.`CLASSE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `anotacoes`.`CLASSE` ;

CREATE TABLE IF NOT EXISTS `anotacoes`.`CLASSE` (
  `COD` INT NOT NULL AUTO_INCREMENT,
  `CLASSE` VARCHAR(45) NULL,
  PRIMARY KEY (`COD`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `anotacoes`.`IMAGEM`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `anotacoes`.`IMAGEM` ;

CREATE TABLE IF NOT EXISTS `anotacoes`.`IMAGEM` (
  `COD` INT NOT NULL AUTO_INCREMENT,
  `IMAGEM` BLOB NULL,
  PRIMARY KEY (`COD`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `anotacoes`.`ANOTACAO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `anotacoes`.`ANOTACAO` ;

CREATE TABLE IF NOT EXISTS `anotacoes`.`ANOTACAO` (
  `COD` INT NOT NULL AUTO_INCREMENT,
  `COD_CLASSE` INT NOT NULL,
  `CENTRO_X` INT NULL,
  `CENTRO_Y` INT NULL,
  `LARGURA` INT NULL,
  `ALTURA` INT NULL,
  `CONFIANCA` FLOAT NULL,
  `ERRADA` TINYINT NULL DEFAULT 0,
  `COD_IMAGEM` INT NULL,
  PRIMARY KEY (`COD`),
  INDEX `ANOTACAO_FK_CLASSE_idx` (`COD_CLASSE` ASC) VISIBLE,
  INDEX `ANOTACAO_FK_IMAGEM_idx` (`COD_IMAGEM` ASC) VISIBLE,
  CONSTRAINT `ANOTACAO_FK_CLASSE`
    FOREIGN KEY (`COD_CLASSE`)
    REFERENCES `anotacoes`.`CLASSE` (`COD`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ANOTACAO_FK_IMAGEM`
    FOREIGN KEY (`COD_IMAGEM`)
    REFERENCES `anotacoes`.`IMAGEM` (`COD`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `anotacoes`.`CLASSE`
-- -----------------------------------------------------
START TRANSACTION;
USE `anotacoes`;
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (1, 'Carro');
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (2, 'Moto');
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (3, 'Bicicleta');
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (4, 'Drone');
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (5, 'Ambulância');
INSERT INTO `anotacoes`.`CLASSE` (`COD`, `CLASSE`) VALUES (6, 'Caminhão');

COMMIT;


-- -----------------------------------------------------
-- Data for table `anotacoes`.`IMAGEM`
-- -----------------------------------------------------
START TRANSACTION;
USE `anotacoes`;
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (1, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (2, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (3, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (5, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (4, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (6, NULL);
INSERT INTO `anotacoes`.`IMAGEM` (`COD`, `IMAGEM`) VALUES (7, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `anotacoes`.`ANOTACAO`
-- -----------------------------------------------------
START TRANSACTION;
USE `anotacoes`;
INSERT INTO `anotacoes`.`ANOTACAO` (`COD`, `COD_CLASSE`, `CENTRO_X`, `CENTRO_Y`, `LARGURA`, `ALTURA`, `CONFIANCA`, `ERRADA`, `COD_IMAGEM`) VALUES (1, 1, 324, 768, 40, 40, 0.8, 0, NULL);
INSERT INTO `anotacoes`.`ANOTACAO` (`COD`, `COD_CLASSE`, `CENTRO_X`, `CENTRO_Y`, `LARGURA`, `ALTURA`, `CONFIANCA`, `ERRADA`, `COD_IMAGEM`) VALUES (2, 3, 323, 753, 20, 20, 0.6, 1, NULL);
INSERT INTO `anotacoes`.`ANOTACAO` (`COD`, `COD_CLASSE`, `CENTRO_X`, `CENTRO_Y`, `LARGURA`, `ALTURA`, `CONFIANCA`, `ERRADA`, `COD_IMAGEM`) VALUES (3, 6, 561, 68, 39, 123, 05, 0, NULL);

COMMIT;

