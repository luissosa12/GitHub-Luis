package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.List;

public interface TrayectoTren extends Comparable<TrayectoTren>{
	
	// Método consultores:
	public String getCodigo();
	
	public String getTrayectoTren();
	
	public TipoTren getTipo();
	
	public List<String> getEstaciones();
	
	public List<LocalTime> getHorasSalida();
	
	public List<LocalTime> getHorasLlegada();
	
//----------------------------------------------------------------------------------------------------------------------------
	// Propiedades derivadas:
	public LocalTime getHoraSalida();
	
	public LocalTime getHoraLlegada();
	
	public Duration getDuracionTrayecto();
	
//---------------------------------------------------------------------------------------------------------------------------
	// Otras operaciones:
	public LocalTime getHoraSalida(String estacion);
	
	public LocalTime getHoraLlegada(String estacion);
	
	public void anadirEstacionIntermedia(int posicion, String estacion, LocalTime horaLlegada, LocalTime horaSalida);
	
	public void eliminarEstacionIntermedia(String estacion);
	
	
	
}
