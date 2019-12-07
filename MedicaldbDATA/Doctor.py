import psycopg2
import csv


def doctor_data_fetch(last_hospital_id): #31318 = last_hospital_id
    with open(
         "/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Doctor/DoctorDbSmall.csv","rt") as fin:
        cin = csv.reader(fin)
        hospitals_data = []
        lastDept = ""
        currentHospitalDept = []
        prevHospital = ""
        for number, row in enumerate(cin, 0):
            # print(number)
            hospital = row[27]
            currentDept = row[11]
            doctor_id = row[0]
            if not hospital.isnumeric():
                continue
            elif any(doctor_id in single_list for single_list in hospitals_data):
                continue
            elif prevHospital != hospital:
                currentHospitalDept = []
            elif currentDept in currentHospitalDept:
                continue
            elif int(hospital) > last_hospital_id:
                break
            #NOTE NOTE: This list is going to contain data for both Doctor and Hospital_dcotor_rel
            prevHospital = hospital
            currentHospitalDept.append(currentDept)
            list_data = []
            list_data.append(row[0]) #dID
            name = row[4] + " " + row[3]
            list_data.append(name) #name
            list_data.append(row[7]) #gender
            list_data.append(row[8]) #credentials
            list_data.append(row[11]) #Speciality
            list_data.append(row[27]) #Hospital ID
            hospitals_data.append(list_data)
        else:
            print("All rows visited")
        # del hospitals_data[0]
        # for list_h in hospitals_data:
        #     print(list_h)
        return hospitals_data

def doctor_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO doctor VALUES(%s,%s,%s,%s,%s,%s);",(list_h[0],list_h[1],list_h[2],list_h[3],list_h[4],list_h[5]))
            connectionObj.commit()
        except Exception as e:
            print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
            continue
    connectionObj.commit()
    cursor.close()

# hospital_db_populate()