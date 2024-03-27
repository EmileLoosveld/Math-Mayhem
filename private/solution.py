#!/usr/bin/python

import socket

def main():
    # Verbind met de server
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    try:
        # Ontvang het welkomstbericht van de server
        print(client_socket.recv(1024).decode())

        # Speel het spel
        while True:
            # Ontvang de berekening van de server
            calculation = client_socket.recv(1024).decode()

            if 'dsctf' in calculation:
                print(calculation)
                break

            print("Berekening:", calculation)

            # Los de berekening op
            result = eval(calculation)
            print("Antwoord:", result)

            # Stuur het antwoord naar de server
            client_socket.send(str(result).encode())

    finally:
        # Sluit de verbinding met de server
        client_socket.close()

if __name__ == "__main__":
    main()

