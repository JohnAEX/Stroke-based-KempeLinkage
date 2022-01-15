# THIS FILE WAS USED FOR TESTING SOLVESPACE API CONVERSION

from python_solvespace import SolverSystem, ResultFlag
import pickle

sys = SolverSystem()
wp = sys.create_2d_base()  # Workplane
p0 = sys.add_point_2d(0, 0, wp)
sys.dragged(p0, wp)
p1 = sys.add_point_2d(1, 1, wp)
line0 = sys.add_line_2d(p0, p1, wp)

f = open("test_file.slvs", "w")
# f.write(pickle.dumps(sys))
sys_dump = pickle.dumps(sys)
f.write(sys_dump.decode("utf-8"))
f.close()



