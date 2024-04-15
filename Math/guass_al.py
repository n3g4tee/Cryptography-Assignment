from math import floor
class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def mul(u, v):
        r = u.x * v.x + u.y * v.y
        return r
def multiple(k, a):
        x = k * a.x
        y = k * a.y
        u = vec(x, y)
        return u
def sub(u, v):
        x = u.x- v.x
        y = u.y- v.y
        r = vec(x, y)
        return r
def Gaussia(v, u):
        while True:
            if mul(u, u) < mul(v, v): u,v=v,u
            m = floor(mul(v, u) / mul(v, v))
            if m == 0: break
            else:
                u = sub(u, multiple(m, v))
            return (v, u)
v = vec(846835985, 9834798552)
u = vec(87502093, 123094980)
v, u = Gaussia(v, u)
print(mul(v, u))