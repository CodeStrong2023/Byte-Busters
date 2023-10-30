/*
ejercicio 7: Pedir números hasta que se introduzca uno negativo y calcular el promedio
 */
package ejercicio7;
import javax.swing.JOptionPane;

public class Ejercicio07JOptionPane {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        while(numero >= 0){ //mientras el nro no sea negativo
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null,"\nError, la division entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;  //suma y conteo son enteras, para convertir se pone float
            JOptionPane.showMessageDialog(null,"\nEl promedio es: "+promedio);
        }
    }
}
