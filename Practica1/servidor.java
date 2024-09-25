import java.net.*;
import java.io.*;

public class ServidorTexto {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Servidor iniciado en el puerto 5000...");
        Socket clientSocket = serverSocket.accept();
        
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        
        String mensajeCliente = in.readLine();
        System.out.println("Cliente dice: " + mensajeCliente);
        out.println("Hola, ¿qué tal?");
        
        in.close();
        out.close();
        clientSocket.close();
        serverSocket.close();
    }
}
