import numpy as np
from geno import minimize

"""
Sample for constrained problem
"""


def fg(x):
    f = (x[0] - 1)**2 + 2 * (x[1] - 2)**2
    g = np.array([2 * (x[0] - 1), 4 * (x[1] - 2)])
    return f, g


def c(x):
  return np.array([x[0] + 4 * x[1]])


def cjprod(x, v):
    return np.array([1, 4]) * v


x0 = np.array([0, 0])
# y0 is optional
y0 = 0
bounds = None

cl = 3
cu = 3
constraints = {'type': 'bnds',
               'fun': c,
               'jacprod': cjprod,
               'cl': cl,
               'cu': cu}

tol = 1E-8
# any option is optionable
options = {'maxiter': 50,
           'constraintsTol': 1E-5,
           'disp': False,
           'debug_fg': False,
           'debug_c': False,
           'debug_cjprod': False}

#constraints = []
result = minimize(fg, x0, y0, bounds=bounds, tol=tol,
                  constraints=constraints, options=options)
print(result)
