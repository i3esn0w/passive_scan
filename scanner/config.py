# coding:utf8
__author__ = 'hartnett'

# mongodb 配置项
db_info = dict(
    host="192.243.116.148",
    port=27017,
    username="",
    password=""
)

CONST_WHITE_DOMAINS = ['weibo.com', 'sina.com.cn', 'google.com', 'baidu.com', 'cnzz.com']

CONST_REDIS = {
    'host' : '192.243.116.148:6379',
    'port' : 6379,
    'db' : 1,
    'password' : ''
}

REDIS_SERVER = "redis://:%s@%s:%d/%d" % (
    CONST_REDIS.get('password'),
    CONST_REDIS.get('host'),
    CONST_REDIS.get('port'),
    CONST_REDIS.get('db')
)

BROKER_URL = REDIS_SERVER
BACKEND_URL = REDIS_SERVER
