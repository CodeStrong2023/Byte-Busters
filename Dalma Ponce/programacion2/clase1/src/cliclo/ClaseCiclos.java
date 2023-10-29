package cliclo;

public class ClaseCiclos {

    public static void main(String[] args) {

        // Clase 1 Java
        // Ciclo While se repide mientras la condicion sea verdadera

        var cont = 0;

        while (cont < 7) {
            System.out.println("Conteo = " + cont);
            cont++;
        }

        // ciclo do while se retite al menos una vez y continua
        // iterando mientras la condicion sea verdadera

        System.out.println("\n----------- \n");

        var contador = 0;

        do {

            System.out.println("contador = " + contador);
            contador++;

        } while (contador < 7);

        System.out.println("\n----------- \n");

        // ciclo for itera un numero determinado de veces


        for(var i = 0; i < 7; i++) {

            if(i % 2 == 0) {

                System.out.println("contando = " + i);
                break ;
            }

        }
        //La funcion break rompe el ciclo y lo detiene, deja de iterar
        // en este caso el bucle se va a detener al momento de imprimir lo que esta en el if

        System.out.println("\n----------- \n");

        inicio:   // etiqueta label
        for(var i = 0; i < 7; i++) {

            if(i % 2 != 0) {

                continue inicio;

            }
            System.out.println("contando2 = " + i);

        }
        // La funcion continue va a hacer que el ciclo continue iterando hasta finalizar
        // pero en este caso va a omitir las sentencias que se encuentren luego saltandolas


        // Etiqueta labels --> no es recomendable usar
        // nos permiten detemeninar especificamente donde continuar nuestro programa mediante las
        // funciones break y continue


    }
}
