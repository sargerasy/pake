import os
from distutils import ccompiler as cc

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


class Task(object):
	def __init__(self, target, depends):
		self.target = target
		self.depends = depends

	def __call__(self, func):
		def _task():
			func(self.target, self.depends)
		return _task

def task(target, depends):
	return Task(target, depends)

@task("main", ["main.c", "hello.c"])
def compile(target, depends):
	print(target, depends)

if '__main__' == __name__:
	compile()
#	from distutils import log
#	log.set_verbosity(1)
#	compile_c(["main.c", "hello.c"])

