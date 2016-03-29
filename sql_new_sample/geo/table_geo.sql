-- ----------------------------
-- Table structure for geo
-- ----------------------------
DROP TABLE IF EXISTS `geo`;
CREATE TABLE `geo` (
  `id` int(11) NOT NULL,
  `i_latitude` double DEFAULT NULL,
  `i_longitude` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  KEY `i_latitude` (`i_latitude`, `i_longitude`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- procedure structure for geo_insert
-- ----------------------------
DROP PROCEDURE IF EXISTS `geo_insert`;

DELIMITER //
CREATE DEFINER = `root`@`localhost`
PROCEDURE `geo_insert`()
BEGIN
    DECLARE s int default 0;
    DECLARE lat double;
    DECLARE log double;
    DECLARE i int;

    DECLARE cur CURSOR FOR 
    SELECT 
        DISTINCT i_latitude, i_longitude 
    FROM small_sample_2;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s=1;

    OPEN cur;
    FETCH cur INTO lat,log;
    SET i = 1;
    WHILE s <> 1 DO

        IF lat <> 0 AND log <> 0 THEN
            INSERT IGNORE INTO geo (id, i_latitude, i_longitude) VALUES (i, lat, log);
        END IF;

        FETCH cur INTO lat,log;
        SET i = i + 1;
    END WHILE;

END;
//
DELIMITER ;

CALL `geo_insert`();
