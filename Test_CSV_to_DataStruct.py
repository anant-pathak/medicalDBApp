import csv
#deactivate
import psycopg2 as p
# from pg import DB
import MedicaldbDATA.Hospital as Hospital
import MedicaldbDATA.Connection as Connection
import  MedicaldbDATA.CreateTables as CreateTables



def master_fn():

    username = "anantpathak"
    passwrd = "Anant123!"
    dataB = "medicaldb"
    hostname = "localhost"

    DbObj = Connection.DBConnection(username=username, password=passwrd, dbName=dataB, hostadd=hostname)
    if DbObj.connectToDb() == False:
         print("Connection failed")
    #create all the tables:
    CreateTables.create_tables(DbObj.connectionObj)
    #For table Hospital fetch data from CSV and put it in our medicalDb database in table hospital
    hospitalDataList = Hospital.hospital_data_fetch()
    Hospital.hospital_data_populate(DbObj.connectionObj, hospitalDataList)
    return DbObj

if __name__ == "__main__":
   DbObj = master_fn()
        
    


