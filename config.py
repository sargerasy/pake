import os
from pake import ConfigError
import pake

class Config(object):
	def getcwd(self):
		if getattr(self, 'file', None):
			return os.path.abspath(os.path.dirname(self.file))
		else:
			raise ConfigError("You must set config.file in pakefile.py")

config = Config()
