-- script lists number of records with same score in second_table of thedatabase
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
