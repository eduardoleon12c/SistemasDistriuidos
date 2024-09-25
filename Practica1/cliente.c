#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main() {
    int sock;
    struct sockaddr_in server;
    char message[1000], server_reply[2000];

    // Crear socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(5000);

    // Conectar al servidor
    connect(sock, (struct sockaddr *)&server, sizeof(server));

    // Enviar mensaje
    strcpy(message, "Hola");
    send(sock, message, strlen(message), 0);

    // Recibir respuesta
    recv(sock, server_reply, 2000, 0);
    printf("Servidor responde: %s\n", server_reply);

    // Cerrar socket
    close(sock);
    return 0;
}
