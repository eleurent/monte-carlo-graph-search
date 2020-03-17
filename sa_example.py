from sympy import symbols
from sympy import expand, factor, collect
from sympy.solvers import solve

g, r, s = symbols('g r s')
r1 = symbols('r1')
r2 = symbols('r2')
r3 = symbols('r3')
rh = symbols('rh')


def gap(n):
    return s * g**n / (1-g)


V_s = r / (1-g)
Rh = []
for h in range(10):
    rh_e = solve(sum(g**i * ri for i, ri in enumerate(Rh)) + g**h * rh + g**(h+1) * V_s - (V_s - gap(h+1)), rh)[0]
    Rh.append(rh_e)
    print(h, collect(rh_e, (r, g)))
