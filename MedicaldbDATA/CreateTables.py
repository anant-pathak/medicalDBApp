import psycopg2

def create_tables(connectionObj):
    queries = [
        "CREATE TABLE hospital (hID INT PRIMARY KEY, hName VARCHAR(50), hType VARCHAR(100), emergency VARCHAR(20), hRating VARCHAR(20), hOwnership VARCHAR(40));" ,
        "CREATE TABLE location (zip INT NOT NULL, city VARCHAR(20) NOT NULL, state VARCHAR(20) NOT NULL, county VARCHAR(30), PRIMARY KEY (zip, city, state));",
        "CREATE TABLE hospital_location_rel (hID INT NOT NULL, zip INT NOT NULL, city VARCHAR(20) NOT NULL, state VARCHAR(20) NOT NULL, st_add VARCHAR(200), ph_number VARCHAR(30), PRIMARY KEY (hID, zip, city, state) , FOREIGN KEY (hID) REFERENCES hospital(hID), FOREIGN KEY (zip, city, state) REFERENCES location(zip, city, state));",
        "CREATE TABLE doctor (dID INT PRIMARY KEY, dName VARCHAR(300) NOT NULL, gender VARCHAR(50), credential VARCHAR(100), speciality VARCHAR(500));",
        "CREATE TABLE hospital_doctor_rel (hID INT REFERENCES hospital(hID), dID INT REFERENCES doctor(dID), dept VARCHAR(100), PRIMARY KEY (hID, dID));",
        "CREATE TABLE disease_type (dName VARCHAR(100) PRIMARY KEY);",
        "CREATE TABLE hospital_disease_visitors_rel (hId INT REFERENCES hospital(hid), dName VARCHAR(100) REFERENCES disease_type(dName), visitors_count INT, PRIMARY KEY (hId, dName));",
        "CREATE TABLE measure (measure_id VARCHAR(200) PRIMARY KEY, measure_name text, national_rate INT);",
        "CREATE TABLE measure_hospital_rel (hid INT REFERENCES hospital(hid),measure_id VARCHAR(200) REFERENCES measure(measure_id),payment INT,payment_category TEXT,PRIMARY KEY(hid, measure_id));",


    ]
    cursor = connectionObj.cursor()
    for eachQuery in queries:
        try:
            cursor.execute(eachQuery)
            connectionObj.commit()
        except:
            print("Table already exists")
            continue
    # connectionObj.commit()
    cursor.close()
