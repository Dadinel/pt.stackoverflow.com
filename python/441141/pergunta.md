    # script de carga 
    import csv 
    import mysql.connector
    
    # conexao com o banco 
    mysql = mysql.connector.connect(
        host='0.0.0.0',
        user='root',
        passwd='mysql',
        database='mydesenv',
        port=3306
    )
    cur=mysql.cursor()
    sql = """insert into mydesenv.tb_load (id, nm_name, dt_load) values (%s, %s, %s)"""
    #passo01 - Ler arquivo .csv
    csv_data = csv.reader('/Users/eduardoaandrad/Dropbox/Desenv/Script/csv/carga_teste.csv',delimiter=';')
    for row in csv_data:
        print(row)
        cur.execute(sql,row)
    
    mysql.commit()
    cur.close()
