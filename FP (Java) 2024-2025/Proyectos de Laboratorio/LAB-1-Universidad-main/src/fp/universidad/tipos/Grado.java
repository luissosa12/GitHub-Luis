package fp.universidad.tipos;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeMap;
import java.util.SortedMap;
import java.util.HashSet;

import fp.utiles.Checkers;

public class Grado implements Comparable<Grado> {
	
	//INICIAL
	
	private String nombre;
	private Set<Asignatura> obligatorias;
	private Set<Asignatura> optativas;
	private float minCreditosOptativas;
	
	//Constructores
	
	public Grado(String nombre, Set<Asignatura> obligatorias, Set<Asignatura> optativas, float minCreditosOptativas) {
		this.nombre = nombre;
		this.obligatorias = obligatorias;
		this.optativas = optativas;
		this.minCreditosOptativas = minCreditosOptativas;
		checkGrado();
	}
	
	//Checkers
	
	private void checkGrado() {
		Checkers.check("Todas las asignaturas optativas del grado deben tener el mismo número de créditos",
				!checkCreditosOptativas(optativas));
		Checkers.check("El número mínimo de créditos de asignaturas optativas que debe cursar un alumno debe estar comprendido entre cero y el número total de créditos de asignaturas optativas del grado", 
				checkMinCreditosOptativas());
	}
	
	private boolean checkCreditosOptativas(Set<Asignatura> optativas) {
	    if (optativas.isEmpty()) return true;

	    float creditosReferencia = -1;
	    final float MARGEN_ERROR = 0.001f; 
	    for (Asignatura asignatura : optativas) {
	        if (creditosReferencia == -1) {
	            creditosReferencia = asignatura.creditos();
	        } else if (Math.abs(asignatura.creditos() - creditosReferencia) > MARGEN_ERROR) {
	            return false; 
	        }
	    }
	    return true;
	}
	
	private boolean checkMinCreditosOptativas() {
		float r = 0.0f;
		for (Asignatura i : optativas) {
			r = r + i.creditos();
		}
		if (this.minCreditosOptativas <= r && this.minCreditosOptativas >= 0.0f) {
			return true;
		} else {
			return false;
		}
	}
	
	//Getters y setters
	
	public Set<Asignatura> getAsiganturas() {
		//TODO
		return null;
	}
	
	public Asignatura getAsignatura() {
		//TODO
		return null;
	}
	
	public String getNombre() {
		return nombre;
	}

	public Set<Asignatura> getObligatorias() {
		return obligatorias;
	}

	public Set<Asignatura> getOptativas() {
		return optativas;
	}

	public float getMinCreditosOptativas() {
		return minCreditosOptativas;
	}
	
	//Tostring
	
	public String toString() {
		return nombre;
	}
	
	//Hashcode y equals
	
	public int hashCode() {
		return Objects.hash(nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!(obj instanceof Grado)) {
			return false;
		}
		Grado other = (Grado) obj;
		return Objects.equals(nombre, other.nombre);
	}
	
	//CompareTo
	
	public int compareTo(Grado g) {
		int r = nombre.compareTo(g.nombre);
		return r;
	}
	
	//Funcionalidades
	
	public float creditosObligatorias() {
		float r = 0;
		for (Asignatura i : this.obligatorias) {
			r = r + i.creditos();
		}
		return r;
	}

	public float totalCreditosTitulo() {
		return this.minCreditosOptativas + this.creditosObligatorias();
	}
	
	
	public SortedMap<Asignatura, Double> getCreditosPorAsignatura() {
		SortedMap<Asignatura, Double> m = new TreeMap<>();
		
		for (Asignatura a: obligatorias) {
			m.put(a, a.creditos());
		}
		
		for (Asignatura a: optativas) {
		m.put(a, a.creditos());
		}
		return m;
	
	}
	
	
	public Map<Integer, Double> getTotalCreditosPorCurso() {
		Map<Integer, Double> m = new HashMap<>();
		
			Set<Asignatura> asignaturas = new HashSet<>(obligatorias);
			asignaturas.addAll(optativas);

			for (Asignatura a: asignaturas) {
				Integer curso = a.curso();
				if(m.containsKey(curso));{
				m.put(curso, m.get(curso) + a.creditos());
		} else {
			m.put(curso, a.creditos);
		}
		return m;
	}
	
	
	
	
}





