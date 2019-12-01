import psycopg2

class DBConnection():
    def __init__(self, username, password, dbName, hostadd):
        self.username = username
        self.password = password
        self.dbName = dbName
        self.hostAdd = hostadd
        self.connectionObj = None

    def connectToDb(self):
        try:
            self.connectionObj = psycopg2.connect(database=self.dbName, host=self.hostAdd, user=self.username, password=self.password)
        except:
            print("Connection failed")
            return None
        return self.connectionObj

    @property
    def connectionObj(self):
        if self.connectionObj == None:
            return None
        else:
            return self.connectionObj

    #No setter for connectionobj

