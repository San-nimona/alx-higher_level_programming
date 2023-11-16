-- Mixing Order by and Where
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score DESC, name;
