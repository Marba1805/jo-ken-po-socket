#Jo-ken-po
#Feito por:
#Abram Grossmann – 31826131
#Victor Melly Cabredo - 31836895
import socket

IP = '192.168.56.1'
PORTA = 31826
BUFFER = 1024
JOGADAS_VALIDAS = ['PEDRA','PAPEL','TESOURA']

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((IP, PORTA))

servidor.listen(1)

print("Servidor dispoivel na porta 31826 e escutando.....") 

conn, addr = servidor.accept()
print ('Endereço conectado:', addr)

while True:
    data = conn.recv(BUFFER)
    if data:
        print ("Jogada recebida")
        jogada_cliente = data.decode('UTF-8')
        if jogada_cliente.upper() not in JOGADAS_VALIDAS:
            if jogada_cliente.upper() == "QUIT":
                print("fechando servidor")
                break
            print("Jogada do cliente foi inválida")
            conn.send("Jogada inválida".encode("UTF-8"))
        else:
            jogada_servidor = input("Insira sua jogada: ")
            while jogada_servidor.upper() not in JOGADAS_VALIDAS:
                print("Jogada do servidor foi inválida")
                jogada_servidor = input("Insira sua jogada: ")
        if jogada_servidor == jogada_cliente:
            print("Empatou")
            conn.send("Empatou".encode("UTF-8"))
        else:
            if (jogada_servidor.upper() == "PEDRA" and jogada_cliente.upper() == "PAPEL")or(jogada_servidor.upper() == "PAPEL" and jogada_cliente.upper() == "TESOURA")or(jogada_servidor.upper() == "TESOURA" and jogada_cliente.upper() == "PEDRA"):
                print("Cliente venceu!")
                conn.send("Cliente venceu".encode("UTF-8"))
            else:
                print("Servidor venceu!")
                conn.send("Servidor venceu".encode("UTF-8"))
        if jogada_cliente == "quit":
            print("fechando servidor...")
            break
conn.close()
servidor.close()
exit(0)
