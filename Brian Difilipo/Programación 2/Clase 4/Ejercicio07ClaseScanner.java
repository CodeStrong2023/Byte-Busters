/*
ejercicio 7: Pedir números hasta que se introduzca uno negativo y calcular el promedio
 */
package ejercicio7;
import java.util.Scanner;

public class Ejercicio07ClaseScanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0){ //mientras el nro no sea negativo
            suma += numero;
            conteo++;
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo == 0){
            System.out.println("\nError, la division entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;  //suma y conteo son enteras, para convertir se pone float
            System.out.println("\nEl promedio es: "+promedio);
        }
    }
}
