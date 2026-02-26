-- ---------------------------------------------------------------------------- 
-- Consulta-1: Fecha y duración de los partidos decididos en 2 sets 
-- ---------------------------------------------------------------------------- 
-- Opción 1 (✅): 
SELECT m.match_date, m.duration 
	FROM matches m JOIN sets s ON m.match_id = s.match_id 
		GROUP BY m.match_id, m.match_date, m.duration 
		HAVING COUNT(*) = 2; 

-- Opción 2: 
SELECT m.match_date, m.duration 
	FROM matches m 
	WHERE match_id IN (SELECT match_id FROM sets 
    							GROUP BY match_id 
    							HAVING COUNT(*) = 2); 


-- ---------------------------------------------------------------------------- 
-- Consulta-2: Lista de árbitros ordenados por número de partidos arbitrados, incluyendo el número de partidos 
-- 					arbitrados por cada árbitro 
-- ---------------------------------------------------------------------------- 
SELECT pl.`name`, COUNT(m.match_id) AS matches_refereed
	FROM referees r JOIN people pl ON r.referee_id = pl.person_id JOIN matches m ON m.referee_id = r.referee_id
	GROUP BY pl.`name`
	ORDER BY matches_refereed DESC;

