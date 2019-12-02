import psycopg2

def Hospital_Specialization_data_populate(connectionObj, hospitals_data):
    cursor = connectionObj.cursor()
    for list_h in hospitals_data:
        try:
            cursor.execute("INSERT INTO hospital_specialization VALUES(%s)",
                           (list_h[0]))
        except:
            print("may b the data already exists")
            continue
    connectionObj.commit()
    cursor.close()