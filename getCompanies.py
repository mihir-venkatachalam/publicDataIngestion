import csv


def g_companies():
    SnpComps = []
    with open('nasdaq.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            SnpComps.append({"ticker":row[0],"name":row[1]})
    return SnpComps


