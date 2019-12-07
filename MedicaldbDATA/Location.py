import psycopg2
import csv


def location_data_fetch():
    with open(
            "/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Location/Hospital_General_Information.csv",
            "rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []

        for number, row in enumerate(cin, 0):
            # print(number)
            list_data = []
            list_data.append(row[5])  # zip
            list_data.append(row[3])  # city
            list_data.append(row[4])  # state
            list_data.append(row[6])  # county
            if not list_data in hospitals_data:
                hospitals_data.append(list_data)
            else:
                print("found a duplicate")
            if number == 200:
                break
        else:
            print("break encountered")
        del hospitals_data[0]
        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data


def location_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO location VALUES(%s,%s,%s,%s)",
                           (list_h[0], list_h[1], list_h[2], list_h[3]))
        except:
            print("may b the data already exists")
            continue
    connectionObj.commit()
    cursor.close()

# hospital_db_populate()
