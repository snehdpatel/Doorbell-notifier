import subprocess

subprocess.call("python readmail.py &", shell=True)

while True:
	range_ret = subprocess.call("python New.py &", shell=True)
	subprocess.call("python image.py", shell=True)
	subprocess.call("python sendmail.py", shell=True)