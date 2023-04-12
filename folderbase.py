import os
def write(name, data):
	f = open(f"{os. getcwd()}/folderbase/{name}", 'w')
	f.write(data)
	f.close()
def ishere(name):
	return os.path.exists(f"{os. getcwd()}/folderbase/{name}")
def read(name):
	if ishere(name):
		f = open(f"{os. getcwd()}/folderbase/{name}", 'r')
		r = f.read()
		f.close()
		return r
	else:
		return False
def delete(name):
	os.remove(f"{os. getcwd()}/folderbase/{name}")
