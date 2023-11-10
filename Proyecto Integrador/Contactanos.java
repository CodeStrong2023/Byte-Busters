public class Contactanos {
    public static void main(String[] args) {
        System.out.println("-----------CONTACTANOS-----------------");
        System.out.println("");
        System.out.println("* ATENCION PERSONALIZADA");
        System.out.println("");
        System.out.println("* WHATSAPP");
        System.out.println("");
        System.out.println("* VISITAS A OBRAS");
        System.out.println("");
        System.out.println("* 0PAGOS INFORMADOS");
        System.out.println("");
        System.out.println("¿NO DUDES! CONTACTANOS");
        System.out.println("");

        String[][] contactos = new String[7][3];
        contactos[0][0] = "Brian Difilipo";
        contactos[0][1] = "2604511997";
        contactos[0][2] = "Briandifilipo@hotmail.com";
        contactos[1][0] = "Lucas Peralta";
        contactos[1][1] = "2604591821";
        contactos[1][2] = "lucas@hotmail.com";
        contactos[2][0] = "Dalma Ponce";
        contactos[2][1] = "3834000000";
        contactos[2][2] = "dalma@hotmail.com";
        contactos[3][0] = "Andrés Luna";
        contactos[3][1] = "2604034760";
        contactos[3][2] = "andresluna201@hotmail.com";
        contactos[4][0] = "Martin Ledezma";
        contactos[4][1] = "3512333714";
        contactos[4][2] = "martynledezma@gmail.com";
        contactos[5][0] = "Bruno de la Vega";
        contactos[5][1] = "2604628937";
        contactos[5][2] = "Brunodelavega@hotmail.com";
        contactos[6][0] = "Micaela Elsesser";
        contactos[6][1] = "2004023589";
        contactos[6][2] = "mikelsesser@gmail.com";

        for (int i = 0; i < 7; i++) {
            System.out.println("Nombre: " + contactos[i][0]);
            System.out.println("WhatsApp: " + contactos[i][1]);
            System.out.println("Email: " + contactos[i][2]);
            System.out.println("");
        }
    }
}
