DDL_QUERY = '''
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `dw_ingresos_municipales` DEFAULT CHARACTER SET utf8 ;
USE `dw_ingresos_municipales` ;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_REGION` (
  `iddim_region` INT NOT NULL AUTO_INCREMENT,
  `region` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_region`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_ENTIDAD` (
  `iddim_entidad` INT NOT NULL AUTO_INCREMENT,
  `codigo_entidad` INT NOT NULL,
  `nombre_entidad` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_entidad`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_DEPARTAMENTO` (
  `iddim_departamento` INT NOT NULL AUTO_INCREMENT,
  `codigo_departamento` INT NOT NULL,
  `nombre_departamento` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_departamento`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_CLASE` (
  `iddim_clase` INT NOT NULL AUTO_INCREMENT,
  `codigo_clase` INT NOT NULL,
  `nombre_clase` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_clase`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_SECCION` (
  `iddim_seccion` INT NOT NULL AUTO_INCREMENT,
  `codigo_seccion` INT NOT NULL,
  `nombre_seccion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_seccion`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_GRUPO` (
  `iddim_grupo` INT NOT NULL AUTO_INCREMENT,
  `codigo_grupo` INT NULL,
  `nombre_grupo` VARCHAR(100) NULL,
  PRIMARY KEY (`iddim_grupo`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`DIM_RECURSO` (
  `iddim_recurso` INT NOT NULL AUTO_INCREMENT,
  `codigo_recurso` INT NOT NULL,
  `nombre_recurso` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iddim_recurso`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dw_ingresos_municipales`.`FACT_TRANSACCION` (
  `idFACT_TRANSACCION` INT NOT NULL AUTO_INCREMENT,
  `anio` INT NOT NULL,
  `asignado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `modificado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `vigente` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `devengado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `percibido` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `iddim_region` INT NOT NULL,
  `iddim_entidad` INT NOT NULL,
  `iddim_departamento` INT NOT NULL,
  `ddim_clase` INT NOT NULL,
  `iddim_seccion` INT NOT NULL,
  `iddim_grupo` INT NOT NULL,
  `iddim_recurso` INT NOT NULL,
  PRIMARY KEY (`idFACT_TRANSACCION`),
  INDEX `fk_FACT_TRANSACCION_dim_region_idx` (`iddim_region` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_entidad1_idx` (`iddim_entidad` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_departamento1_idx` (`iddim_departamento` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_clase1_idx` (`ddim_clase` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_seccion1_idx` (`iddim_seccion` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_grupo1_idx` (`iddim_grupo` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_dim_recurso1_idx` (`iddim_recurso` ASC) VISIBLE,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_region`
    FOREIGN KEY (`iddim_region`)
    REFERENCES `dw_ingresos_municipales`.`DIM_REGION` (`iddim_region`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_entidad1`
    FOREIGN KEY (`iddim_entidad`)
    REFERENCES `dw_ingresos_municipales`.`DIM_ENTIDAD` (`iddim_entidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_departamento1`
    FOREIGN KEY (`iddim_departamento`)
    REFERENCES `dw_ingresos_municipales`.`DIM_DEPARTAMENTO` (`iddim_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_clase1`
    FOREIGN KEY (`ddim_clase`)
    REFERENCES `dw_ingresos_municipales`.`DIM_CLASE` (`iddim_clase`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_seccion1`
    FOREIGN KEY (`iddim_seccion`)
    REFERENCES `dw_ingresos_municipales`.`DIM_SECCION` (`iddim_seccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_grupo1`
    FOREIGN KEY (`iddim_grupo`)
    REFERENCES `dw_ingresos_municipales`.`DIM_GRUPO` (`iddim_grupo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_dim_recurso1`
    FOREIGN KEY (`iddim_recurso`)
    REFERENCES `dw_ingresos_municipales`.`DIM_RECURSO` (`iddim_recurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

'''