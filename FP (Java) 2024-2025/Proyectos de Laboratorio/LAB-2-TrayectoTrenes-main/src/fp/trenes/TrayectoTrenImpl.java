package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;
import java.util.LinkedList;
import java.util.List;

import fp.utiles.Checkers;

public class TrayectoTrenImpl implements TrayectoTren {
	
	private String codigo;
	private String trayectoTren;
	private TipoTren tipo;
	private List<String> estaciones;
	private List<LocalTime> horasSalida;
	private List<LocalTime> horasLlegada;
	
	
//---------------------------------------------------------------------------------------------------------------------------------------------------
	public TrayectoTrenImpl(String codigo, String trayectoTren, TipoTren tipo, String origen, String destino, LocalTime salida, LocalTime llegada) {
		super();
		
		Checkers.check("El código debe de tener 5 dígitos", null);
	//------------------------------------------------------------------------------------------------------------------------
		//El siguiente método de Checkers recibe un parámetro y NO lanza la excepción si NO son nulos los parámrtros entregados,
		// se pueden pasr tantos parámetros como se deseen en la misma línea
		Checkers.checkNoNull(salida, llegada);
	//------------------------------------------------------------------------------------------------------------------------
		Checkers.check("La hora de llegada debe de ser posterior sa la de salida", llegada.isAfter(salida));
		
		
		this.codigo = codigo;
		this.trayectoTren = trayectoTren;
		this.tipo = tipo;
		
		//Insertar muchos elementos: LinkedList
		//Insertar pocos elementos: ArrayList
		this.estaciones = new LinkedList<>();
		estaciones.add(origen); estaciones.add(destino);
		
		this.horasSalida = new LinkedList<>();
		horasSalida.add(salida); horasSalida.add(null);
		
		this.horasLlegada = new LinkedList<>();
		horasLlegada.add(null); horasLlegada.add(llegada);
		
	}

	
//---------------------------------------------------------------------------------------------------------------------------------------------------
	@Override
	public int compareTo(TrayectoTren o) {
		int res = getTrayectoTren().compareTo(o.getTrayectoTren());
		if (res == 0) {
			res = getHoraSalida().compareTo(o.getHoraLlegada());
			if (res == 0) {
				res = getTipo().compareTo(o.getTipo());
			}
		}
		return res;
	}

	@Override
	public String getCodigo() {
		return codigo;
	}

	@Override
	public String getTrayectoTren() {
		return trayectoTren;
	}

	@Override
	public TipoTren getTipo() {
		return tipo;
	}

	@Override
	public List<String> getEstaciones() {
		return new LinkedList<>(estaciones);
	}

	@Override
	public List<LocalTime> getHorasSalida() {
		return new LinkedList<>(horasSalida);
	}

	@Override
	public List<LocalTime> getHorasLlegada() {
		return new LinkedList<>(horasLlegada);
	}

	@Override
	public LocalTime getHoraSalida() {
		return horasSalida.get(0); //También: return horasSalida.getFirst();
	}

	@Override
	public LocalTime getHoraLlegada() {
		return horasLlegada.get(horasLlegada.size()- 1); //También: return horasLlegada.getLast();
	}

	@Override
	public Duration getDuracionTrayecto() {
		return Duration.between(getHoraSalida(), getHoraLlegada());
	}
	
//---------------------------------------------------------------------------------------------------------------------------------------------------
//Otra forma si fuese tipo "Long" en lugar de tipo "Duration":
	public Long getDuracionTrayectoMinutos() {
		return getHoraSalida().until(getHoraLlegada(), ChronoUnit.MINUTES);
	}
//Aún sabiendo esto, es preferible usar el tipo "Duration" ya que es mucho más cómodo a la larga
//---------------------------------------------------------------------------------------------------------------------------------------------------

	@Override
	public LocalTime getHoraSalida(String estacion) {
		Integer posicion = estaciones.indexOf(estacion);
		return horasSalida.get(posicion);
	}

	@Override
	public LocalTime getHoraLlegada(String estacion) {
		Integer posicion = estaciones.indexOf(estacion);
		return horasLlegada.get(posicion);
	}

	@Override
	public void anadirEstacionIntermedia(int posicion, String estacion, LocalTime horaLlegada, LocalTime horaSalida) {
		estaciones.add(posicion, estacion);
		horasLlegada.add(posicion, horaLlegada);
		horasSalida.add(posicion, horaSalida);
	}

	@Override
	public void eliminarEstacionIntermedia(String estacion) {
		//Aquí sí es importante usar el tipo: "int" y no la envoltura "Integer"
		//Los métodos siempre se usan con el tipo, ya que Java nos lo pide
		int posicion = estaciones.indexOf(estacion);
		estaciones.remove(estacion);
		horasSalida.remove(posicion);
		horasLlegada.remove(posicion);
		

	}


	
}


