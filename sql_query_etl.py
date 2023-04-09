DDL_QUERY = '''
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `fuente_ingresos_muni_mysql` DEFAULT CHARACTER SET utf8 ;
USE `fuente_ingresos_muni_mysql` ;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_REGION` (
  `region` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`region`),
  UNIQUE INDEX `region_UNIQUE` (`region` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_ENTIDAD` (
  `codigo_entidad` INT NOT NULL,
  `nombre_entidad` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_entidad`),
  UNIQUE INDEX `codigo_entidad_UNIQUE` (`codigo_entidad` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_DEPARTAMENTO` (
  `codigo_departamento` INT NOT NULL,
  `nombre_departamento` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_departamento`),
  UNIQUE INDEX `codigo_departamento_UNIQUE` (`codigo_departamento` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_CLASE` (
  `codigo_clase` INT NOT NULL,
  `nombre_clase` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_clase`),
  UNIQUE INDEX `codigo_clase_UNIQUE` (`codigo_clase` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_SECCION` (
  `codigo_seccion` INT NOT NULL,
  `nombre_seccion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_seccion`),
  UNIQUE INDEX `codigo_seccion_UNIQUE` (`codigo_seccion` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_GRUPO` (
  `codigo_grupo` INT NOT NULL,
  `nombre_grupo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_grupo`),
  UNIQUE INDEX `codigo_grupo_UNIQUE` (`codigo_grupo` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`DIM_RECURSO` (
  `codigo_recurso` INT NOT NULL,
  `nombre_recurso` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo_recurso`),
  UNIQUE INDEX `codigo_recurso_UNIQUE` (`codigo_recurso` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `fuente_ingresos_muni_mysql`.`FACT_TRANSACCION` (
  `idFACT_TRANSACCION` INT NOT NULL AUTO_INCREMENT,
  `anio` INT NOT NULL,
  `asignado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `modificado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `vigente` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `devengado` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `percibido` DECIMAL(12,8) NOT NULL DEFAULT 0,
  `region` VARCHAR(100) NOT NULL,
  `codigo_entidad` INT NOT NULL,
  `codigo_departamento` INT NOT NULL,
  `codigo_clase` INT NOT NULL,
  `codigo_seccion` INT NOT NULL,
  `codigo_grupo` INT NOT NULL,
  `codigo_recurso` INT NOT NULL,
  PRIMARY KEY (`idFACT_TRANSACCION`),
  INDEX `fk_FACT_TRANSACCION_DIM_REGION1_idx` (`region` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_ENTIDAD1_idx` (`codigo_entidad` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_DEPARTAMENTO1_idx` (`codigo_departamento` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_CLASE1_idx` (`codigo_clase` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_SECCION1_idx` (`codigo_seccion` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_GRUPO1_idx` (`codigo_grupo` ASC) VISIBLE,
  INDEX `fk_FACT_TRANSACCION_DIM_RECURSO1_idx` (`codigo_recurso` ASC) VISIBLE,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_REGION1`
    FOREIGN KEY (`region`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_REGION` (`region`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_ENTIDAD1`
    FOREIGN KEY (`codigo_entidad`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_ENTIDAD` (`codigo_entidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_DEPARTAMENTO1`
    FOREIGN KEY (`codigo_departamento`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_DEPARTAMENTO` (`codigo_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_CLASE1`
    FOREIGN KEY (`codigo_clase`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_CLASE` (`codigo_clase`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_SECCION1`
    FOREIGN KEY (`codigo_seccion`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_SECCION` (`codigo_seccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_GRUPO1`
    FOREIGN KEY (`codigo_grupo`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_GRUPO` (`codigo_grupo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_TRANSACCION_DIM_RECURSO1`
    FOREIGN KEY (`codigo_recurso`)
    REFERENCES `fuente_ingresos_muni_mysql`.`DIM_RECURSO` (`codigo_recurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

'''