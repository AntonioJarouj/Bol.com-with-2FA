
-- Table user
CREATE TABLE IF NOT EXISTS `user` (
   `id` INT NOT NULL AUTO_INCREMENT,
   `firstname` VARCHAR(255) NOT NULL,
   `prefix` VARCHAR(255) NULL DEFAULT NULL,
   `lastname` VARCHAR(255) NOT NULL,
   `email` VARCHAR(255) NOT NULL,
   `password` VARCHAR(255) NOT NULL,
   `bankrekening` VARCHAR(255) NOT NULL,
   `KvK` INT NOT NULL,
   `bedrijfsnaam` VARCHAR(255),
   PRIMARY KEY (`id`)
);

INSERT INTO user.user VALUES(NULL,'Antonyo',NULL,'Jarouj','antonyo.jarouj@hva.nl', '$2b$12$eX819XcEUZO.hEhY70ijb.OMdOxbkUUOyK9ijgYhoj5f059No7pyy', 'NL0INGB123456789', 85766585, 'Kapsalon Robert');
INSERT INTO user.user VALUES(NULL,'Nilas',NULL,'Meeder','nilas.meeder@hva.nl', '$2b$12$eX819XcEUZO.hEhY70ijb.OMdOxbkUUOyK9ijgYhoj5f059No7pyy', 'NL0INGB1234567890', 85766585, 'Kapsalon Robert');
INSERT INTO user.user VALUES(NULL,'Gilles','de','Goeij','gilles.de.goeij@hva.nl', '$2b$12$eX819XcEUZO.hEhY70ijb.OMdOxbkUUOyK9ijgYhoj5f059No7pyy', 'NL0INGB123456789', 85766585, 'Kapsalon Robert');
INSERT INTO user.user VALUES(NULL,'Ibrahim',NULL,'Selek','ibrahim.selek@hva.nl', '$2b$12$eX819XcEUZO.hEhY70ijb.OMdOxbkUUOyK9ijgYhoj5f059No7pyy', 'NL0INGB123456789', 85766585, 'Kapsalon Robert');
INSERT INTO user.user VALUES(NULL,'Vincent','van','Loon','vincent.van.loon@hva.nl', '$2b$12$eX819XcEUZO.hEhY70ijb.OMdOxbkUUOyK9ijgYhoj5f059No7pyy', 'NL0INGB123456789', 85766585, 'Kapsalon Robert');

