from pake import config
from pake import task
from pake.compiler import cc

config.file = __file__
objs = cc.compile() # the arguments files/dirs

@task('main', objs)
def main(target, depends):
	print(target)
	print(depends)

if __name__ == '__main__':
	main()
