import pandas as pd
import pymssql
import datetime
import time
import os

conn = pymssql.connect(server='ldn-nt-sql003-1', user='fimaclear_administrator', password='admin00', database='TRADELOADS')
path = 'R:\\stanley\\CME\\'
map_file = 'map_stan.xlsx'

def get_prompt(s):
    yyyy = mm = ''
    d = {'F':'01','G':'02','H':'03','J':'04','K':'05','M':'06','N':'07','Q':'08','U':'09','V':'10','X':'11','Z':'12'}
    yyyy = '201' + s[1]
    prompt = datetime.date(int(yyyy), int(d[s[0]]), 1)
    if prompt < datetime.date.today():
        prompt = datetime.date(prompt.year + 10, prompt.month, prompt.day)
    return prompt.strftime('%Y%m')

def run_rec(input_file):
    print('-------- rec started for ' + input_file + ' --------')
    xls =  pd.ExcelFile(path + input_file)
    df_file = xls.parse('Trade Vertical Results')
    xls = pd.ExcelFile(path + map_file)
    df_map = xls.parse('Sheet1')
    df_file = df_file[~df_file['Instrument'].str.contains(' ')]
    df_file = df_file[~df_file['Instrument'].str.contains('-')]
    df_file = df_file[~df_file['Instrument'].str.contains(':')]
    df_file = df_file[['Trade Date', 'Account','Side','Quantity','Instrument','Price']]
    df_file['TDATE'] = df_file['Trade Date'].apply(lambda x: datetime.datetime.strptime(x,'%m/%d/%Y').strftime('%Y%m%d'))
    df_file['prompt'] = df_file['Instrument'].str[-2:]
    df_file['exch_symbol'] = df_file['Instrument'].str[:-2]
    df_file['QTY_FILE'] = df_file['Quantity']
    df_file['QTY_GMI'] = 0
    df_file = pd.merge(df_file, df_map, how='left', on=['exch_symbol'])
    df_file = df_file[~pd.isnull(df_file['exch'])] # missing mapping
    df_file.loc[df_file['Side'] == 'Buy', 'BS'] = 1
    df_file.loc[df_file['Side'] == 'Sell', 'BS'] = 2
    df_file['BS'] = df_file['BS'].astype('int')
    df_file['exch'] = df_file['exch'].map(str).apply(lambda x: x.zfill(2))
    df_file['fc'] = df_file['fc'].map(str).apply(lambda x: x.zfill(2))
    df_file['EXCH_FC'] = df_file['exch'] + df_file['fc']
    df_file['TPRIC'] = df_file['Price']/df_file['multiplier']
    df_file['CTYM'] = df_file['prompt'].apply(get_prompt)

    gmi_accounts = ', '.join(["''" + str(i) + "''" for i in set(df_file['Account'].values)])
    sql = """
    SELECT * FROM OPENQUERY(repsqlprod01, '
        SELECT DISTINCT ACCOUNT_GROUP_LEVEL_1 AS FIRM
        FROM fimacis.dbo.ACCOUNT_MASTER
        WHERE ACCOUNT_GROUP_LEVEL_2 + ACCOUNT_GROUP_LEVEL_3
        IN ({})
    ')
    """.format(gmi_accounts)
    gmi_firm = pd.read_sql(sql, conn)

    if len(gmi_firm) > 1:
        print('ERROR more than one firm!!!')
    firm = gmi_firm.iloc[0,0]

    df_file['FIRM_OFF_ACCT'] = df_file['Account'].apply(lambda x: firm + str(x))


    firm_office_acct = ', '.join(["''" + str(i) + "''" for i in set(df_file['FIRM_OFF_ACCT'].values)])
    sql = """
    SELECT * FROM OPENQUERY(repsqlprod01, '
        SELECT DISTINCT ACCOUNT_GROUP_LEVEL_5 AS GMI_ENV
        FROM FIMACIS.DBO.ACCOUNT_MASTER
        WHERE ACCOUNT_GROUP_LEVEL_1 + ACCOUNT_GROUP_LEVEL_2 + ACCOUNT_GROUP_LEVEL_3
        IN ({})
    ')
    """.format(firm_office_acct)
    # print(sql)
    GMI_ENV = pd.read_sql(sql, conn)
    if len(GMI_ENV) > 1:
        print('ERROR more than one gim environment!!!')
    GMI_ENV = GMI_ENV.iloc[0, 0]

    FIRM_OFF_ACCTS = ', '.join(["''" + str(i) + "''" for i in set(df_file['FIRM_OFF_ACCT'].values)])
    TEXCHES = ', '.join(["''" + str(i) + "''" for i in set(df_file['exch'].values)])
    TDATES = ', '.join(["''" + str(i) + "''" for i in set(df_file['TDATE'].values)])
    print('FIRM_OFF_ACCT: ' + FIRM_OFF_ACCTS)
    print('TEXCH: ' + TEXCHES)
    print('TDATE: ' + TDATES)
    df_file = df_file[['TDATE', 'EXCH_FC', 'FIRM_OFF_ACCT', 'CTYM', 'BS', 'TPRIC', 'QTY_GMI', 'QTY_FILE' ]]
    sql = """
    SELECT
        TTDATE                  AS TDATE,
        TEXCH + TFC             AS EXCH_FC,
        TFIRM + TOFFIC + TACCT  AS FIRM_OFF_ACCT,
        TCTYM                   AS CTYM,
        TBS                     AS BS,
        TTPRIC                  AS TPRIC,
        TQTY                    AS QTY_GMI,
        0                       AS QTY_FILE
    FROM OPENQUERY(AS400, '
        SELECT * FROM {}.GMITH1F1
        WHERE 1 = 1
        AND TRECID IN (''T'', ''B'', ''Q'')
        AND TFIRM || TOFFIC || TACCT IN ({})
        AND TEXCH IN ({})
        AND TTDATE IN ({})
        --FETCH FIRST 10 ROW ONLY
    ')
    """.format(GMI_ENV, FIRM_OFF_ACCTS, TEXCHES, TDATES )

    start = time.time()
    print('Querying GMITH1F1...')
    df_gmi = pd.read_sql(sql, conn)
    elapsed = (time.time() - start)
    print(str(len(df_gmi)) + ' records')
    print(str(datetime.timedelta(seconds=elapsed)))

    sql = """
    SELECT
        FTDATE                  AS TDATE,
        FEXCH + FFC             AS EXCH_FC,
        FFIRM + FOFFIC + FACCT  AS FIRM_OFF_ACCT,
        FCTYM                   AS CTYM,
        FBS                     AS BS,
        FTPRIC                  AS TPRIC,
        FQTY                    AS QTY_GMI,
        0                       AS QTY_FILE
    FROM OPENQUERY(AS400, '
        SELECT * FROM {}.GMITRNF1
        WHERE 1 = 1
        AND FRECID IN (''T'', ''B'', ''Q'')
        AND FFIRM || FOFFIC || FACCT IN (''Q15048700'')
        AND FEXCH IN (''16'', ''04'', ''01'', ''07'')
        AND FTDATE IN (''20161109'')
        --FETCH FIRST 10 ROW ONLY
    ')
    """.format(GMI_ENV, FIRM_OFF_ACCTS, TEXCHES, TDATES )

    start = time.time()
    print('Querying GMITRNF1...')
    df_gmi_trn = pd.read_sql(sql, conn)
    elapsed = (time.time() - start)
    print(str(len(df_gmi_trn)) + ' records')
    print(str(datetime.timedelta(seconds=elapsed)))

    if len(df_gmi_trn) > 0:
        df_gmi = pd.concat([df_gmi, df_gmi_trn])

    df_gmi['TDATE'] = df_gmi['TDATE'].astype('int').astype('str')
    df_gmi['BS'] = df_gmi['BS'].astype('int')
    df_gmi['QTY_GMI'] = df_gmi['QTY_GMI'].astype('int')
    df_gmi['QTY_FILE'] = df_gmi['QTY_FILE'].astype('int')
    # save file to csv
    df_gmi.to_csv(path+input_file+'_gmi.csv', index=False)

    print('File rows : {}'.format(len(df_file)))
    print('GMI  rows : {}'.format(len(df_gmi)))

    df_union = pd.concat([df_gmi, df_file])
    df_groupby = df_union.groupby(['TDATE', 'EXCH_FC', 'FIRM_OFF_ACCT', 'CTYM', 'BS', 'TPRIC']).sum()
    df_result = pd.DataFrame(df_groupby.to_records())
    df_result['FULLY_MATCHED'] = df_result['QTY_GMI'] == df_result['QTY_FILE']
    df_result.to_csv(path+input_file+'_result.csv', index=False)
    print('-------- rec done for ' + input_file + ' --------')

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('xlsx') and filename != 'map_stan.xlsx':
            print(filename)
            run_rec(filename)
