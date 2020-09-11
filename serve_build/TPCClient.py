from socket import * 
serverName='127.0.0.1'#'servername'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))
sentence=input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence=clientSocket.recv(1024)
print('From Server:',modifiedSentence.decode())
clientSocket.close()