import redis
class RedisHandler:
    """
    client to handler redis operations

    """
    def __init__(self, redisClient):
        self.client=redisClient

    # implementing CRUD opetions
    def set(self,key,value):
        if self.client.exists(key):
            print("false",end='\n')
            return
        self.client.set(key,value)
        print("true",end="\n")

    def fetch(self,key):
        if not self.client.exists(key):
            print("false", end='\n')
            return
        value = self.client.get(key).decode("utf-8")
        print("true", end='\n')
        print(value)

    def update(self,key,val):
        if self.client.exists(key):
            self.client.set(key,val)
            print("true",end="\n")
            return
        print("false",end="\n")
    def delete(self,key):
        if self.client.exists(key):
            self.client.delete(key)
            print("true",end="\n")
            return
        print("false", end="\n")

