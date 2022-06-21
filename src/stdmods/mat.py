def approx_pi():
    rank = 10
    return 4 * sum(-float(k%4 - 2) / k for k in range(1, 2*rank+1, 2))

vars = {
        'pi':approx_pi()
    }

def add(a, b):
    return int(a)+int(b)

def subs(a, b):
    return int(b)-int(a)

def mul(a, b):
    return int(b)*int(a)

def div(a, b):
    return int(a)/int(b)


def sqrt(x):
    return int(x)**0.5

def root(x, y):
    return int(x)**(1/int(y))

funcs = {
        'add':add,
        'sub':subs,
        'mul':mul,
        'div':div,

        'sqrt':sqrt,
        'root':root
    }
