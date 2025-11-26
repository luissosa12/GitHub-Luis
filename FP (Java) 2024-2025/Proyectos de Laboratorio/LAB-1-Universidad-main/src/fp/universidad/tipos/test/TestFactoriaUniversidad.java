package fp.universidad.tipos.test;

import java.util.List;

import fp.universidad.tipos.Espacio;
import fp.universidad.tipos.FactoriaUniversidad;

public class TestFactoriaUniversidad {

	public static void main(String[] args) {
		
		List<Espacio> espacios = FactoriaUniversidad.leeEspacios("data/espacios.csv"); //Factoria.leeEspacios(String fichero)
		System.out.println("Leídos " + espacios.size() + " espacios");
		System.out.println("Los tres primeros son: " + espacios.subList(0, 3)); //subList() --> Muestra desde una posición hasta otra de una lista
		
		System.out.println("Los tres primeros son: ");
		muestraLista(espacios, 3); //Muestra los elementos de una lista hacia abajo (que es mucho más legible)
	}

	private static void muestraLista2(List<Espacio> lista, Integer n) {
		Integer contador = 0;
		for (Espacio e: lista) {
			System.out.println("Elemento " + contador + ": " + e);
			contador++; //Incremento el contador de 1 en 1
			if (contador > n) {
				break;
			}
		}
	}
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Mostrar CUALQUIER LISTA UNO ABAJO DE OTRO: LOS n PRIMEROS ELEMENTOS --> Se puede copiar y pegar siempre
	private static  <T> void muestraLista(List<T> lista, Integer n) {
		Integer contador = 0;
		for (T e: lista) {
			System.out.println("Elemento " + contador + ": " + e);
			contador++; //Incremento el contador de 1 en 1
			if (contador > n) {
				break;
			}
		}
	}
//----------------------------------------------------------------------------------------------------------------------------------------------------


}


