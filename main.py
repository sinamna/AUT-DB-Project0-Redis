from RedisHandler import RedisHandler
import redis
import csv
def loadCSV(redisHandler):
    with open("NYSE_20210301.csv") as csv_file:
        rows=csv.reader(csv_file,delimiter=",")
        for row in rows:
            redisHandler.set(row[0],row[1])

if __name__ == '__main__':
    redisClient = redis.Redis(host='localhost',port=6379)
    handler = RedisHandler(redisClient)
    loadCSV(handler)

