import psycopg2

class DBConnection():

    def __init__(self, username, password, dbName, hostadd):
        self.username = username
        self.password = password
        self.dbName = dbName
        self.hostAdd = hostadd


    def connectToDb(self):
        try:
            self.connectionObj = psycopg2.connect(host=self.hostAdd, database=self.dbName, user=self.username, password=self.password)
        except:
            print("Connection failed")
            return False
        return self.connectionObj

    # @property
    # def connectionObj(self):
    #     if self.connectionObj == None:
    #         return None
    #     else:
    #         return self.connectionObj

    #No setter for connectionobj

