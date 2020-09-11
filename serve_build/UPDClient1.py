from socket import *    
serverName = '127.0.0.1'#本机ip地址或者包含服务器的主机名
serverPort = 12000#整数变量		
clientSocket=socket(AF_INET,SOCK_DGRAM)#创建客户套接字 地址簇AF_IMET代表使用ipv4 SOCK_DGRAM为套接字类型代表使用UDP套接字
message = input('input lowercase sentence :') #输入进message
clientSocket.sendto(message.encode(),(serverName,serverPort)) #encode
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    
print(modifiedMessage)
print(serverAddress)
input('just for fun!!!')   
clientSocket.close()    


