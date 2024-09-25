#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int server_sock, client_sock, client_len;
    struct sockaddr_in server_addr, client_addr;
    int number;

    // Crear socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock == -1) {
        printf("No se pudo crear el socket\n");
        return 1;
    }

    // Preparar la estructura sockaddr_in
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(5000);

    // Enlazar
    if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        printf("Error al enlazar\n");
        return 1;
    }

    // Escuchar conexiones
    listen(server_sock, 3);
    printf("Esperando conexiones en el puerto 5000...\n");

    client_len = sizeof(struct sockaddr_in);
    client_sock = accept(server_sock, (struct sockaddr *)&client_addr, (socklen_t*)&client_len);
    if (client_sock < 0) {
        printf("Error al aceptar la conexión\n");
        return 1;
    }

    while (1) {
        // Recibir número del cliente
        recv(client_sock, &number, sizeof(number), 0);
        number = ntohl(number); // Convertir de orden de red a host

        if (number == 0) {
            printf("Cierre de conexión solicitado por el cliente\n");
            break;
        }

        printf("Número recibido del cliente: %d\n", number);

        // Incrementar el número y enviarlo de regreso al cliente
        number++;
        number = htonl(number); // Convertir de host a orden de red
        send(client_sock, &number, sizeof(number), 0);
    }

    close(client_sock);
    close(server_sock);
    return 0;
}
