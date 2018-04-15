import socket
import os
import time
import threading
import psutil



# import thread
class client:
    def __init__(self, commandPort, transferPort, host):
        self.commandSock = socket.socket()
        self.commandPort = commandPort
        self.transferSock = socket.socket()
        self.transferPort = transferPort
        self.host = host

    def connectToServer(self):
        self.commandSock.connect((self.host, self.commandPort))
        self.transferSock.connect((self.host, self.transferPort))
        self.dps = eval(self.commandSock.recv(2 ** 10).decode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Partitions Sent':
            print('Waiting for Partitions to receive...')
            time.sleep(1)
        else:
            print('Partitions Received!')
        print(self.dps)
        return self.dps

    def recive(self, seveDirectory=''):
        print ('Receiving...')
        self.size = self.transferSock.recv(128)
        self.transferSock.send('Name Size Received'.encode('utf-8'))
        # if not self.size:
        # break
        self.size = int(self.size.decode('utf-8'))
        self.filename = self.transferSock.recv(self.size)
        self.transferSock.send('File Name Received'.encode('utf-8'))
        self.filesize = self.transferSock.recv(64)
        self.transferSock.send('File Size Received'.encode('utf-8'))
        self.filesize = int(self.filesize.decode('utf-8'))
        print(self.filename)
        self.file_to_write = open(seveDirectory + self.filename.decode('utf-8'), 'wb')
        self.chunksize = 4096
        def fileReceiving():
            while self.filesize > 0:
                if self.filesize < self.chunksize:
                    self.chunksize = self.filesize
                self.data = self.transferSock.recv(self.chunksize)
                self.file_to_write.write(self.data)
                self.filesize -= len(self.data)
            else:
                self.file_to_write.close()
                print ('File received successfully!')
                self.transferSock.send('File Received'.encode('utf-8'))

        threading.Thread(target=fileReceiving).start()

    def deleteRequest(self, fileDirectory):
        self.commandSock.send(('Delete Request').encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Delete Request Received':
            print('Waiting for Delete Request to deliver...')
            time.sleep(1)
        else:
            print('Delete Request Delivered!')
        self.commandSock.send((fileDirectory).encode('utf-8'))
        self.deleteStatus = (self.commandSock.recv(32)).decode('utf-8')
        while (self.deleteStatus != 'File Deleted' and self.deleteStatus != 'File Not Found'):
            print('Waiting for Delete Status...')
            time.sleep(1)
        else:
            if self.deleteStatus == 'File Deleted':
                print('File Deleted Successfully!')
            elif self.deleteStatus == 'File Not Found':
                print('File Not Found!')

    def copyRequest(self, fileDirectory, distanationPath):
        self.commandSock.send(('Copy Request').encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Copy Request Received':
            print('Waiting for Copy Request to deliver...')
            time.sleep(1)
        else:
            print('Copy Request Delivered!')
        self.commandSock.send((fileDirectory + ',' + distanationPath).encode('utf-8'))
        self.deleteStatus = (self.commandSock.recv(32)).decode('utf-8')
        while (self.deleteStatus != 'File Copied' and self.deleteStatus != 'File Not Found or Access Denied'):
            print('Waiting for Copy Status...')
            time.sleep(1)
        else:
            if self.deleteStatus == 'File Copied':
                print('File Copied Successfully!')
            elif self.deleteStatus == 'File Not Found or Access Denied':
                print('File Not Found or Access Denied!')

    def sendFileRequest(self, fileDirectory):
        self.commandSock.send(('Send File Request').encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Send File Request Received':
            print('Waiting for Send File Request to deliver...')
            time.sleep(1)
        else:
            print('Send File Request Delivered!')
        self.commandSock.send((fileDirectory).encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'File Directory Received':
            print('Waiting for File Directory to deliver...')
            time.sleep(1)
        else:
            print('File Directory Delivered!')
            threading.Thread(target=self.recive()).start()

    def listdirRequest(self, path):
        self.commandSock.send(('Listdir Request').encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Listdir Request Received':
            print('Waiting for Listdir Request to deliver...')
            time.sleep(1)
        else:
            print('Listdir Request Delivered!')
        self.commandSock.send(path.encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Listdir Path Received':
            print('Waiting for Listdir Path to deliver...')
            time.sleep(1)
        else:
            print('Listdir Path Delivered!')
        self.listdirSize = int((self.commandSock.recv(128)).decode('utf-8'))
        self.commandSock.send(('Listdir Size Received').encode('utf-8'))
        self.listdir = ''
        self.chunksize = 4096
        while self.listdirSize > 0:
            if self.listdirSize < self.chunksize:
                self.chunksize = self.listdirSize
            self.data = self.commandSock.recv(self.chunksize).decode('utf-8')
            self.listdir += self.data
            self.listdirSize -= len(self.data)
        else:
            self.listdir = eval(self.listdir)
            print ('Listdir received successfully!')
            self.commandSock.send('Listdir Received'.encode('utf-8'))
        print(self.listdir)
        return self.listdir

    def mkdirRequest(self, path):
        self.commandSock.send(('Mkdir Request').encode('utf-8'))
        while (self.commandSock.recv(32)).decode('utf-8') != 'Mkdir Request Received':
            print('Waiting for Mkdir Request to deliver...')
            time.sleep(1)
        else:
            print('Mkdir Request Delivered!')
        self.commandSock.send((path).encode('utf-8'))
        self.mkdirStatus = (self.commandSock.recv(32)).decode('utf-8')
        while (self.mkdirStatus != 'Directory Made' and self.mkdirStatus != 'Directory Already Exist'):
            print('Waiting for Making Status...')
            time.sleep(1)
        else:
            if self.mkdirStatus == 'Directory Made':
                print('Directory Made Successfully!')
            elif self.mkdirStatus == 'Directory Already Exist':
                print('Directory Already Exist!')

    def closeSocket(self):
        self.commandSock.close()
        self.transferSock.close()


if __name__ == '__main__':
    myClient = client(8000, 9000, socket.gethostname())
    myClient.connectToServer()
    myClient.sendFileRequest('C:\\Users\\moham\\Downloads\\Video\\Fereshteha_Ba_Ham_Miayand_HD_(Doostiha.NET)_2.mkv')
    myClient.deleteRequest('C:\\Users\\moham\\Desktop\\12271.jpg')
    myClient.copyRequest('D:\\Pictures\\Baby Wallpapers\\4K\\325.jpg', 'C:\\Users\\moham\\Desktop\\')
    myClient.listdirRequest('D:\\Music\\100 billboard')
    myClient.mkdirRequest('C:\\Users\\moham\\Desktop\\x')
    # myClient.closeSocket()
