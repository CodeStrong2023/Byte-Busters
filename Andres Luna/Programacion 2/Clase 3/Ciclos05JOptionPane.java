/*
Ejercicio5: Realizar un juego para adivinar un número, para ello generar un número aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor 
o menor con respecto a N. El proceso termina cuando el usuario acierta a mostrarnos el 
número de intentos hechos. CLASE JOptionPane
 */
package ciclos05;
import javax.swing.JOptionPane;

public class Ciclos05JOptionPane {
        public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // ESTO GENERA UN NRO ALEATORIO
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            if(numero<aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número mayor: ");
            }
            else if(numero>aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número menor: ");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡¡¡FELICIDADES, HAS ADIVINADO EL NÚMERO!!!");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste el número en: "+conteo+" intentos");
    }
}