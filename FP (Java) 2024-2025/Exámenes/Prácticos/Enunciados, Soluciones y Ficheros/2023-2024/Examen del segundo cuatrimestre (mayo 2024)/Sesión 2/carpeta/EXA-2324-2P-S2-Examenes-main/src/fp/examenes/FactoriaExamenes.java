package fp.examenes;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;

public class FactoriaExamenes {
	
	private static Examen parsearExamen(String lineaCSV) { 
		 String[] trozos = lineaCSV.split(","); 
		 Checkers.check("Formato de cadena incorrecto", trozos.length == 9); 
		   
		 String asignatura = trozos[0].trim(); 
		 Integer curso = Integer.valueOf(trozos[1].trim()); 
		 LocalDateTime fechaHora = LocalDateTime.parse(trozos[2].trim() + "-" +  
		trozos[3].trim(), DateTimeFormatter.ofPattern("d/M/y-H:m")); 
		 Duration duracion = Duration.ofMinutes(Integer.valueOf(trozos[4].trim())); 
		 TipoExamen tipo = TipoExamen.valueOf(trozos[5].trim().toUpperCase()); 
		 Integer asistentes = Integer.valueOf(trozos[6].trim()); 
		 Boolean inscripcion = parseaInscripcion(trozos[7].trim()); 
		 List<Aula> aulas = parseaAulas(trozos[8].trim()); 
		   
		 return new Examen(asignatura, curso, fechaHora, duracion, tipo, 
		  asistentes, inscripcion, aulas); 
		} 
		  
		private static Boolean parseaInscripcion(String cadena) { 
		Boolean inscripcion = false; 
		 if (cadena.toUpperCase().equals("SI")) { 
		  inscripcion = true; 
		 } 
		 return inscripcion; 
		}

		private static List<Aula> parseaAulas(String cadena) { 
			 String[] trozos = cadena.split(";"); 
			 List<Aula> aulas = new ArrayList<>(); 
			 
			 for (String trozo: trozos) { 
			  aulas.add(parseaAula(trozo)); 
			 } 
			 return aulas;   
			} 
			  
			private static Aula parseaAula(String cadena) { 
			 String[] trozos = cadena.split("-"); 
			 Checkers.check("Formato de cadena incorrecto", trozos.length == 2); 
			 String nombre = trozos[0].trim(); 
			 Integer capacidad = Integer.valueOf(trozos[1].trim()); 
			 return new Aula(nombre, capacidad); 
			}


			
			
			
}