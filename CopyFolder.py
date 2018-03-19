import os,shutil
def CopyFolder(Path,Dest):
    FolderName=Path.split('\\')[-1]
    os.mkdir(Dest+'\\'+FolderName)
    for i in os.listdir(Path):
        if '.'  in i:
            tmp=Path+'\\'+i
            shutil.copy2(tmp,Dest+'\\'+FolderName)
        else:
            CopyFolder(Path+'\\'+i,Dest+'\\'+FolderName)
Path='C:\\Users\\Mahdi-PC\\Desktop\\Project\\20'
Dest='D:\\'
CopyFolder(Path,Dest)
