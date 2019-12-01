import psycopg2

def create_tables(connectionObj):
    queries = [
        "CREATE TABLE hospital (hID INT PRIMARY KEY, hName VARCHAR(50), hType VARCHAR(100), emergency VARCHAR(20), hRating VARCHAR(20), hOwnership VARCHAR(40));" ,
    ]
    cursor = connectionObj.cursor()
    for eachQuery in queries:
        try:
            cursor.execute(eachQuery)
        except:
            print("Table already exists")
            continue
    connectionObj.commit()
    cursor.close()
