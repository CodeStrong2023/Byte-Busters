/*
Ejercicio5: Realizar un juego para adivinar un número, para ello generar un número aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor 
o menor con respecto a N. El proceso termina cuando el usuario acierta a mostrarnos el 
número de intentos hechos. CLASE SCANNER
 */
package ciclos05;
import java.util.Scanner;

public class Ciclos05ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // ESTO GENERA UN NRO ALEATORIO
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero<aleatorio){
                System.out.println("Digite un número mayor: ");
            }
            else if(numero>aleatorio){
                System.out.println("Digite un número menor: ");
            }
            else{
                System.out.println("¡¡¡FELICIDADES, HAS ADIVINADO EL NÚMERO!!!");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivinaste el número en: "+conteo+" intentos");
    }
}
