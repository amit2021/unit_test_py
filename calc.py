def add(x,y):
    """Add function"""
    return x+y

def subtract(x,y):
    """subtract method"""
    return x-y

def multiplication(x,y):
    """mulriplication method"""
    return x*y

def divide(x,y):
    """division method"""
    if y==0:
        raise ValueError('cannot divide by zero')
    else:
        return x/y


if __name__=='__main__':
    print('starting from here')

print('now')
print(add(10,5))
