# Python try/catch exception handling

def function1():
    try:
        1/0
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))

# test
function1()
