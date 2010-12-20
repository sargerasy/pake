import os
import subprocess
from pake import log

def convert_mbcs(s):
	dec = getattr(s, "decode", None)
	if dec is not None:
		try:
			s = dec("mbcs")
		except UnicodeError:
			pass
	return s

def remove_duplicates(var):
	oldList = var.split(os.pathsep)
	newList = []
	for i in oldList:
		if i not in newList:
			newList.append(i)
	return os.pathsep.join(newList)

def find_vcvarsall(version=9.0, arch="x86"):
	vcvarsall = None
	toolskey = "VS%0.f0COMNTOOLS" % version
	toolsdir = os.environ.get(toolskey, None)
	log.debug(toolsdir)
	if toolsdir and os.path.isdir(toolsdir):
		vcvarsall = os.path.join(toolsdir, "vcvarsall.bat")
	else:
		log.debug("Env var %s is not set or invalid" % toolskey)
		return None

	if vcvarsall and os.path.isfile(vcvarsall):
		return vcvarsall
	log.debug("Unable to find vcvarsall.bat")


if '__main__' == __name__:
	log.set_threshold(log.DEBUG)
	print(find_vcvarsall())

