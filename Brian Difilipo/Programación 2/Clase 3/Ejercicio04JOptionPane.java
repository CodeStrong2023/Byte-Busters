/*
Ejercicio04: Pedir números hasta que se teclee uno negativo y mostrar cúantos números
se han introduciodo.
JOptionPane
 */
package ciclos04;
import javax.swing.JOptionPane;
public class Ejercicio04JOptionPane {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero= Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero>= 0){
            JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
            conteo++;
            numero= Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" números que son POSITIVO");
    }
}
