package fp.universidad.tipos;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

import fp.utiles.Checkers;

public class Profesor extends Persona {
	
	//INICIAL
	
	private TipoCategoria categoria;
	private SortedSet<Tutoria> tutorias;
	
	private Map<Asignatura, Double> dedicacionPorAsignatura;
	private final static Double MAX_CREDITOS = 24.;
	
	//Constructores
	
	public Profesor(String dni, String nombre, String apellidos, String email, LocalDate fechaNacimiento, TipoCategoria categoria) {
		super(dni, nombre, apellidos, email, fechaNacimiento);
		checkProfesor();
		this.categoria = categoria;
		this.tutorias = new TreeSet<>();
		
		this.dedicacionPorAsignatura = new HashMap<>();
	}
	
	//Checkers
	
	private void checkProfesor() {
		Checkers.check("La edad de un profesor no puede ser menor que 18", getEdad() >= 18);
	}
	
	//Getters y setters
	
	public TipoCategoria getCategoria() {
		return categoria;
	}
	
	public void setCategoria(TipoCategoria categoria) {
		this.categoria = categoria;
	}
	
	public HashSet<Tutoria> getTutorias() {
		return tutorias;
	}
	
	//Tostring
	
	public String toString() {
		return this.getDni() + " - " + this.getApellidos() + ", " + this.getNombre() + " - " + 
				this.getFechaNacimiento().getDayOfMonth() + "/" + this.getFechaNacimiento().getMonthValue() + "/" + this.getFechaNacimiento().getYear() + 
				" (" + this.getCategoria() + ")";
	}	
	
	//Funcionalidades
	
	public void nuevaTutoria(LocalTime horaInicio, int duracion, DayOfWeek dia) {
		Tutoria t = new Tutoria(dia, horaInicio, duracion);
		tutorias.add(t);
	}
	
	public void borraTutoria(LocalTime horaInicio, DayOfWeek dia) {
		for (Tutoria i : this.tutorias) {
			if (i.horaInicio() == horaInicio && i.dia() == dia) {
				tutorias.remove(i);
			}
		}
	}
	
	public void borraTutorias() {
		tutorias.clear();
	}
	
	public List<Asignatura> getAsignaturas() {
		return new ArrayList<>(dedicacionPorAsignatura.keySet());
	}
	
	
	public List<Double> getCreditos() {
		return new ArrayList<>(dedicacionPorAsignatura.values());
	}
	
	public void imparteAsignatura(Asignatura a, Double d) {
		Checkers.check("La dedicación debe ser positiva y menor o igual que los créditos de la asignatura", d > 0 && d <= a.creditos());
		Checkers.check("La dedicación total no debe superar los " + MAX_CREDITOS + " créditos", (getDedicacionTotal() + d) <= MAX_CREDITOS);
		dedicacionPorAsignatura.put(a, d);
	}
	
	public Double getDedidacionTotal() {
		Double suma = 0.;
		for (Double d: getCreditos()) {
			suma += d;
		}
		return suma;
	}
	
	public void eliminaAsignatura(Asignatura a) {
		dedicacionPorAsignatura.remove(a);
	}
	
	public Double dedicacionAsignatura(Asignatura a) {
		Double res = 0.;
		if (dedicacionPorAsignatura.containsKey(a)) {
			res = dedicacionPorAsignatura.get(a);
		}
		return res;
		
	}
	
	
	
	
}



