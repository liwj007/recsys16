-- ----------------------------
-- Procedure structure for itemDegree
-- ----------------------------
DROP PROCEDURE IF EXISTS `itemDegree`;
DELIMITER ;;
CREATE DEFINER = `root`@`localhost` PROCEDURE `itemDegree`()
BEGIN
	#Routine body goes here...
	DECLARE i int;
	DECLARE week1 int;
	DECLARE week2 int;

		
	SET i=37;
    while i<=44 do
		set week1=i-2;
		set week2=i-1;
		BEGIN
			DECLARE ss int DEFAULT 0;
			DECLARE d int;
			DECLARE degree int;
			
			DECLARE cur1 CURSOR FOR 
			SELECT
				c.item_id,
				IFNULL(count(*), 0) AS itemDegree
			FROM
			(
				SELECT
					b.*
				FROM
				(
					(
						SELECT DISTINCT
							item_id
						FROM
							join_uia
						WHERE
							ui_week = i
						AND interaction_type IN (1, 2, 3)
					) a
					INNER JOIN (
						SELECT
							item_id
						FROM
							join_uia b
						WHERE
							ui_week = week1
						OR ui_week = week2
						AND interaction_type IN (1, 2, 3)
						) b
					)
			)c
			GROUP BY item_id;

			DECLARE CONTINUE HANDLER FOR NOT FOUND SET ss=1;
			open cur1;
			FETCH cur1 into d,degree;
			WHILE ss<>1 DO
				insert into item_degree(serial,itemDegree,item_id) values(i,degree,d);
				FETCH cur1 into d,degree;
			END WHILE;
			CLOSE cur1;
		END;
		SET i = i+1;
	END WHILE;
END;
;;
DELIMITER ;
call `itemDegree`()