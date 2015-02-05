class MySQL:
    connection = False
    cursor = False
    
    def __init__(self):
        import MySQLdb
        self.connection = MySQLdb.connect(host="127.0.0.1",  user="youruser",  passwd="yourpass",  db="yourdatabase" )
        self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor); 
    def query(self, sql):
        self.cursor.execute(sql) 
        fetchall = self.cursor.fetchall()
        
        Result = []
        
        class MRow(object): 
            pass
        Item = MRow() 
            
        for row in fetchall: 
            for k in row: setattr(Item, k, row[k] )
            Result.append(Item)
        return Result;
    
    def __del__(self):
        if(self.cursor!=False): self.cursor.close()
        if(self.connection!=False): self.connection.close()

class Model:
    def __init__(self):
       self.db = MySQL()
