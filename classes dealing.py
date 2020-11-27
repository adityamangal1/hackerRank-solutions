import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        complex_n = complex(self.real, self.imaginary) + \
            complex(no.real, no.imaginary)
        return Complex(complex_n.real, complex_n.imag)

    def __sub__(self, no):
        complex_n = complex(self.real, self.imaginary) - \
            complex(no.real, no.imaginary)
        return Complex(complex_n.real, complex_n.imag)

    def __mul__(self, no):
        complex_n = complex(self.real, self.imaginary) * \
            complex(no.real, no.imaginary)
        return Complex(complex_n.real, complex_n.imag)

    def __truediv__(self, no):
        factor = no.real ** 2 + no.imaginary ** 2

        return Complex((self.real * no.real + self.imaginary * no.imaginary) / factor,                          (self.imaginary * no.real - self.real * no.imaginary) / factor)

    def mod(self):

        return Complex((self.real ** 2 + self.imaginary ** 2) ** (1 / 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
