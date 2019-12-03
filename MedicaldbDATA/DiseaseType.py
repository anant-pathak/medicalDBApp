import psycopg2
import csv

def DiseaseType_and_patientsVisited_data_fetch(last_hospital_id):
    with open(
            "/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Patients_visited/Outpatient_Procedures_Volume.csv",
            "rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []
        hospitalID = ""
        for number, row in enumerate(cin, 0):
            # print(number)
            hospitalID = row[0]
            if hospitalID.isnumeric() and int(hospitalID) > last_hospital_id:
                break
            list_data = []
            list_data.append(row[0]) #Hid
            list_data.append(row[3]) #Disease1 ...
            list_data.append(row[4])
            list_data.append(row[5])
            list_data.append(row[6])
            list_data.append(row[7])
            list_data.append(row[8])
            list_data.append(row[9])
            list_data.append(row[10])
            list_data.append(row[11])
            hospitals_data.append(list_data)
        else:
            print("Read all the data")

        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data


def DiseaseType_and_patientsVisited_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    disease_types = hospitals_data[0] #it's an array & we are interested in column: 3-11
    del disease_types[0] #Since it'd contain Name: Facility ID & that is not a disease type.
    for index in range(9):
        try:
            cursor.execute("INSERT INTO disease_type VALUES(%s)", (disease_types[index],))
            connectionObj.commit()
        except Exception as e:
            print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
            continue
    del hospitals_data[0] #bcz the first row is for table: disease_type only.
    for list_h in hospitals_data:
        hospital_id = list_h[0]
        for index in range(9): #bcz diseases: 3-11 = 9
            try:
                cursor.execute("INSERT INTO hospital_disease_visitors_rel VALUES(%s, %s, %s)",
                               (hospital_id, disease_types[index], list_h[index]))
                connectionObj.commit()
            except Exception as e:
                print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
                continue
    connectionObj.commit()
    cursor.close()