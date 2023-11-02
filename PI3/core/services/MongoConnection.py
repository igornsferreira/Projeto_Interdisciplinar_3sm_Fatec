from .ConexaoService import ConexaoService


class MongoConnection:
    def __init__(self,connection, db_name) -> None:
        self.client = connection.getConnection()
        self.db = self.client[db_name]
        
    
    def insert(self, collection_name, **kwargs):
        data = {}
        collection = self.db[collection_name]
        for key, value in kwargs.items():
            data[key] = value
        
        collection.insert_one(data)

    def find(self, collection_name, **kwargs):
        collection = self.db[collection_name]
        return collection.find_one(kwargs)
    
    def findAll(self, colletion_name, **kwargs):

        collection = self.db[colletion_name]
        return collection.find(kwargs)