import os
from distutils import ccompiler as cc

def compile(*args):
	if len(args) == 0:
		dirs = [os.getcwd()]

def compile_c(srcs):
	from distutils import ccompiler as c
	compiler = c.new_compiler()
	objs = compiler.compile(srcs)
	compiler.link_executable(objs, 'main')
#TODO: generate setup file
#TODO: cmd like "pake cc hello.c"
#TODO: package, dist, xxx

def get_obj_name(compiler, cfile):
	return os.path.basename(cfile) + compile.obj_extension

def compile_c(cfile, depends, force):
	compiler = cc.new_compiler()
	ofile = get_obj_name(compiler, cfile)


