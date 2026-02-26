-- ---------------------------------------------------------------------------- 
-- Transacción-1: Realice un procedimiento transaccional que crea dos entrenadores. Debe recibir como parámetros 
-- 						todos los datos necesarios para crear ambos entrenadores. 
--                Realice una prueba para comprobar el correcto funcionamiento:
-- 						Primer con datos correctos, segundo entrenador es un tenista en activo.
-- ---------------------------------------------------------------------------- 
DELIMITER //
CREATE OR REPLACE PROCEDURE crear_2_trainers(
	person_id1 INT,
	NAME1 VARCHAR(100),
	age1 INT,
	nationality1 VARCHAR(100),
	person_id2 INT,
	NAME2 VARCHAR(100),
	age2 INT,
	nationality2 VARCHAR(100),
    trainer_id1 INT, 
    experience1 INT, 
    specialty1 VARCHAR(50), 
    trainer_id2 INT, 
    experience2 INT, 
    specialty2 VARCHAR(50)
)

BEGIN
    START TRANSACTION;
    tblock: BEGIN
        DECLARE EXIT HANDLER FOR SQLEXCEPTION, SQLWARNING
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;
        INSERT INTO people (person_id, name, age, nationality) VALUES
        	(person_id1, NAME1, age1, nationality1),
        	(person_id2, NAME2, age2, nationality2);
		INSERT INTO trainers (trainer_id, experience, especiality) VALUES
			(trainer_id1, experience1, specialty1),
			(trainer_id2, experience2, specialty2);
        COMMIT;
    END tblock;
END //
DELIMITER ;


-- ---------------------------------------------------------------------------- 
-- Prueba transacción-1: Realice un procedimiento transaccional que crea dos entrenadores. Debe recibir como parámetros 
-- 							 	todos los datos necesarios para crear ambos entrenadores. 
--                		 Realice una prueba para comprobar el correcto funcionamiento:
-- 						    	Primero con datos correctos, segundo entrenador es un tenista en activo.
-- ---------------------------------------------------------------------------- 
CALL crear_2_trainers(
		67, 'Trainer Pruebas1', 22, 'Español', 
		68, 'Trainer Pruebas2', 25, 'Colombiano', 
		67, 44, 'Individual', 
		68, 20, 'Individual')
;

-- LO COMENTO PARA QUE NO DE ERROR 
-- CALL crear_2_trainers(
--     100, 'Entrenador Nuevo OK', 30, 'Español',      -- Datos Persona 1
--     101, 'Carlos Alcaraz', 22, 'Español',           -- Datos Persona 2 (EXISTENTE - ID 2)
--     100, 10, 'Individual',                          -- Datos Trainer 1
--     2,   5,  'Dobles');                             -- Datos Trainer 2 (ID 2 coincide con Persona 2)

