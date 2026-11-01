import sys, importlib.util
sys.path.insert(0, '/home/user/work/pipe'); import common
p = sys.argv[1]; spec = importlib.util.spec_from_file_location('plan', p); P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
common.build(P, P.W)
