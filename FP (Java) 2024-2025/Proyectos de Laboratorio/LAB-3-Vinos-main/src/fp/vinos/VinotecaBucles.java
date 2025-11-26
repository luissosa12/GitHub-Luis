package fp.vinos;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.Set;
import fp.utiles.Checkers;

public class VinotecaBucles {

	
	private Set<Vino> vinos;
	
	public VinotecaBucles() {
		this.vinos= new HashSet<>();
	}
	
	public VinotecaBucles(Collection<Vino> vinos) {
		this.vinos = Set.copyOf(vinos);
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
		VinotecaBucles other = (VinotecaBucles) obj;
		return Objects.equals(vinos, other.vinos);
	}

	@Override
	public String toString() {
		return "VinotecaBucles [vinos=" + vinos + "]";
	}

	@Override
	public void AgregarVino(Vino v) {
		vinos.add(v);
	}

	@Override
	public void eliminarVino(Vino v) {
		Checkers.check("El vino no existe", vinos.remove(v));
	}

	@Override
	public Integer obtenerNumeroVinos() {
		return vinos.size();
	}

	@Override
	public Boolean contieneVino(Vino v) {
		return vinos.contains(v);
	}

	@Override
	public void agregarVinos(Collection<Vino> vinos) {
		vinos.addAll(vinos);
	}

	@Override
	public Boolean contieneVinos(Collection<Vino> vinos) {
		return vinos.containsAll(vinos);
	
	}
	
	// Tratamientos apartado a):
	public Integer calcularNumeroVinosPais(String pais) {
		// filtro + contador
		Integer res = 0;
		for(Vino v: vinos) {
			if(v.pais().equals(pais)) {
				res++;
			}
		}
		return res;
	}
	
	public HashSet<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup){
		HashSet<Vino> res = new HashSet<>();
		Checkers.check("Limites incorrectos", inf < sup);
		for (Vino v: vinos) {
			if (v.puntos() > inf && v.puntos() < sup) {
				res.add(v);
			}
		}
		return res;
	}
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		Integer res = 0;
		for (Vino v: vinos) {
			if (v.pais().equals(pais) && v.puntos() > umbral) {
				res++;
			}
		}
		return res;
	}
	public HashSet<Vino> obtenerVinosBaratos(Integer precio){
		HashSet<Vino> res = new HashSet<>();
		for (Vino v: vinos) {
			if ( v.precio() < precio) {
				res.add(v);
			}
		}
		return res;
	}
	public Boolean existeVinoDeUvaEnRegion(String region, String uva, boolean res) {
		res = false;
		for (Vino v: vinos) {
			if (v.region().equals(uva) && v.uva().equals(uva)) {
				res = true;
			}
		}
		return res;
	}
	
	// Tratamientos apartado b):
	public HashSet<String> calcularUvasDeRegion(String region){
		HashSet<String> res = new HashSet<>();
		for (Vino v: vinos) {
			if (v.region().equals(region)) {
				res.add(v.uva()); 
			}
		}
		return res;
	}
	public Integer calcularTotalPuntosVinosDeRegion(String region, int res) {
		res = 0;
		for (Vino v: vinos) {
			if (v.region().equals(region)) {
				return res + v.puntos();				}
			}
		return res;
	}
	public Double calcularMediaPuntosVinosDeUva(String uva) {
		Integer contador = 0;
		Double puntuacion = 0.0;
		for (Vino v: vinos) {
			if (v.uva().equals(uva)) {
				puntuacion += v.puntos();	
				contador ++;
				}
			}
		return puntuacion/contador;
	}
	
	// Tratamientos apartado c):
	public Vino obtenerVinoMejorPuntuado() {
	    if (vinos.isEmpty()) {
	        throw new NoSuchElementException("No hay vinos en la vinoteca.");
	    }

	    Vino mejorVino = null;

	    for (Vino v : vinos) {
	        if (mejorVino == null || v.puntos() > mejorVino.puntos()) {
	            mejorVino = v;
	        }
	    }

	    return mejorVino;
	}


	public Vino obtenerVinoMejorPuntuadoDePais (String  pais) {
	    Vino mejorVinoPais = null;

		for (Vino v:vinos) {
			if (v.pais().equals(pais)) {
				if (mejorVinoPais == null || v.puntos() > mejorVinoPais.puntos()) {
		            mejorVinoPais = v;
		        }
			}
		}
		return mejorVinoPais;
	}
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(String region, int n) {
	    // Filtrar los vinos de la regiĆ³n indicada
	    List<Vino> vinosRegion = new ArrayList<>();
	    for (Vino v : vinos) {
	        if (v.region().equals(region)) {
	            vinosRegion.add(v);
	        }
	    }

	    // Ordenar la lista de mayor a menor precio (burbuja o usando Collections.sort)
	    Collections.sort(vinosRegion, new Comparator<Vino>() {
	        @Override
	        public int compare(Vino v1, Vino v2) {
	            return Double.compare(v2.precio(), v1.precio()); // mayor a menor
	        }
	    });

	    // Obtener los primeros N vinos o todos si hay menos
	    List<Vino> resultado = new ArrayList<>();
	    for (int i = 0; i < Math.min(n, vinosRegion.size()); i++) {
	        resultado.add(vinosRegion.get(i));
	    }

	    return resultado;
	}
	
	// Tratamientos apartado d):
	public Map<String, List<Vino>> agruparVinosPorPais() {
		Map<String, List<Vino>> res = new HashMap<>();
		for(Vino v: vinos) {
			String clave = v.pais();
			if(res.containsKey(clave)) {
				res.get(clave).add(v);
			} else {
				List<Vino> lv = new ArrayList<Vino>();
				lv.add(v);
				res.put(clave, lv);
			}
		}
		return res;
	}
	
	public Map<String, List<Vino>> agruparVinosPorPais2() {
		Map<String, List<Vino>> res = new HashMap<>();
		for(Vino v: vinos) {
			String clave = v.pais();
			List<Vino> lv = res.getOrDefault(clave, newArrayList<Vino>());
			lv.add(v);
			res.put(clave, lv);
		}
		return res;
	}
	
	
	
}



