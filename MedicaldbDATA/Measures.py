import psycopg2
import csv

def measures_data_fetch():
    with open("/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Measure/Payment/PaymentNational.csv", "rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []

        for number, row in enumerate(cin, 0):
            # print(number)
            row[2] = row[2].strip('$')
            try:
                row[2] = int(float(row[2]))
            except ValueError:
                pass
            list_data = []
            list_data.append(row[0])
            list_data.append(row[1])
            list_data.append(row[2])
            hospitals_data.append(list_data)
        else:
            print("break encountered")
        del hospitals_data[0]
        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data

def measures_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO measure VALUES(%s,%s,%s)",(list_h[0],list_h[1],list_h[2]))
            connectionObj.commit()
        except Exception as e:
            print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
            continue
    connectionObj.commit()
    cursor.close()

