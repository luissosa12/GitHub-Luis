package fp.vinos;

import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class VinotecaStream implements Vinoteca {
	
	//Constructores:
	private Set<Vino> vinos;
	
	public VinotecaStream() {
		vinos = new HashSet<>();
	}
	
	public VinotecaStream(Collection<Vino> vinos) {
		this.vinos = new HashSet<>(vinos);
	}
	
	public String toString() {
		return "La vinoteca contiene: " + vinos.size() + " vinos";
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(vinos);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		VinotecaStream other = (VinotecaStream) obj;
		return Objects.equals(vinos, other.vinos);
	}

	//-----------------------------------------------------------------------------------------------------------------------------------------------
	@Override
	public void agregarVino(Vino v) {
		// TODO Auto-generated method stub
		vinos.add(v);
	}

	@Override
	public void eliminarVino(Vino v) {
		// TODO Auto-generated method stub
		Checkers.check("El vino " + v + " no existe", vinos.contains(v)); //ó: contieneVino(v)
		vinos.remove(v);
	}

	@Override
	public Integer obtenerNumeroVinos() {
		// TODO Auto-generated method stub
		return vinos.size();
	}

	@Override
	public Boolean contieneVino(Vino v) {
		// TODO Auto-generated method stub
		return vinos.contains(v);
	}

	@Override
	public void agregarVinos(Collection<Vino> vinos) {
		// TODO Auto-generated method stub
		vinos.addAll(vinos);
	}

	@Override
	public Boolean contieneVinos(Collection<Vino> vinos) {
		// TODO Auto-generated method stub
		return vinos.containsAll(vinos);
	}
//---------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 a):
	@Override
	public Integer calcularNumeroVinosDePais(String pais) {
		// TODO Auto-generated method stub
		return (int) vinos.stream().filter(v -> v.pais().equals(pais)).count();
	}

	@Override
	public Collection<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup) {
		// TODO Auto-generated method stub
		Checkers.check("El valor inferior debe ser menor o igual que el superior", inf <= sup);
		return vinos.stream().filter(v -> v.puntos() >= inf && v.puntos() <= sup).collect(Collectors.toSet());
	}

	@Override
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		// TODO Auto-generated method stub
		return (int) vinos.stream().filter(v -> v.pais().equals(pais) && v.puntos() > umbral).count();
	}

	@Override
	public Set<Vino> obtenerVinosBaratos(Double precio) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.precio() < precio).collect(Collectors.toSet());
	}

	@Override
	public Boolean existeVinoDeUvaEnRegion(String uva, String region) {
		// TODO Auto-generated method stub
		return vinos.stream().anyMatch(v -> v.uva().equals(uva) && v.region().equals(region));
	}
		//Otra forma:
	@Override
	public Boolean existeVinoDeUvaEnRegion2(String uva, String region) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.region().equals(region)).anyMatch(v -> v.uva().equals(uva));
	}
//---------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 b):
	@Override
		// TODO Auto-generated method stub
	public Set<String> calcularUvasDeRegion(String region) {
		return vinos.stream().filter(v -> v.region().equals(region)).map(v -> v.uva()).collect(Collectors.toSet());
	}
	
		//Otra forma:
	@Override
		// TODO Auto-generated method stub
	public Set<String> calcularUvasDeRegion2(String region) {
		return vinos.stream().filter(v -> v.region().equals(region)).map(Vino::uva).collect(Collectors.toSet());
	}

	@Override
	public Integer calcularTotalPuntosVinosDeRegion(String region) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.region().equals(region)).mapToInt(Vino::puntos).sum();
	}

	@Override
	public Double calcularMediaPuntosVinosDeUva(String uva) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.uva().equals(uva)).mapToInt(v -> v.puntos()).average().orElse(0.); //orElse(0.) devuelve un 0 si está vacío
			//si queremos que mande una excepción: .getAsDouble()
	}
//----------------------------------------------------------------------------------------------------------------------------------------------------
	//Tratamientos 4 c):

	@Override
	public Vino obtenerVinoMejorPuntuado() {
		// TODO Auto-generated method stub
		return vinos.stream().max(Comparator.comparing(Vino::puntos)).get(); //el .get() si está vacío, lanza la excepción: NoSuchElementException
	}

	@Override
	public Vino obtenerVinoMejorPuntuadoDePais(String pais) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.pais().equals(pais)).max(Comparator.comparing(v -> v.puntos())).get();
	}

	@Override
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(String region, Integer n) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.region().equals(region)).sorted(Comparator.comparing(Vino::precio).reversed()).limit(n).collect(Collectors.toList());
			//.reversed() para ordenar de mayor a menor en ligar de menor a mayor;
			//.limit(n) para que ordene por los N vinos;
			//.collect(Collectors.toList() para que convierta los vinos a una lista;
	}
//----------------------------------------------------------------------------------------------------------------------------------------------------	
//EJERCICIOS EXTRA DE MARIANO:
	
	//1.-Obtener el vino más barato cuya uva esté en un conjunto dado, si no existe, se devolverá null:
	@Override
	public Vino obtenerVinoMasBaratoDeUva(Set<String> uvas) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> uvas.contains(v.uva())).min(Comparator.comparing(Vino::precio)).orElse(null);
	}
	
	//1.1.-Obtener el país con el vino más barato cuya uva esté en un conjunto dado, si no existe, se devolverá null:
	public String obtenerPaisVinoMasBaratoDeUva(Set<String> uvas) {
		// TODO Auto-generated method stub
		Optional<Vino> o = vinos.stream().filter(v -> uvas.contains(v.uva())).min(Comparator.comparing(Vino::precio));
		if (o.isPresent()) {
			return o.get().pais();
		} else {
			return null;
		}
		
	}
	
	//2.-Obtener las n uvas de los vinos con más puntos cuyos precios sean menores de un precio dado, sin repetir ninguna:
	@Override
	public List<String> getUvasVinosMasPuntuadosConPrecioMenor(Double precio, Integer n) {
		// TODO Auto-generated method stub
		return vinos.stream().filter(v -> v.precio() < precio).sorted(Comparator.comparing(Vino::puntos).reversed()).map(Vino::uva).distinct().limit(n).collect(Collectors.toList());
		//.distinct() elimina elementos repetidos
		//.limit() SIEMPRE va al final, ya que primero filtramos, etc... y luego añadimos el parámetro
	}
//----------------------------------------------------------------------------------------------------------------------------------------------------	
	//Tratamientos 4 d):
	
	public Map<String, List<Vino>> agruparVinosPorPais() {
		return vinos.stream().collect(Collectors.groupingBy(Vino::pais));
	}
	
	public Map<String, Set<String>> agruparUvasPorPais() {
		return vinos.stream().collect(Collectors.groupingBy(Vino::pais, Collectors.mapping(Vino::uva, Collectors.toSet())));
	}
	
	public Map<String, Integer> calcularCalidadPrecioPorRegionMayorDe(Double umbral) {
		return vinos.stream().filter(v -> v.calidadPrecio() > umbral).collect(Collectors.groupingBy(Vino::region, Collectors.collectingAndThen(Collectors.counting(), l -> l.intValue())));
	}
	
	
	
	
	
//----------------------------------------------------------------------------------------------------------------------------------------------------	
}




