import os

name = os.environ["NAME"]
files = list(filter(lambda x: x[-4:]==".cpp" or x[-2:] == ".c", os.listdir()))

env = Environment(ENV = os.environ.copy(), CXXFLAGS = ["-std=c++20"], LINKFLAGS = os.environ["LINKFLAGS"])
#program = env.Program(name, files, CPPPATH = ["include"], LIBPATH = ["lib"])
program = env.SharedLibrary(name, files, CPPPATH = ["include"], LIBPATH = ["lib"])
env.NoClean(program)
