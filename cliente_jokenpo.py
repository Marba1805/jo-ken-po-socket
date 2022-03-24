#Jo-ken-po
#Feito por:
#Abram Grossmann – 31826131
#Victor Melly Cabredo - 31836895
import socket
import socket
import asyncio
IP = '192.168.56.1'
PORTA = 31826
BUFFER = 1024

def cria_socket():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return cliente

def abre_conexao(socket, IP, PORTA):
    socket.connect((IP, PORTA))

def envia_jogada(socket, jogada):
    socket.send(jogada.encode('UTF-8'))

def recebe_resultado(socket, BUFFER):
    data, addr = socket.recvfrom(BUFFER)
    return data.decode('UTF-8')

def main():
    cliente = cria_socket()
    abre_conexao(cliente, IP, PORTA)
    while True:
        jogada = input("Insira a sua jogada: ")
        envia_jogada(cliente, jogada)
        if jogada == "quit":
            print("fechando...")
            break
        print("Aguardando resultado do servidor")
        resultado_servidor = recebe_resultado(cliente, BUFFER)
        while resultado_servidor == '':
            resultado_servidor = recebe_resultado(cliente, BUFFER)
        print(resultado_servidor)
        if input("Deseja jogar mais uma vez? [s/N]") != "s":
            print("Fim de jogo")
            envia_jogada(cliente, "quit")
            break
    cliente.close()
    exit(0)

main()
