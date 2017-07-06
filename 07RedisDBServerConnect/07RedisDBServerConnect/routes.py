from flask import Flask;
from app import app;
import redis;


@app.route('/')
def connectRedisDB():
    #windows for Redis Server download link  https://github.com/rgl/redis/downloads
    try:
        rConnection=redis.StrictRedis(host='localhost',port=6379,db=0); 
        #ALternative way to connect Redis, each command to equivalent connection below
        #r=redis.StrictRedis('localhost',6379,0);
        # #r=redis.StrictRedis();            
        return "Successfully Connect to RedisDB";

    except:
        return "Failed to connect to RediesDB";
