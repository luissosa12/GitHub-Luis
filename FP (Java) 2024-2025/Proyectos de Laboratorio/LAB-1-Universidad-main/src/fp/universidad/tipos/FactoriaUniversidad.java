package fp.universidad.tipos;

import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaUniversidad {
	
	//1. Leer el fichero y crear una lista de cadenas
	public static List<Espacio> leeEspacios(String fichero) {
		
		//1.1. Leer el fichero
		List<String> lineas = Ficheros.leeFichero("Error en el fichero", fichero); //Ficheros.leeFichero(String errMsg, String path)
		
		//1.2. Convertir una lista de cadenas (String) en un tipo (Espacio en nuestro caso)
		List<Espacio> espacios = new ArrayList<>();
		for (String linea: lineas) {
			Espacio e = creaEspacio(linea);
			espacios.add(e);
		}
		return espacios;
	}
	
	//2. Crear el espacio a partir de una cadena (1.)
	private static Espacio creaEspacio(String cadena) {
		String[] trozos = cadena.split(",");
		Checkers.check("Cadena no válida", trozos.length == 4);
		
		String nombre = trozos[0].trim(); //Siempre se pone el trim() por si hubiera espacios indeseados
		Integer planta = Integer.valueOf(trozos[1].trim());
		Integer capacidad = Integer.valueOf(trozos[2].trim());
		TipoEspacio tipo = TipoEspacio.valueOf(trozos[3].trim());
		
		return new Espacio(tipo, nombre, capacidad, planta);
	}

}
