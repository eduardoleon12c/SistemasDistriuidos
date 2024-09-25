import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClienteJava {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            Socket socket = new Socket("192.168.38.160", 5000); // Cambiar la IP según tu servidor

            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            DataInputStream in = new DataInputStream(socket.getInputStream());

            int number;

            while (true) {
                System.out.print("Ingresa un número entero (0 para salir): ");
                number = scanner.nextInt();

                // Enviar número al servidor
                out.writeInt(number);

                if (number == 0) {
                    System.out.println("Cerrando conexión...");
                    break;
                }

                // Recibir el número incrementado desde el servidor
                int incrementedNumber = in.readInt();
                System.out.println("Número incrementado desde el servidor: " + incrementedNumber);
            }

            in.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
