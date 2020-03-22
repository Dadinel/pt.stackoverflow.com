# script de carga 
import csv 
import mysql.connector
import os.path

# conexao com o banco 
mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='CODINGGROUND'
)

cur = mysql.cursor()
sql = """insert into CODINGGROUND.tb_load (id, nm_name, dt_load) values (%s, %s, %s)"""

# Teste: Cria o arquivo para efetuar os testes...
if not os.path.exists('carga_teste.csv'):
    with open('carga_teste.csv', 'a') as csv_file:
        csv_file.write('id;name;load')

# Teste: Cria a tabela
try:
    table = mysql.cursor()
    table.execute("create table CODINGGROUND.tb_load (id varchar(50), nm_name varchar(50), dt_load varchar(50) )")
except:
    pass

#passo01 - Ler arquivo .csv
with open('carga_teste.csv') as carga:
    csv_data = csv.reader(carga, delimiter=';')
    for row in csv_data:
        print(row)
        cur.execute(sql,row)
        print("line inserted")

# Teste: Ler os dados gravados
data = mysql.cursor()
data.execute("select * from CODINGGROUND.tb_load")

for (cId, cName, cLoad) in data:
    print(cId, cName, cLoad)

mysql.commit()
cur.close()

print("Finished")
