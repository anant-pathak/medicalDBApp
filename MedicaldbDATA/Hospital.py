import psycopg2
import csv


def hospital_data_fetch():
    with open(
            "/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Hospital/CSV-plain/Hospital_General_Information.csv",
            "rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []

        for number, row in enumerate(cin, 0):
            # print(number)
            list_data = []
            list_data.append(row[0])
            list_data.append(row[1])
            list_data.append(row[8])
            list_data.append(row[10])
            list_data.append(row[12])
            list_data.append(row[9])
            hospitals_data.append(list_data)
            if number == 10:
                break
        else:
            print("break encountered")
        del hospitals_data[0]
        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data

def hospital_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s)",(list_h[0],list_h[1],list_h[2],list_h[3],list_h[4],list_h[5]))
        except:
            print("may b the data already exists")
            continue
    connectionObj.commit()
    cursor.close()

# hospital_db_populate()