package fp.netflix;

import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.SortedSet;
import java.util.stream.Collectors;

public class CatalogoNetflix {
	
	
	
	
	public Map<String, Set<ProduccionNetflix>> getProduccionesPorGenero() {
		Map<String, Set<ProduccionNetflix>> res = new HashMap<>();
		
		for (String g: p.getGeneros()) {
			if (res.containsKey(g)) {
				res.get(g).add(p);
			} else {
				Set<ProduccionNetflix> s = new HashSet<>();
				s.add(p);
				res.put(g, s);
			}
		}
		return res;
	}



	public SortedSet<String> getGeneros() {
		return producciones.stream().flatMap(p -> p.getGeneros().stream()).sorted().collect(Collectors.toCollection(TreeSet::new));
	}
	
	
	public List<String> getNombreTitulosConGenerosOrdenadosPorTamanyo(List<String> generos) {
		
		Comparator<ProduccionNetflix> cmp = Comparator.comparing(p -> p.getGeneros().size()).reversed().thenComparing(p -> p.getTitulo().length());
		
		return producciones.stream().filter(p -> p.getGeneros().containsAll(generos)).sorted(cmp).map(ProduccionesNetflix::getTitulo).toList();
	}
}