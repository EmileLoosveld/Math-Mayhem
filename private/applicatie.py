import socket
import random
import select
import threading

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 12345))
        server_socket.listen(15)

        while True:
            client_socket, addr = server_socket.accept()
            print("New client connected:", addr)

            # Start een nieuwe thread om het spel te spelen voor elke nieuwe client
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()

    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        server_socket.close()

def handle_client(client_socket, addr):
    try:
        client_socket.send(b"Welcome to this calculation game!\nSolve the calculations and get the flag!\nYou have 5 seconds for every answer!\n")
        Play(client_socket, addr)
    finally:
        client_socket.close()

def Play(client_socket, addr):
    for i in range(10):
        result, calculation = CreateCalculation(i ** 2 + 1)
        client_socket.send(calculation.encode() + b"\n")

        ready = select.select([client_socket], [], [], 5)
        if ready[0]:
            client_input = client_socket.recv(1024).decode().strip()
            if client_input == str(result):
                continue
            else:
                client_socket.send(b"\nWrong answer, start over again!\n")
                Play(client_socket, addr)
                return
        else:
            client_socket.send(b"\nTimeout reached, start over again!\n")
            Play(client_socket, addr)
            return
    client_socket.send(b"dsctf{well_done}")

def CreateCalculation(amount):
    operators = ['+', '-', '*']
    calculation = str(random.randint(1, 100))

    for _ in range(amount):
        operator = random.choice(operators)
        number = random.randint(1, 100)
        calculation += f' {operator} {number}'

    result = eval(calculation)
    return result, calculation

if __name__ == "__main__":
    main()
