-- ---------------------------------------------------------------------------- 
-- RA-02: Un entrenador no puede entrenar a más de 2 tenistas simultáneamente 
-- ---------------------------------------------------------------------------- 

DELIMITER //
CREATE OR REPLACE TRIGGER RA_02_1EntrenadorNoMas2Tenistas
BEFORE INSERT OR UPDATE ON players
FOR EACH ROW
BEGIN
	 DECLARE n INT;
	 SET n = (SELECT COUNT(*) FROM players pl WHERE (pl.trainer_id = NEW.trainer_id));
    IF (n>=2) THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un entrenador no puede entrenar a más de 2 tenistas';
    END IF;
END//
DELIMITER ;

-- la condición debe de ser (n>=2) ya que tenemos el "before insert or update" -> antes de insertar o actualizar la tabla de 
-- 	players, consulta la condición, es decir, si ya entrena a 2, salta el error (ya que no puede entrenar a más) 

