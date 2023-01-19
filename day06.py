class OopsException(Exception):
    pass

test = ['a','b','c','d']
value = 1

try:
    if len(test) > value:
        raise OopsException
    else:
        print('ssss')
except OopsException:
    print('Caught an oops')

