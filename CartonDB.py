import pickle
import threading

class StoredData:
    def __init__(self,path):
        self.path=path
    def save(self,data):
        self.writeObject=open(self.path,"wb")
        pickle.dump(data,self.writeObject)
    def get(self):
        try:
            self.readObject=open(self.path,"rb")
            data=pickle.load(self.readObject)
        except FileNotFoundError:
            data={}
        return data

class Carton:
    def __init__(self,path):
        self.store=StoredData(path)    
        self.data=self.store.get()
        self.lock = threading.Lock()
    def add(self,key,inputData):
        with self.lock:
            self.data[key]=inputData
    def get(self,key):
        return self.data.get(key)
    def delete(self,key):
        try:
            del self.data[key]
            return key+"deleted"
        except KeyError:
            return key+"does not exist"
    def save(self):
        with self.lock:
            self.store.save(self.data)