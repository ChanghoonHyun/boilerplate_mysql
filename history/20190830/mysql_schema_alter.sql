USE `boilerplate_mysql`;

ALTER TABLE `user` ADD COLUMN `is_active` tinyint(1) NOT NULL;

UPDATE user SET is_active=1;

