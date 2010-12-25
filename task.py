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

