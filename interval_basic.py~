#--encoding:utf-8

# A idéia aqui vai ser criar uma classe que represente intervalos fechados simples.
# Depois, criar outra classe que represente uniões de intervalos fechados simples, usando a classe acima

# Para usar na segunda classe:
#    """ input: an iterable of pairs of floats
#        output: an object "interv" that represents an union of closed intervals, one interval for each pair of #floats, using them as extremes """

import struct
from fpu import up, down

class Interv_single:
    _N_ = {"N0", "N1"}
    _P_ = {"P0", "P1"}
    def classify(self): # Doesn't return anything, just changes the interv_class parameter.
        self.interv_class = ""
        inf = self.inf
        sup = self.sup
        if inf == float("nan"):
            self.interv_class = "E" # empty
        if inf < 0:
            if sup > 0:
                self.interv_class = "M"
            elif sup == 0:
                self.interv_class = "N0"
            else:
                self.interv_class = "N1"
        elif inf == 0:
            if sup > 0:
                self.interv_class = "P0"
            else: # Notice that it's impossible that sup < 0, because sup > inf
                self.interv_class = "Z"
        else: #inf > 0
            self.interv_class = "P1"

    def __init__(self, a,b):     
        """ input: a pair of floats (x,y)
        output: an object "interv" that represents the closed interval [min(x,y),max(x,y)]"""
        if a == float("nan") or b == float("nan"):
            self.inf = float("nan")
            self.sup = float("nan")
            self.midpoint = float("nan")
        else:
            inf = float(min(a,b))
            sup = float(max(a,b))
            self.inf = inf
            self.sup = sup
            self.midpoint = (inf+sup)/2
        Interv_single.classify(self)
        
    def __repr__(self):
        return "<%s,%s>" % (self.inf, self.sup)

    def __add__(self,other):
        return Interv_single(down(lambda: self.inf + other.inf), up(lambda:(self.sup + other.sup)))
    def __sub__(self,other):
        return Interv_single(down(lambda: self.inf - other.inf), up(lambda: (self.sup - other.sup)))
    def __mul__(self,other):
        inf = 0
        sup = 0
        c1 = self.interv_class
        c2 = other.interv_class
        if c1 == "E" or c2 == "E":
            inf = float("nan")
            sup = float("nan")
        elif c1 == 'Z' or c2 == 'Z':
            inf = 0
            sup = 0
        elif c1 in P:
            if c2 in P:
                inf = down(lambda: self.inf * other.inf)
                sup = up(lambda: self.sup * other.sup)
            elif c2 == 'M':
                inf = down(lambda: self.sup * other.inf)
                sup = up(lambda: self.sup * other.sup)
            else: #c2 in N:
                inf = down(lambda: self.sup * other.inf)
                sup = up(lambda: self.inf * other.sup)
        elif c1 == 'M':
            if c2 in P:
                inf = down(lambda: self.inf * other.sup)
                sup = up(lambda: self.sup * other.sup)
            elif c2 == 'M':
                inf = min(down(lambda: self.inf * other.sup), down(lambda: self.sup * other.inf))
                sup = max(up(lambda: self.sup * other.sup), up(lambda: self.inf * other.inf))
            else: #c2 in N
                inf = down(lambda: self.sup * other.inf)
                sup = up(lambda: self.inf * other.inf)
        else: #c1 in N
            if c2 in P:
                inf = down(lambda: self.inf * other.sup)
                sup = up(lambda: self.sup * other.inf)
            elif c2 == 'M':
                inf = down(lambda: self.inf * other.sup)
                sup = up(lambda: self.inf * other.inf)
            else: #c2 in N
                inf = down(lambda: self.sup * other.sup)
                sup = up(lambda: self.inf * other.inf)

        return Interv_single(inf,sup)
        
    def __div__(self,other):

        inf = 0
        sup = 0
        c1 = self.interv_class
        c2 = other.interv_class
        if c2 == "E" or c1 == "E":
            inf = float("nan")
            sup = float("nan")
        elif c2 == "Z":
            inf = float("nan")
            sup = float("nan")
        elif c1 == "Z":
            inf = 0
            sup = 0
        elif c2 == "P0":
            if c1 == "P1":
                inf = down(lambda: self.inf / other.sup)
                sup = float("+inf")
            elif c1 == "P0":
                inf = 0
                sup = float("+inf")
            elif c1 == "M":
                inf = float("-inf")
                sup = float("inf")
            elif c1 == "N0":
                inf = float("-inf")
                sup = 0
            else: #c1 == "N1":
                inf = float("-inf")
                sup = up(lambda: self.sup / other.sup)
        elif c2 == "P1":
            if c1 == "P1":
                inf = down(lambda: self.inf / other.sup)
                sup = up(lambda: self.sup / other.inf)
            elif c1 == "P0":
                inf = 0
                sup = up(lambda: self.sup / other.inf)
            elif c1 == "M":
                inf = down(lambda: self.inf / other.inf)
                sup = up(lambda: self.sup / other.inf)
            elif c1 == "N0":
                inf = down(lambda: self.inf / other.inf)
                sup = 0
            else: #c1 == "N1":
                inf = down(lambda: self.inf / other.inf)
                sup = up(lambda: self.sup / other.sup)
        elif c2 == "M":
            inf = float("-inf")
            sup = float("inf")
        elif c2 == "N0":
            if c1 == "P1":
                inf = float("-inf")
                sup = up(lambda: self.inf / other.inf)
            elif c1 == "P0":
                inf = float("-inf")
                sup = 0
            elif c1 == "M":
                inf = float("-inf")
                sup = float("inf")
            elif c1 == "N0":
                inf = 0
                sup = float("+inf")
            else: #c1 == "N1":
                inf = down(lambda: self.sup / other.inf)
                sup = float("+inf")
        elif c2 == "N1":
            if c1 == "P1":
                inf = down(lambda: self.sup / other.sup)
                sup = up(lambda: self.inf / other.inf)
            elif c1 == "P0":
                inf = down(lambda: self.sup / other.sup)
                sup = 0
            elif c1 == "M":
                inf = down(lambda: self.sup / other.sup)
                sup = up(lambda: self.inf / other.sup)
            elif c1 == "N0":
                inf = 0
                sup = up(lambda: self.inf / other.sup)
            else: #c1 == "N1":
                inf = down(lambda: self.sup / other.inf)
                sup = up(lambda: self.inf / other.sup)

        return Interv_single(inf,sup)      

    def __pow__(self,other):
        if self.interv_class == "M":
            if other%2 == 0:
                maximo = max(abs(self.inf),abs(self.sup))
                return Interv_single(0,maximo**other)
            else:
                return Interv_single(self.inf**other,self.sup**other)
        else:  # N, P, Z, E
            return Interv_single(self.inf**other,self.sup**other)

    def inters(self,other):
        """ Interval intersection""" 
        inf = max(self.inf, other.inf)
        sup = min(self.sup, other.sup)
        if inf > sup:
            inf = float("nan")
            sup = float("nan")
        return Interv_single(inf,sup)

    def newton(self,f,d,maxiter = 10000):
        # This is currently bugged!
        """ Input: a function f and its derivative d
            Output: a contracted interval where all the zeroes of f in I"""
        def passo(x, i):
            return i.inters(Interv_single(x,x) - (Interv_single(f(x),f(x)) / d(i)))
        def amostra(i):
            yield i.midpoint
            yield i.inf
            yield i.sup
        def iteracao(i):
            atual = i
            for n in xrange(maxiter):
                anterior = atual
                for valor in amostra(atual):
                    atual = passo(valor,atual)
                    print atual
                    if atual != anterior:
                        break
                else:
                    return atual
            return atual
        return iteracao(self)
    
def roda(k=10000):
    z = Interv_single(-100,100)
    f = lambda x: (x*x - 1)*(x-2) # input: float; output: float
    d = lambda x: Interv_single(3,3)*x*x - Interv_single(4,4)*x - Interv_single(1,1) # input: interval; output: interval
    print z.newton(f,d,k)

        
#---

# This isn't used in the code above. It's here just so that we can confirm the binary float form of each number

def binary(num):
    # Struct can provide us with the float packed into bytes. The '!' ensures that
    # it's in network byte order (big-endian) and the 'f' says that it should be
    # packed as a float. Alternatively, for double-precision, you could use 'd'.
    packed = struct.pack('!f', num)
    print 'Packed: %s' % repr(packed)

    # For each character in the returned string, we'll turn it into its corresponding
    # integer code point
    # 
    # [62, 163, 215, 10] = [ord(c) for c in '>\xa3\xd7\n']
    integers = [ord(c) for c in packed]
    print 'Integers: %s' % integers

    # For each integer, we'll convert it to its binary representation.
    binaries = [bin(i) for i in integers]
    print 'Binaries: %s' % binaries

    # Now strip off the '0b' from each of these
    stripped_binaries = [s.replace('0b', '') for s in binaries]
    print 'Stripped: %s' % stripped_binaries

    # Pad each byte's binary representation's with 0's to make sure it has all 8 bits:
    #
    # ['00111110', '10100011', '11010111', '00001010']
    padded = [s.rjust(8, '0') for s in stripped_binaries]
    print 'Padded: %s' % padded

    # At this point, we have each of the bytes for the network byte ordered float
    # in an array as binary strings. Now we just concatenate them to get the total
    # representation of the float:
    return ''.join(padded)
