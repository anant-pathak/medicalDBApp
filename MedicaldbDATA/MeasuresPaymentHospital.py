import psycopg2
import csv

def measure_hospital_rel_data_fetch(last_hospital_id):
    with open("/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Measure/Payment/Payment_and_value_of_careHospital.csv", "rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []
        hospitalId = ""
        for number, row in enumerate(cin, 0):
            # print(number)
            hospitalID = row[0]
            if hospitalID.isnumeric() and int(hospitalID) > last_hospital_id:
                break
            list_data = []
            list_data.append(row[0])
            list_data.append(row[8])
            list_data.append(row[12])
            list_data.append(row[10])
            hospitals_data.append(list_data)
        else:
            print("Read all the data")
        del hospitals_data[0]
        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data

def measure_hospital_rel_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO measure_hospital_rel VALUES(%s,%s,%s,%s)",(list_h[0],list_h[1],list_h[2], list_h[3]))
            connectionObj.commit()
        except Exception as e:
            print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
            continue
    connectionObj.commit()
    cursor.close()

