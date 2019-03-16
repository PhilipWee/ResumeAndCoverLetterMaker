from math import sqrt
import numpy as np
from decimal import Decimal
import scipy.constants as scipy

n = 1680
p = 680
x = 252*10**3/scipy.Avogadro
x = scipy.h*scipy.c/x

print('{:.4E}'.format(Decimal(x)))