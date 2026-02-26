-- ---------------------------------------------------------------------------- 
-- Función-1: Dado un tenista y un partido, realice una función que devuelva el número de sets ganados por ese 
-- 			  		tenista en ese partido. 
-- 			Realice una prueba para comprobar el correcto funcionamiento de la función. 
-- ---------------------------------------------------------------------------- 

DELIMITER //
CREATE OR REPLACE FUNCTION numSetsGanados(jugador_id INT, partido_id INT) RETURNS INT
BEGIN
	DECLARE sets_ganados INT;

	SET sets_ganados = (SELECT COUNT(*) FROM sets s
		WHERE (s.winner_id = jugador_id AND match_id = partido_id));

    RETURN sets_ganados;
END //
DELIMITER ;


-- ---------------------------------------------------------------------------- 
-- Prueba función-1: Dado un tenista y un partido, realice una función que devuelva el número de sets ganados por ese 
-- 			  				tenista en ese partido 
--							Realice una prueba para comprobar el correcto funcionamiento de la función 
-- ---------------------------------------------------------------------------- 

SELECT numSetsGanados(2, 1);



