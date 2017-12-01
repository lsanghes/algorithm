# https://azure.microsoft.com/en-us/documentation/articles/sql-database-develop-python-simple/
# pip install pymssql

# Export from MSSQL to CSV
def export_mssql():
    import pymssql, sqlalchemy, pandas as pd, csv
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.width', 1000)
    # conn = pymssql.connect(server='ldn-nt-sql003-1', user='user', password='pass', database='TRADELOADS')
    # conn = pymssql.connect(server='flsqlecc03') # use AD login
    # conn = sqlalchemy.create_engine('mssql+pymssql://user:pass@ldn-nt-sql003-1/TRADELOADS')
    conn = sqlalchemy.create_engine('mssql+pymssql://flsqlecc03')

    sql = '''
    SELECT top 10 * FROM [BrokRecs].[dbo].[USATurnover]
    where rec_name = 'CDCC'
    '''

    df = pd.read_sql(sql, conn)
    print(df)

    # df.to_csv(r'C:\Users\ssang\Downloads\mssql.csv', index=False, sep=',', encoding='utf-8', header=True, quoting=csv.QUOTE_MINIMAL)
    df.to_csv(r'C:\Users\ssang\Downloads\mssql.csv', index=False)

    writer = pd.ExcelWriter(r'C:\Users\ssang\Downloads\mssql.xlsx')
    df.to_excel(writer,'Sheet1', index=False)
    writer.save()

    # conn = sqlalchemy.create_engine('mssql+pymssql://user:pass@ldn-nt-sql003-1/TRADELOADS')
    # df.to_sql('CONTECH_CME_new_table1', conn, index=False)


# https://pypi.python.org/pypi/cx_Oracle/5.3
# ORACLE_HOME and PATH must point to C:\HOMEWARE\instantclient_12_1
# bug in cx_Oracle-5.3-12c.win-amd64-py3.5, MIGHT need to change HKEY_CURRENT_USER\Software\Python\PythonCore\3.5 to 3.5-32
# cx_Oracle-5.3-12c.win-amd64-py3.5-2 works fine

# Export from Oracle to CSV
def export_oracle():
    import cx_Oracle, sqlalchemy, pandas as pd, csv
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.width', 1000)

    # conn = cx_Oracle.connect('user/pass@na-cv-scan/clvp_app') #works for both SID and service_name
    # conn = sqlalchemy.create_engine('oracle://user:pass@apcvdb.ap.newedge.int/CVSBY_HK') # sid
    conn = sqlalchemy.create_engine('oracle://user:pass@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=na-cv-scan)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=clvp_app)))') # service_name

    sql = '''
    SELECT * FROM CV_WELCOME
    WHERE ROWNUM < 10
    '''

    df = pd.read_sql(sql, conn)
    print(df)

    # df.to_csv(r'C:\Users\ssang\Downloads\oracle.csv', index=False, sep=',', encoding='utf-8', header=True, quoting=csv.QUOTE_MINIMAL)
    df.to_csv(r'C:\Users\ssang\Downloads\oracle.csv', index=False)

    writer = pd.ExcelWriter(r'C:\Users\ssang\Downloads\oracle.xlsx')
    df.to_excel(writer,'Sheet1', index=False)
    writer.save()

# Import CSV into MSSQL
def import_mssql():
    import pymssql, sqlalchemy, pandas as pd, csv
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.width', 1000)
    df = pd.read_csv(r'C:\Users\ssang\Downloads\cdcc_turnover.csv')
    print(df)
    df2 = pd.read_excel(r'C:\Users\ssang\Downloads\mssql.xlsx', 'Sheet1')
    print(df2)


# export_mssql()
# export_oracle()
# import_mssql()