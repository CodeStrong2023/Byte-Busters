public class Ejercicios {
    public static void main(String[] args) {

        //Ejercicio 1:
        // Leer un numero y mostrar su cuadrado, repetir hasta que se ingrese un numero negativo

        /*Scanner leer = new Scanner(System.in);

        var bandera = true;

        while (bandera){

            System.out.println("Ingrese un numero");
            var num = leer.nextInt();

            if(num >= 0) {

                var cuadrado = num * num;
                System.out.println("El cuadrado de " + num + " es " + cuadrado);

            } else {
                System.out.println("Solo se aceptan numeros positivos");
                bandera = false;
            }
        }*/

        //Ejercicio 2:
        // repetir el ejercicio anterior sin usar clase scanner
        // en su lugar se usará clase JOpctionPane

        /*var bandera2 = true;

        while (bandera2){

            var num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

            if(num2 >= 0) {

                var cuadrado = num2 * num2;
                System.out.println("El cuadrado de " + num2 + " es " + cuadrado);

            } else {
                System.out.println("Solo se aceptan numeros positivos");
                bandera2 = false;
            }
        }*/

        //Ejercicio3:
        // leer un numero e indicar si es positivo  o negativo.
        // se debe iterar hasta que se introduzca un 0

        /*Scanner leer = new Scanner(System.in);

        var num = 0;

        do {

            System.out.println("Ingrese un numero");
            num = leer.nextInt();

            if(num > 0){

                System.out.println("El numero " + num + " es positivo");

            } else if (num < 0) {

                System.out.println("El numero " + num + " es negativo");

            } else {

                System.out.println("Ingresó el numero cero, ¡Fin!");

            }
        } while (num != 0);*/

        //ejercicio 4
        // repito el ejercicio anterior pero, con clase JOptionPane

        /*var num = 0;

        do {

            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

            if(num > 0){

                JOptionPane.showMessageDialog(null,"El numero " + num + " es positivo");

            } else if (num < 0) {

                JOptionPane.showMessageDialog(null,"El numero " + num + " es negativo");

            } else {

                JOptionPane.showMessageDialog(null,"Ingresó el numero cero, ¡Fin!");

            }
        } while (num != 0);
*/

        

    }
}