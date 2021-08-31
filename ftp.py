import ftplib, os 
 
# IPv4 do ftp server 
ftp = ftplib.FTP('10.107.134.8') 
# Usuário e senha no ftp 
ftp.login('aluno', 'Mud@r123') 
 
                              # Diretório com os arquivos a serem enviados ao ftp 
for _, _, arquivos in os.walk('c:/vbox/ftp/arquivos'): 
    for arquivo in arquivos:         
        uploadfile = open(f"c:/vbox/ftp/arquivos/{arquivo}", 'rb') 
        ftp.storlines('STOR ' + arquivo, uploadfile)