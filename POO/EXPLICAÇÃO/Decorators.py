#DECORATORS
##ÚTIL PARA QUE HAJA REAPROVEITAMENTO DE CÓDIGO


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('*You add sprinkles✨*')
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print('*You add fudge🍫*')
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f'Here is your {flavor} ice cream🍦')