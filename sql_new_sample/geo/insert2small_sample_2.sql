-- ----------------------------
-- insert data small_sample_2
-- ----------------------------
INSERT INTO small_sample_2
SELECT * FROM
(SELECT * FROM sample WHERE id >= (8530861 * RAND() + 8974187) LIMIT 212091)
AS tmp; 

INSERT INTO small_sample_2
SELECT * FROM
(SELECT * FROM sample WHERE label = 1)
AS tmp; 
