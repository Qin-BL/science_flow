
def model_to_dict(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs).__dict__
        del res['_sa_instance_state']
        return res
    return wrapper


def model_to_list(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in range(len(res)):
            res[i] = res[i].__dict__
            del res[i]['_sa_instance_state']
        return res
    return wrapper
