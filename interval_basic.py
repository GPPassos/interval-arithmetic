#--encoding:utf-8

# A idéia aqui vai ser criar uma classe que represente intervalos fechados simples.
# Depois, criar outra classe que represente uniões de intervalos fechados simples, usando a classe acima

# Para usar na segunda classe:
#    """ input: an iterable of pairs of floats
#        output: an object "interv" that represents an union of closed intervals, one interval for each pair of #floats, using them as extremes """

from fpu import up, down

class Interv_single:
    N = {"N0", "N1"}
    P = {"P0", "P1"}
    def classify(self): # Doesn't return anything, just changes the interv_class parameter.
        self.interv_class = ""
        l = 0
        r = 0
        # l: -1 if inf < 0, l = 0 if inf = 0, l = 1 if inf > 1; same for r
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
        inf = min(a,b)
        sup = max(a,b)
        self.inf = inf
        self.sup = sup
        classify(self)
        
    def __add__(self,other):
        return Interv_single(down(lambda: self.inf + other.inf), up(lambda:(self.sup + other.sup)))
    def __sub__(self,other):
        return Interv_single(down(lambda: self.inf - other.inf), up(lambda: (self.sup - other.sup)))
    def __mul__(self,other):
        prod = [self.inf * other.inf, self.inf * other.sup, self.sup * other.if, self.eup * other.sup]
        return Interv_single(m
        



---

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
