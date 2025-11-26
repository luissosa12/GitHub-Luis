package fp.universidad.tipos;

import fp.utiles.Checkers;

public class Espacio {
	
	
	//1. ATRIBUTOS
	private TipoEspacio tipo;
	private String nombre;
	private Integer capacidad;
	private Integer planta;
	
	
	//2. CONTRUCTORES
	public Espacio(TipoEspacio espacio, String nombre, Integer capacidad, Integer planta) {
		super();
		
		Checkers.check("La capacidad tiene que ser >= 0 ", (capacidad >= 0));
		
		this.tipo = tipo;
		this.nombre = nombre;
		this.capacidad = capacidad;
		this.planta = planta;
	}

	
//----------------------------------------------------------------------------------------------------------------------------------------------------	
	//Constructor a partir de String (cadena)
	//"A0.10,0,100,TEORIA"
	public Espacio(String cadena) {
		String[] trozos = cadena.split(",");
		Checkers.check("Cadena no válida", trozos.length == 4);
		
		String nombre = trozos[0].trim(); //Siempre se pone el trim() por si hubiera espacios indeseados
		Integer planta = Integer.valueOf(trozos[1].trim());
		Integer capacidad = Integer.valueOf(trozos[2].trim());
		TipoEspacio tipo = TipoEspacio.valueOf(trozos[3].trim());
		
		Checkers.check("La capacidad tiene que ser >= 0 ", (capacidad >= 0));
		
		this.tipo = tipo;
		this.nombre = nombre;
		this.capacidad = capacidad;
		this.planta = planta;
		
		}
//----------------------------------------------------------------------------------------------------------------------------------------------------
	
	
	//3. MÉTODOS CONSULTORES Y GETTERS
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Integer getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(Integer capacidad) {
		this.capacidad = capacidad;
	}

	public Integer getPlanta() {
		return planta;
	}

	public void setPlanta(Integer planta) {
		this.planta = planta;
	}

	
	//4.PROPIEDADES DERIVADAS
	
	
	
	
	//5. toSTRING
	@Override
	public String toString() {
		return "Espacio [nombre=" + nombre + ", capacidad=" + capacidad + ", plantas=" + planta + "]";
	}
	

}
