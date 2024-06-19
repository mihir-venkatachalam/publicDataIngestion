from yahoofinancials import YahooFinancials
import pandas as pd
from getCompanies import g_companies
from format import Data
import threading

companies = g_companies()
metrics = ["totalRevenue","grossProfit","eBITDA","totalOperatingExpenses"]
frequencies = {"quarterly":["incomeStatementHistoryQuarterly","Q"], "annual":["incomeStatementHistory","A"]}
prepared_data = []
data = {}
threads=[]



def getReport(companies):
    for company in companies:
        for frequency in frequencies:
            reports = YahooFinancials(company["ticker"]).get_financial_stmts(frequency, ['income'])[frequencies[frequency][0]][company["ticker"]]
            for entry in reports:
                for dateFiled in entry:
                    for metric in list(entry[dateFiled].keys()):
                        if metric in metrics:
                            data = Data(company["name"], frequencies[frequency][1], metric, dateFiled,
                                        entry[dateFiled][metric], "yahooFinance")
                            prepared_data.append(data.row())


def getCompany():
    for company in range(0,len(companies), 4):
            thread = threading.Thread(target=getReport, args=(companies[company:company+4],))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    df = pd.DataFrame(prepared_data)
    df.to_csv("yahoofinancials.csv")

    print(df)

getCompany()