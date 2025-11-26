package fp.examenes;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class Examen implements Comparable<Examen>{
	
	private String asignatura;
	private Integer curso;
	private LocalDateTime fechaHora;
	private Duration duracion;
	private TipoExamen tipo;
	private Integer asistentes;
	private Boolean inscripcion;
	private List<Aula> aulas;
	
	public Examen(String asignatura, Integer curso, LocalDateTime fechaHora, Duration duracion, TipoExamen tipo,
			Integer asistentes, Boolean inscripcion, List<Aula> aulas) {
		
		Checkers.check("El número de asistentes debe ser mayor que 0", asistentes > 0);
		
		Checkers.check("La duración debe ser como mínimo de una hora", duracion.toHours() >= 1);
		
		this.asignatura = asignatura;
		this.curso = curso;
		this.fechaHora = fechaHora;
		this.duracion = duracion;
		this.tipo = tipo;
		this.asistentes = asistentes;
		this.inscripcion = inscripcion;
		this.aulas = new ArrayList<>(aulas);
	}
	
	public String getAsignatura() {
		return asignatura;
	}
	
	public Integer getCurso() {
		return curso;
	}
	
	public LocalDateTime getFechaHora() {
		return fechaHora;
	}
	
	public Duration getDuracion() {
		return duracion;
	}
	
	public void setDuracion(Duration duracion) {
		Checkers.check("La duración debe ser como mínimo de una hora", duracion.toHours() >= 1);
		
		this.duracion = duracion;
	}
	
	public TipoExamen getTipo() {
		return tipo;
	}
	
	public Integer getAsistentes() {
		return asistentes;
	}
	
	public void setAsistentes(Integer asistentes) {
		Checkers.check("El número de asistentes debe ser mayor que 0", asistentes > 0);
		
		this.asistentes = asistentes;
	}
	
	public Boolean getInscripcion() {
		return inscripcion;
	}
	
	public List<Aula> getAulas() {
		return new ArrayList<>(aulas);
	}
	
	//Propiedades derivadas:
	public List<Integer> getPuestos() {
		return aulas.stream()
                .map(Aula::capacidad)
                .collect(Collectors.toList());
	}
	
	public Integer getCapacidadMaxima() {
		return aulas.stream()
				.mapToInt(Aula::capacidad)
				.sum();
	}
	
	public Double getPorcentajeAsistentes() {
		return getAsistentes() / getCapacidadMaxima() * 100.;
	}

	@Override
	public int hashCode() {
		return Objects.hash(asignatura, curso, fechaHora);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Examen other = (Examen) obj;
		return Objects.equals(asignatura, other.asignatura) && Objects.equals(curso, other.curso)
				&& Objects.equals(fechaHora, other.fechaHora);
	}

	@Override
	public String toString() {
		return "Examen [asignatura=" + asignatura + ", curso=" + curso + ", fechaHora=" + fechaHora + ", duracion="
				+ duracion + ", tipo=" + tipo + ", asistentes=" + asistentes + ", inscripcion=" + inscripcion
				+ ", aulas=" + aulas + "]";
	}

	public int compareTo(Examen o) {
		int res = fechaHora.compareTo(o.getFechaHora());
		if (res == 0) {
			res = curso.compareTo(o.getCurso());
			if (res == 0) {
				res = asignatura.compareTo(o.getAsignatura());
			}
		}
		return res;
	}

	//Otras operaciones:
	public Boolean usaAula(String nombreAula) {
		return aulas.stream().anyMatch(a -> a.nombre().equals(nombreAula));
	}
	
	
	
	
}