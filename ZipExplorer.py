import zipfile
file='D:\\s.zip'
myzip=zipfile.ZipFile(file)
#hamun kare listdir ro mikone
myzip.namelist()
#hamun kare copy ro mishe kard
myzip.extract('extract.py','D:\\Games')

myzip.setpassword('Salam')

class zip:
    def __init__(self,path):
        self.Zip=zipfile.ZipFile(path)
    def extract(self,member,dest):
        self.Zip.extract(member,dest)