# AN EXAMPLE FILE GENERATED OUT OF PYSLVS - JUST USED FOR ANALYZING, WILL NOT RUN

# Generate by Pyslvs 21.12.0
# Project "Crank lifter"

from pyslvs import parse_vpoints, t_config, expr_solving

if __name__ == '__main__':
    # todo: do we want to create mechanism points like this? guess we can just create VPoint objects? --> see testing.py
    vpoints = parse_vpoints(
        "M["
        "J[R, color[Green], P[-67.38, 36.13], L[ground, L1]], "
        "J[R, color[Green], P[-68.925, 55.925], L[L1, L2]], "
        "J[RP, A[0.0], color[Green], P[11.88, 0], L[ground, L2, L3]], "
        "J[R, color[Green], P[50.775, 24.7908], L[L3, L4]], "
        "J[R, color[Green], P[80.375, 8.625], L[ground, L4]], "
        "J[R, color[Green], P[109.1972, 63.8805], L[L3, L5]], "
        "J[RP, A[0.0], color[Green], P[0.82, 64.42], L[L5, L4]], "
        "]")
    exprs = t_config(vpoints, ((0, 1),))
    print(vpoints)
    print(exprs)
    print("Copeium")
    print(vpoints[1].expr())
    mapping = {n: f'P{n}' for n in range(len(vpoints))}
    pos = expr_solving(exprs, vpoints, {(0, 1): 0.0})
    print(data_dict)
    print(pos)



###

from pyslvs import pla, plap, pllp, plpp

# a0, i0, l0, l1, l2, l3, l4, l5, l6, p0, p4 are known

if __name__ == '__main__':
    p1 = pla(p0, l0, i0)
    s2 = pllp(p0, l1, l2, p2)
    p2 = plpp(p1, l3, p2, s2)
    p3 = pllp(p2, l4, l5, p4)
    p5 = plap(p2, l6, a0, p3)