
import redis
from settings import DEFAULT_REDIS


def gen_redis_client(conf=DEFAULT_REDIS):
    conf.update({"decode_responses": True})
    return redis.StrictRedis(**conf)


rs = gen_redis_client()
