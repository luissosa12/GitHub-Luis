package fp.universidad.tipos;

import java.time.LocalDate;
import fp.utiles.Checkers;

public record Asignatura(String nombre, TipoAsignatura tipo, int codigo, float creditos, int curso) implements Comparable<Asignatura> {
	
		//INICIAL
	
		public Asignatura {
			checkAsignatura(nombre, codigo, creditos);
		}
		
		//Constructor alternativo
		
		public Asignatura(String nombre, TipoAsignatura tipo, int codigo, float creditos) {
			this(nombre, tipo, codigo, creditos, LocalDate.now().getYear());
			checkAsignatura(nombre, codigo, creditos);
		}
		
		public Asignatura(String s) {
			this(parseNombre(s), parseTipo(s), parseCodigo(s), parseCreditos(s), parseCurso(s));
			checkAsignatura(nombre, codigo, creditos);
		}
		
		//Parsers
		
	    private static String parseNombre(String s) {
	        String[] trozos = s.split("#");
	        if (trozos.length != 5) {
	            throw new IllegalArgumentException("Cadena con formato no válido");
	        }
	        return trozos[0].trim();
	    }
	    
	    private static Integer parseCodigo(String s) {
	    	String[] trozos = s.split("#");
	    	return Integer.valueOf(trozos[1].trim());
	    }
	    
	    private static Float parseCreditos(String s) {
	    	String[] trozos = s.split("#");
	    	return Float.valueOf(trozos[2].trim());
	    }
	    
	    private static TipoAsignatura parseTipo(String s) {
	    	String[] trozos = s.split("#");
	    	return TipoAsignatura.valueOf(trozos[3].trim());
	    }
	    
	    private static Integer parseCurso(String s) {
	    	String[] trozos = s.split("#");
	    	return Integer.valueOf(trozos[4].trim());
	    }
	    
		//Checkers

		private void checkAsignatura(String nombre, int codigo, float creditos) {
			Integer c = codigo;
			Checkers.check("El nombre no puede estar vacío", !nombre.equals("") || !nombre.equals(null));
			Checkers.check("El número de creditos tiene que ser mayor que 0", creditos >= 0);
			Checkers.check("El código debe estar formado por siete dígitos", c.toString().length() == 7);
			
		}
		
		//Getters y setters
		
		public String getAcrónimo() {
			String res = "";
			char[] chararray = this.nombre.toCharArray();
			for (char c : chararray) {
				if (c >= 'A' && c <= 'Z') {
					res.concat(String.valueOf(c));
				}
			}
			return res;
		} 
		
		//Tostring
		
		public String toString() {
			return "(" + codigo + ") " + nombre;
		}
		
		//Hashcode y equals
		
		public int hashCode() {
			return Integer.valueOf(codigo).hashCode();
		}

		public boolean equals(Object o) {
	    	if (o instanceof Asignatura) {
	    		Asignatura a = (Asignatura) o;
	    		if (codigo == a.codigo) {
	    			return true;
	    		} else {
	    			return false;
	    		}
	    	} else {
	    		return false;
	    	}
		}
		
		//CompareTo
		
		public int compareTo(Asignatura o) {
			int r = Integer.valueOf(codigo).compareTo(Integer.valueOf(o.codigo));
			return r;
		}

}
