import redis
class RedisHandler:
    """
    client to handler redis operations

    """
    def __init__(self,host,port):
        self.client=redis.Redis(host=host,port=port)


    # implementing CRUD opetions
    def set(self,key,value):
        if self.client.exists(key):
            print("false",end='\n')
            return
        self.client.set(key,value)
        print("true",end="\n")

    def fetch(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass