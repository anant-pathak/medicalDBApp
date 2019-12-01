import csv
#deactivate
import psycopg2 as p
# from pg import DB
import MedicaldbDATA.Hospital as Hospital


Hospital.hospital_db_populate()

def hello():
    psycopg2.connect()
    # with open("/Users/anantpathak/OneDrive/PortlandStateUniversity/Year1/Sem1/Intro To DatabaseManagement/Project/Data/TablesRaw/Hospital/CSV-plain/Hospital_General_Information.csv", "rt") as fin:
    #     cin = csv.reader(fin)
    #     hospitals_data = []

    #     for number, row in enumerate(cin,0):
    #         print(number)
    #         list_data = []
    #         list_data.append(row[0])
    #         list_data.append(row[1])
    #         hospitals_data.append(list_data)
    #         if number == 10:
    #             break
    #     else: 
    #         print("break encountered")
        
    #     for list_h in hospitals_data:
    #         print(list_h)

    # Make a connection
    username = "f19wdb64" 
    passwrd = "Anant123!" 
    dataB = "f19wdb64"
    hostname = "dbclass.cs.pdx.edu"
   
    connection = connect(database=dataB, host=hostname, user=username, password=passwrd)
   # db = connectio
    #Define your Query
    query = "SELECT * FROM spy.Agent WHERE last LIKE 'W%'" 
    db.execute(query)
    # rows and columns/fields returned
    col_names = [desc[0] for desc in db.description] # fetch all the rows from the db
    rows = db.fetchall()
    print(col_names)
    #look at the rows, one-by-one
    for row in rows: print(row)
    #close the connection
    db.close()
    connection.close()

if __name__ == "__main__":
    hello()
        
    


