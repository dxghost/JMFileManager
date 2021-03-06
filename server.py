import socket
import threading
import os
import time
import psutil
import shutil



class server:
    def __init__(self):
        self.commandSock = socket.socket()
        self.commandPort = 8080
        self.transferSock = socket.socket()
        self.transferPort = 8088
        self.chatSock=socket.socket()
        self.chatPort=8085
        self.host = ''
        self.bindsocket()

    def bindsocket(self):
        self.commandSock.bind((self.host, self.commandPort))
        self.transferSock.bind((self.host, self.transferPort))
        self.chatSock.bind((self.host,self.chatPort))
        self.commandSock.listen(10)
        self.transferSock.listen(10)
        self.chatSock.listen(10)

        self.filename = ""
        print ("Waiting for a connection.....")
        self.clientTransferSock, self.transferAddr = self.transferSock.accept()
        self.clientCommandSock, self.commandAddr = self.commandSock.accept()
        self.clientChatSock , self.chatAddr = self.chatSock.accept()

        print("Got a transfer connection from %s" % str(self.transferAddr))
        print("Got a command connection from %s" % str(self.commandAddr))
        print("Got a chat connection from %s" % str(self.chatAddr))

        self.sendPartitions()
        self.clientCommandSock.send(('Partitions Sent').encode('utf-8'))
        print('Partitions Sent!')

    def closeServer(self):
        self.clientCommandSock.close()
        self.clientTransferSock.close()
        self.clientChatSock.close()

    def dicision(self):
        while True:
            self.message = (self.clientCommandSock.recv(32)).decode('utf-8')
            #(self.message)
            if self.message == 'Delete Request':
                self.clientCommandSock.send('Delete Request Received'.encode('utf-8'))
                self.delete()
            elif self.message == 'Copy Request':
                self.clientCommandSock.send('Copy Request Received'.encode('utf-8'))
                self.copy()
            elif self.message == 'Send File Request':
                self.clientCommandSock.send('Send File Request Received'.encode('utf-8'))
                self.sendFile()
            elif self.message == 'Listdir Request':
                self.clientCommandSock.send('Listdir Request Received'.encode('utf-8'))
                self.listdir()
            elif self.message == 'Chat Request':
                self.clientCommandSock.send('Chat Request Received'.encode('utf-8'))
                self.chat()
            elif self.message == 'Mkdir Request':
                self.clientCommandSock.send('Mkdir Request Received'.encode('utf-8'))
                self.mkdir()

    def chat(self):
        self.chatfile=open('chatfile.txt','w')
        self.message = self.clientChatSock.recv(128).decode('utf-8')
        self.chatfile.write(self.message+'\n')
        self.chatfile.close()
        print(self.message)

    def mkdir(self):
        self.mkdirPath = self.clientCommandSock.recv(128).decode('utf-8')
        try:
            os.mkdir(self.mkdirPath)
            self.clientCommandSock.send('Directory Made'.encode('utf-8'))
            print ('Directory Made Successfully!')
        except:
            self.clientCommandSock.send('Directory Already Exist'.encode('utf-8'))
            print ('Directory Already Exist')

    def send(self, directory):
        print(directory)
        self.filename = directory.split('\\')[len(directory.split('\\')) - 1]
        self.filename = self.filename.encode('utf-8')
        self.nameSize = len(self.filename)
        self.nameSize = str(self.nameSize).encode('utf-8')
        self.clientTransferSock.send(self.nameSize)
        while (self.clientTransferSock.recv(32)).decode('utf-8') != 'Name Size Received':
            print('Waiting for Name Size to deliver...')
            time.sleep(1)
        else:
            print('Name Size Delivered!')
        self.clientTransferSock.send(self.filename)
        while (self.clientTransferSock.recv(32)).decode('utf-8') != 'File Name Received':
            print('Waiting for File Name to deliver...')
            time.sleep(1)
        else:
            print('File Name Delivered!')
        self.filename = self.filename.decode('utf-8')

        # filename = os.path.join(path,filename)
        self.fileSize = os.path.getsize(directory)
        self.fileSize = str(self.fileSize).encode('utf-8')
        self.clientTransferSock.send(self.fileSize)
        while (self.clientTransferSock.recv(32)).decode('utf-8') != 'File Size Received':
            print('Waiting for File Size to deliver...')
            time.sleep(1)
        else:
            print('File Size Delivered!')
        file_to_send = open(directory, 'rb')

        lines = file_to_send.read()
        self.clientTransferSock.sendall(lines)
        file_to_send.close()

        while (self.clientTransferSock.recv(32)).decode('utf-8') != 'File Received':
            print('Waiting for File to deliver...')
            time.sleep(1)
        else:
            print('File Delivered Successfully!')

    def delete(self):
        self.deleteDirectory = self.clientCommandSock.recv(128).decode('utf-8')
        try:
            os.remove(self.deleteDirectory)
            self.clientCommandSock.send('File Deleted'.encode('utf-8'))
            print ('Delete successfully!')
        except:
            self.clientCommandSock.send('File Not Found'.encode('utf-8'))
            print ('File not found!')

    def copy(self):
        self.pathes = (self.clientCommandSock.recv(128).decode('utf-8')).split(',')
        print(self.pathes)
        #shutil.copy2(self.pathes[0], self.pathes[1])
        try:
            shutil.copy2(self.pathes[0], self.pathes[1])
            self.clientCommandSock.send('File Copied'.encode('utf-8'))
            print ('Copied successfully!')
        except:
            self.clientCommandSock.send('File Not Found or Access Denied'.encode('utf-8'))
            print ('File Not Found or Access Denied')

    def sendFile(self):
        self.sendFileDirectory = self.clientCommandSock.recv(128).decode('utf-8')
        self.clientCommandSock.send('File Directory Received'.encode('utf-8'))
        threading.Thread(target=self.send, args=(self.sendFileDirectory,)).start()

    def sendPartitions(self):
        self.dps_defualt = psutil.disk_partitions()
        fmt_str = "{:<8}"
        fmt_str.format("Opts")
        self.dps = [chr(x) + ":" for x in range(65, 90) if os.path.exists(chr(x) + ":")]
        self.clientCommandSock.send((str(self.dps)).encode('utf-8'))

    def listdir(self):

        self.listdirPath = self.clientCommandSock.recv(128).decode('utf-8')
        self.clientCommandSock.send('Listdir Path Received'.encode('utf-8'))
        self.clientCommandSock.send(str(len(str(os.listdir(self.listdirPath)))).encode('utf-8'))
        while (self.clientCommandSock.recv(32)).decode('utf-8') != 'Listdir Size Received':
            print('Waiting for Listdir Size to deliver...')
            time.sleep(1)
        else:
            print('Listdir Size Delivered!')
        self.clientCommandSock.sendall(str(os.listdir(self.listdirPath)).encode('utf-8'))
        while (self.clientCommandSock.recv(32)).decode('utf-8') != 'Listdir Received':
            print('Waiting for Listdir to deliver...')
            time.sleep(1)
        else:
            print('Listdir Delivered!')



if __name__ == '__main__':
    myServer = server()
    threading.Thread(target=myServer.dicision()).start()

