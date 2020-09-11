from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))  #为socket分配端口号
print ('the server is ready to receive:')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)    #\\一定要缩进，不然会报错
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)

