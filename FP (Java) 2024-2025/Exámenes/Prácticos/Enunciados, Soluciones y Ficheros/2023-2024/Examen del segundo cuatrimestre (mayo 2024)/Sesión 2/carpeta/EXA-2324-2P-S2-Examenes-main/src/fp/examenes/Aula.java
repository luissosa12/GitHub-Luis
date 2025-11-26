package fp.examenes;

import fp.utiles.Checkers;

public record Aula(String nombre, Integer capacidad) {
	
	public Aula {
		
		Checkers.check("El nombre debe de empezar por una letra", Character.isLetter(nombre.charAt(0)));
		
		Checkers.check("La capacidad debe ser mayor que cero", capacidad > 0 );
	}
	
	
	
	
}