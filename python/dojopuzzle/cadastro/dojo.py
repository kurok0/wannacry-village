import getpass
from os import name
import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=xxxxxxxxx;" #inserir o server
                      "Database=xxxxx;" #inserir a database
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

##  No banco de dados, criar 1 tabela com 4 colunas
##  Nomear as colunas como name, email, usr e passwd

nameinput = input("Insira seu nome:\n")
mailinput = input("Insira seu email:\n")
with open("email", "r") as f:
    for l_num, l in enumerate(f, 1):
        if (mailinput in l):
            raise NameError("Este e-mail já existe.")
with open("email", "a") as mail:
    mail.write("***" + mailinput)
userinput = input("Insira seu usuário:\n")
with open("user", "r") as sf:
    for l_num, l in enumerate(sf, 1):
        if (userinput in l):
            print('Sugestão de usuários:')
            print(userinput[:2] + mailinput[:6])
            print(userinput[:4] + mailinput[:3])
            print(userinput[:6] + mailinput[:5])
            raise NameError("Este e-mail já existe.")
with open("user", "a") as user:
    user.write("***" + userinput)
if(userinput == mail):
    raise NameError("Este usuário já existe.")
mypass = getpass.getpass("Insira sua senha:\n")
print('Cadastro realizado com sucesso!')

cursor.execute(
'INSERT INTO xxxxxxx(name, email, usr, passwd) VALUES(?, ?, ?, ?)', (nameinput, mailinput, userinput, mypass))
##inserir a tab nos X acima.
cnxn.commit()
