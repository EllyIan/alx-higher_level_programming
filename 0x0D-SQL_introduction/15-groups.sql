-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0

SELECT DISTINCT score, id FROM second_table WHERE score = score ORDER BY score DESC;
