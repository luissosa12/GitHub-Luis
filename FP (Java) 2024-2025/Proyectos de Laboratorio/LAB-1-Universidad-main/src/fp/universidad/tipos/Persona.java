package fp.universidad.tipos;

import java.time.LocalDate;

public class Persona implements Comparable<Persona> {

	//1. ATRIBUTOS
	private String dni;
	private String nombre;
	private String apellidos;
	private LocalDate fechaNacimiento;
	private String email;
	private Integer edad;
	
	
	//2. CONSTRUCTORES
	public Persona(String dni, String nombre, String apellidos, LocalDate fechaNacimiento, String email, int edad) {
		super();
		this.dni = dni;
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.fechaNacimiento = fechaNacimiento;
		this.email = email;
		this.edad = edad;
	}

	//sonDigitos
	private boolean sonDigitos(String codigo) {
		boolean res = true;
		for (int i = 0; i < codigo.length(); i++) {
			if (!Character.isDigit(codigo.charAt(i))) {
				res = false;
				break;
			}
		}
		return res;
	}
	
	//3.CONSULTORES Y MODIFICADORES
	public String getDni() {
		return dni;
	}




	public void setDni(String dni) {
		this.dni = dni;
	}




	public String getNombre() {
		return nombre;
	}




	public void setNombre(String nombre) {
		this.nombre = nombre;
	}




	public String getApellidos() {
		return apellidos;
	}




	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}




	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}




	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}




	public String getEmail() {
		return email;
	}




	public void setEmail(String email) {
		this.email = email;
	}




	public int getEdad() {
		return edad;
	}




	public void setEdad(int edad) {
		this.edad = edad;
	}

	
	//4. PROPIEDADES DERIVADAS
	
	
	

	//5. toSTRING
	@Override
	public String toString() {
		return "Persona [dni=" + dni + ", nombre=" + nombre + ", apellidos=" + apellidos + ", fechaNacimiento="
				+ fechaNacimiento + ", email=" + email + ", edad=" + edad + "]";
	}
	
	
	//6. COMPARACIONES
	@Override
	public int compareTo(Persona o) {
		int res = apellidos.compareTo(o.getApellidos());
		if (res == 0) {
			res = nombre.compareTo(o.getNombre());
			if (res == 0) {
				res = dni.compareTo(o.getDni());
			}
		}
		return res;
	}
}
