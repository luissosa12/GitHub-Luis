package fp.universidad.tipos;

import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

import fp.utiles.Checkers;

public class Centro implements Comparable<Centro> {
	
	//ATRIBUTOS
	private String nombre;
	private String direccion;
	private Integer plantas;
	private Integer sotanos;
	private Set<Espacio> espacios;
	
	
	//CONSTRUCTORES
	public Centro(String nombre, String direccion, Integer plantas, Integer sotanos) {
		super();
		
		//RESTRICCIONES:
		Checkers.check("El número de plantas debe ser > 0", plantas > 0);
		Checkers.check("El número de sótanos debe ser >= 0", sotanos >= 0);
		
		this.nombre = nombre;
		this.direccion = direccion;
		this.plantas = plantas;
		this.sotanos = sotanos;
		this.espacios = new HashSet<>();
	}


	//GETTERS Y SETTERS (EN ESTE CASO SETTERS NO HYA QUE SUS PROPIEDADES NO CAMBIAN)
	public String getNombre() {
		return nombre;
	}


	public String getDireccion() {
		return direccion;
	}


	public Integer getPlantas() {
		return plantas;
	}


	public Integer getSotanos() {
		return sotanos;
	}


	public Set<Espacio> getEspacio() {
		return new HashSet<>(espacios); //Creamos una "copia" para que así no elimine al ser modificado un espacio
	}


	//REPRESENTACIÓN COMO CADENA
	@Override
	public String toString() {
		return nombre;
	}

	
	//IGUALDAD
	@Override
	public int hashCode() {
		return Objects.hash(nombre);
	}

	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Centro other = (Centro) obj;
		return Objects.equals(nombre, other.nombre);
	}


	//ORDEN NATURAL: ordenar por orden de atributos
		//1. Poner en la cabecera lo de: implements Comparable<Centro> ara que sea comparable
	@Override
	public int compareTo(Centro o) {
		return nombre.compareTo(o.getNombre());
	}
	
	
	//RESTRICCIONES: se chequea (escribe) en el constructor
	
	
	//OTRAS OPERACIONES: métodos
	public void nuevoEspacio(Espacio e) { //Método que recibe un espacio y lo añade al conjunto Espacio
		
		Checkers.check("La planta debe estar entre: " + (plantas-1) + " y " + (-sotanos), e.getPlanta() < (plantas-1) &&
				e.getPlanta() > (-sotanos));
		espacios.add(e);
	}
	
	public void eliminaEspacio(Espacio e) { //Método que pregunta si el espacio está en el conjunto, si está, no hace nada,
		//si no está, lo elimina
		espacios.remove(e);
	}
	
	
//---------------------------------------------------------------------------------------------------------------------------------------------------
	//Método que devuelve un espacio
	public Espacio getEspacioMayorCapacidad() {
		return Collections.max(espacios),
				Comparator.comparing(Espacio::getCapacidad()); //Da el máximo de los espacios, comparándolos por tipo Espacio por su capacidad
	}
	
	//Otra forma:
	public Espacio getEspacioMayorCapacidad2() {
		Espacio max = null;
		for (Espacio e: espacios) {
			if (max == null || e.getCapacidad() > max.getCapacidad()) {
				max = e;
			}
		}
		return max;
	}
	
//---------------------------------------------------------------------------------------------------------------------------------------------------
}


