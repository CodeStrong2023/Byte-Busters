/*
Ejercicio04: Pedir números hasta que se teclee uno negativo y mostrar cúantos números
se han introduciodo.
ClaseScanner
 */
package ciclos04;
import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un número: ");
        numero= Integer.parseInt(entrada.nextLine());
        while(numero>= 0){
            System.out.println("El número "+numero+" es POSITIVO");
            conteo++;
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.next());
        }
        System.out.println("A Ingresado "+conteo+" números que son POSITIVOS");
    }
}
