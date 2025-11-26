package fp.universidad.tipos.test;

import java.util.List;
import java.util.Set;

import fp.universidad.tipos.Centro;
import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.FactoriaUniversidad;
import fp.universidad.tipos.TipoEspacio;

public class TestCentro {

	public static void main(String[] args) {
		Centro etsii = new Centro( "E.T.S. de Ingeniería Informática", "Av. Reina Mercedes s/n", 5, 1);
		System.out.println(etsii);
		System.out.println(etsii.getEspacio());
		
		Espacio e1 = new Espacio(TipoEspacio.LABORATORIO, "F1.32", 24, 1);
		c.nuevoEspacio(e1);
		System.out.println(etsii);
		System.out.println(etsii.getEspacio());
		
		Set<Espacio> s = etsii.getEspacio();
		System.out.println("s = " + s);
		s.remove(e1);
		System.out.println("s = " + s);
		System.out.println("espacios = " + c.getEspacio());
	}
	
	
	List<Espacio> espacios = FactoriaUniversidad.leeEspacios("data/espacios.csv"); //Factoria.leeEspacios(String fichero)
	for (Espacio e: espacios) {
		etsii.nuevoEspacio(e);
	}
	
	Espacio max = etsii.getEspacioMayorCapacidad();
	System.out.println("Espacio con mayor capacidad: " + max);
}


