import os,shutil,glob,win32api

#todo: #Lock-----#Share# -Send To Desktop-Properties-- -



def cd(path):
    os.chdir(path)
def back():
    os.chdir('..')
def newfolder(Name):
    try:
        cd.mkdir(Name)
    except FileExistsError:
        #bind it to a dialog box containing the message below
        print('This Folder Already Exists')
def showcurdir():
    print(os.getcwd())


class Folder:
    def __init__(self,Path):
        self.Path=Path
        self.password=''
    def showdir(self):
        for x in os.listdir(self.Path):
            print(x)
    def compress(self,ArchieveName, Format,  DestPath):
        if Format == 'bztar' or Format == 'gztar' or Format == 'tar' or Format == 'xztar' or Format == 'zip':
            if '/' in ArchieveName or ':' in ArchieveName or '*' in ArchieveName or '?' in ArchieveName or '"' in ArchieveName or '<' in ArchieveName or '>' in ArchieveName or '|' in ArchieveName:
                print('Invalid FileName')
            else:
                shutil.make_archive(DestPath+'\\'+ArchieveName, Format, self.Path)

        else:
            print('Invalid Format')
    #def lock
    def delete(self):
        for i in os.listdir(self.Path):
            try:
                os.remove(self.Path+'\\'+i)
            except PermissionError:
                os.removedirs(self.Path+'\\'+i)
        os.removedirs(self.Path)
        #os.rmdir(
        #except FileNotFoundError:
         #   print('Theres No Folder Like That :)')
    def searchextension(self,extension):
        os.chdir(self.Path)
        for file in glob.glob("*."+extension):
            print(file)
    def searchfile(self,keyword):
        #its not case sensitive
        counter=0
        if type(keyword)==str:
            for i in os.listdir(self.Path):
                if keyword.lower() in i.lower():
                    print(i)
                    counter=1
            if counter==0:
                print('There was no file named %s in this directory'%(keyword))
        else:print('Invalid Input')
    def hidden(self):
        win32api.SetFileAttributes(self.Path, 0x02)
    def readonly(self):
        win32api.SetFileAttributes(self.Path, 0x01)
    def normal(self):
        win32api.SetFileAttributes(self.Path, 0x80)

class File:
    def __init__(self,Path):
        self.Path=Path
        self.password=''
        self.format=self.Path[self.Path.index('.')+1:len(self.Path)]
        self.dir=self.Path[:self.Path.index('.')-2]
    def copy(self,TargetPath):
        shutil.copy2(self.Path,TargetPath)
    def rename(self,NewName):
        os.rename(self.Path,self.dir+'\\'+NewName)
    def cut(self,TargetPath):
        shutil.copy2(self.Path,TargetPath)
        os.remove(self.Path)
    def delete(self):
        try:
            os.remove(self.Path)
        except FileNotFoundError:
            print('Theres No File Like That :)')
    def hidden(self):
        win32api.SetFileAttributes(self.Path, 0x02)
    def readonly(self):
        win32api.SetFileAttributes(self.Path, 0x01)
    def normal(self):
        win32api.SetFileAttributes(self.Path, 0x80)




file='C:\\Users\\Mahdi-PC\\Downloads\\Soroush Downloads\\Images\\1.png'
Dir='C:\\Users\\Mahdi-PC\\Downloads\\Soroush Downloads\\Images\\1'

#win32api.GetLogicalDriveStrings()
