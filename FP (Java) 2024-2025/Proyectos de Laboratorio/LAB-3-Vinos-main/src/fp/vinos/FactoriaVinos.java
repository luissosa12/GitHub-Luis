package fp.vinos;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class FactoriaVinos {
	
	public static Vinoteca leerVinoteca(String fichero) {
		Vinoteca res = null;
		try {
		List<Vino> vinos = Files.lines(Paths.get(fichero))
		.skip(1)
		.map(linea -> parsearVino(linea))
		.collect(Collectors.toList());
		res = new VinotecaStream(vinos);
		} catch (IOException e) {
		System.out.println("No se ha encontrado el fichero " +
		fichero);
		e.printStackTrace();
		}
		return res;
	}

	//Método para parsear
	public static Vino parsearVino(String cadena) {
		String[] trozos = cadena.split(",");
		
		Checkers.check("Cadena con formato no válido", trozos.length == 5);
		
		String pais = trozos[0].trim();
		String region = trozos[1].trim();
		Integer puntos = Integer.valueOf(trozos[2].trim());
		Double precio = Double.valueOf(trozos[3].trim());
		String uva = trozos[4].trim();
		
		return new Vino(pais, region, puntos, precio, uva);
	}
}
