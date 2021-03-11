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
    while True:
        operation = input()
        operation_list= operation.split(" ")
        operator=operation_list[0]
        if operator == "create":
            handler.set(operation_list[1],operation_list[2])
        elif operator == "fetch":
            handler.fetch(operation_list[1])
        elif operator == "update":
            handler.update(operation_list[1],operation_list[2])
        elif operator == "delete":
            handler.delete(operation_list[1])
        else:
            print("you have entered wrong operator")
        print()
