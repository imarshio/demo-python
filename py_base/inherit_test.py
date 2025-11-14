class A:
    def __init__(self, a,b,c: int = 0):
        pass
    def method_a(self, a, b,c :int = 0):
        pass



class B(A):
    def __init__(self, a,b,d,c: int = 0,f: int = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.f = f
    def method_a(self, a, b, d, c :int = 0, f: int = 0):
        print(a,b,d,c,f)


if __name__ == '__main__':
    b = B(1,2,3,4,5)
    b.method_a(1,2,3,4,5)