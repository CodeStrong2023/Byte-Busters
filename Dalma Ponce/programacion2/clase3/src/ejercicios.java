import javax.swing.*;
import java.util.Scanner;

public class ejercicios {
    public static void main(String[] args) {

        //Ejercicio3:
        // Leer numeros hasta que se introduzca un cero
        // para cada uno indicar si es par o impar
        // realizar con clase scanner

        /*Scanner leer = new Scanner(System.in);

        int num;

        do {

            System.out.println("Ingrese un numero");
            num = leer.nextInt();

            if (num % 2 == 0) {

                System.out.println("El numero " + num +" es par");

                if(num == 0) {

                    System.out.println("Ingreso el numero 0, el programa finaliza");
                }

            } else {

                System.out.println("El numero " + num + " es impar");

            }

        } while(num != 0);*/

        //Ejercicio 4:
        // repetir el ejercicio anterior usando clase JOptionPane

       /* int num;

        do {

            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

            if (num % 2 == 0) {

                JOptionPane.showMessageDialog(null, "El numero " + num +" es par");

                if(num == 0) {

                    JOptionPane.showMessageDialog(null, "Ingreso el numero 0, el programa finaliza");

                }

            } else {

                JOptionPane.showMessageDialog(null,"El numero " + num + " es impar");

            }
        } while(num != 0);*/

        //Ejercicio 5:
        //Pedir numeros hasta que se ingrese un numero negativo
        // mostrar cuantos numeros se han introducido
        // hacer con clase scanner

        /*Scanner leer = new Scanner(System.in);

        int num;
        var cont = 0;

        do {

            System.out.println("Ingrese un numero");
            num = leer.nextInt();

            cont++;


        } while (num >= 0);

        System.out.println("Se ingresaron " + cont + " numeros.");*/

        //Ejercicio 6:
        //Pedir numeros hasta que se ingrese un numero negativo
        // mostrar cuantos numeros se han introducido
        // hacer con clase JOptionPane

        /*int num;
        var cont = 0;

        do {

            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

            cont++;


        } while (num >= 0);

        JOptionPane.showMessageDialog(null, "Se ingresaron " + cont + " numeros.");
*/

        //Ejercicio 7:
        // Realizar un juego para adivinar un numero
        // Generando un numero aleatorio entre 0 - 100, solicitar numeros
        // indicando si es mayor o menor hasta que se acierte mostrando el numeros de intentos realizado

        /*Scanner leer = new Scanner(System.in);

        int cont = 0, numIngresado, num = (int) (Math.random() * 100);

        do {

            System.out.println("Ingrese un numero");
            numIngresado = leer.nextInt();

            cont++;

            if (numIngresado < num) {

                System.out.println("Es menor");

            } else if (numIngresado > num) {

                System.out.println("Es mayor");

            } else if (numIngresado == num) {

                System.out.println("Usted acertó, ¡Felicidades!, sus intentos fueron " + cont);

            }

        } while (numIngresado != num);*/

        //Ejercicio 8:
        // Realizar un juego para adivinar un numero
        // Generando un numero aleatorio entre 0 - 100, solicitar numeros
        // indicando si es mayor o menor hasta que se acierte mostrando el numeros de intentos realizado
        // use clase JOptionPane

        /*int cont = 0, numIngresado, num = (int) (Math.random() * 100);

        do {

            numIngresado = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

            cont++;

            if (numIngresado < num) {

                JOptionPane.showMessageDialog(null, "Es menor");

            } else if (numIngresado > num) {

                JOptionPane.showMessageDialog(null,"Es mayor");

            } else if (numIngresado == num) {

                JOptionPane.showMessageDialog(null,"Usted acertó, ¡Felicidades!, sus intentos fueron " + cont);

            }

        } while (numIngresado != num);*/


        /* Leccion 3 - Clases y objetos
  - Los objetos son la representacion de objetos de la vida real
 Los objetos tienen estado/caracteristica (atributos como color, nombre, edad, tamaño, forma, etc) y
 comportamiento/acciones (metodos o procedimientos como comer, acelerar, encender, correr, etc)
  - Una clase es el molde/plantilla para crear los objetos; define atributos (variables) y
 métodos (funciones) comunes a los objetos de ese tipo,
 pero luego, cada objeto tendrá sus propios valores y compartirán las mismas funciones.
 Debemos crear una clase antes de poder crear objetos (instancias) de esa clase.
 Al crear un objeto de una clase, se dice que se crea una instancia de la clase
         * */



    }
}