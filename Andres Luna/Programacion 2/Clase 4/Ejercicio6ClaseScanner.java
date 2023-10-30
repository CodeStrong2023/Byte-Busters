/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos
 */
package Ejercicio06;

import java.util.Scanner;

public class Ejercicio6ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,suma = 0;
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero != 0);
        System.out.println("\n La suma de todo los números seleccionado es= "+suma);
    }
    
}
