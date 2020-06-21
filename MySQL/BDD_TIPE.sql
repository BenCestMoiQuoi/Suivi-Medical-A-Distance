CREATE SCHEMA `tipe`;
CREATE TABLE `tipe`.`patients` (
  `idPATIENTS` INT NOT NULL AUTO_INCREMENT COMMENT 'Id du Patient',
  `Nom` VARCHAR(45) NULL DEFAULT NULL COMMENT 'Nom du patient',
  `Prenom` VARCHAR(45) NOT NULL COMMENT 'Prénom du patient',
  `Sexe` CHAR(1) NULL DEFAULT NULL COMMENT 'Sexe du patient (M : Masculin ; F : Féminin)',
  `Date_nais` DATE NULL DEFAULT NULL COMMENT 'Date de naissance du patient',
  `Autre` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Infos complémentaires (Maladies chroniques, alèrgies...)',
  `Traitement` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Traitement que prend le patients',
  `Date_creat` DATETIME NOT NULL COMMENT 'Date de création du patient',
  `Date_der_modif` DATETIME NOT NULL COMMENT 'Date de dernière modification du patient',
  `Rcd_valid` TINYINT NOT NULL DEFAULT '1' COMMENT 'Validation',
  PRIMARY KEY (`idPATIENTS`),
  UNIQUE INDEX `idPATIENTS_UNIQUE` (`idPATIENTS` ASC) VISIBLE)
COMMENT = 'Information sur les patients';
  CREATE TABLE `tipe`.`type_prise` (
  `idtype_prise` INT NOT NULL AUTO_INCREMENT COMMENT '1 = Poux \\n2 = Tension\\n3 = SpO2',
  `Nom` VARCHAR(45) NOT NULL COMMENT 'Nom du type de prise',
  `Date_creat` DATETIME NOT NULL,
  `Date_der_modif` DATETIME NOT NULL,
  `Rcd_valid` TINYINT NOT NULL DEFAULT '1',
  PRIMARY KEY (`idtype_prise`),
  UNIQUE INDEX `idtype_prise_UNIQUE` (`idtype_prise` ASC) VISIBLE)
COMMENT = 'Type de prise';
CREATE TABLE `tipe`.`valeurs` (
  `idvaleurs` INT NOT NULL AUTO_INCREMENT,
  `idPatients` INT NOT NULL,
  `idType_prise` INT NOT NULL,
  `Date_prise` DATETIME NOT NULL,
  `Valeur_prise` FLOAT NOT NULL,
  PRIMARY KEY (`idvaleurs`, `idPatients`, `idType_prise`),
  INDEX `idPatients_idx` (`idPatients` ASC) INVISIBLE,
  INDEX `idType_prise_idx` (`idType_prise` ASC) VISIBLE,
  CONSTRAINT `idPatients`
    FOREIGN KEY (`idPatients`)
    REFERENCES `tipe`.`patients` (`idPATIENTS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idType_prise`
    FOREIGN KEY (`idType_prise`)
    REFERENCES `tipe`.`type_prise` (`idTYPE_PRISE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
COMMENT = 'Les valeurs des différentes prises en fonction des idPATIENTS et des id TYPE_PRISE';

