package fp.vinos;

import java.util.Collection;
import java.util.List;
import java.util.Set;

public interface Vinoteca {
	
	public void agregarVino (Vino v); //Entre paréntesis va lo que se le pasa como parámetro
	
	public void eliminarVino (Vino v); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Integer obtenerNumeroVinos(); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Boolean contieneVino(Vino v); //Entre paréntesis va lo que se le pasa como parámetro
	
	public void agregarVinos (Collection<Vino> vinos); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Boolean contieneVinos(Collection<Vino> vinos); //Entre paréntesis va lo que se le pasa como parámetroç
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 a):
	public Integer calcularNumeroVinosDePais(String pais); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Collection<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Set<Vino> obtenerVinosBaratos(Double precio); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Boolean existeVinoDeUvaEnRegion(String uva, String region); //Entre paréntesis va lo que se le pasa como parámetro
	public Boolean existeVinoDeUvaEnRegion2(String uva, String region); //Entre paréntesis va lo que se le pasa como parámetro
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 b):
	public Set<String> calcularUvasDeRegion(String region); //Entre paréntesis va lo que se le pasa como parámetro
	public Set<String> calcularUvasDeRegion2(String region); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Integer calcularTotalPuntosVinosDeRegion(String region);
	
	public Double calcularMediaPuntosVinosDeUva(String uva);
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 c):
	public Vino obtenerVinoMejorPuntuado(); //Entre paréntesis va lo que se le pasa como parámetro
	
	public Vino obtenerVinoMejorPuntuadoDePais(String pais); //Entre paréntesis va lo que se le pasa como parámetro
	
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(String region, Integer n);
//----------------------------------------------------------------------------------------------------------------------------------------------------
//EJERCICIOS EXTRA DE MARIANO:
	
	//1.-Obtener el vino más barato cuya uva esté en un conjunto dado, si no existe, se devolverá null
	
	public Vino obtenerVinoMasBaratoDeUva(Set<String> uvas);
	
	//1.1.-Obtener el país con el vino más barato cuya uva esté en un conjunto dado, si no existe, se devolverá null
	public String obtenerPaisVinoMasBaratoDeUva(Set<String> uvas);
	
	//2.-Obtener las uvas de los n vinos con más puntos cuyos precios sean menores de un precio dado, sin repetir ninguna:
	
	public List<String> getUvasVinosMasPuntuadosConPrecioMenor(Double precio, Integer n);
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 d):
	
	
//----------------------------------------------------------------------------------------------------------------------------------------------------
}


