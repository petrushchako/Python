#help(print)

#help()
import sys

print("In the file")
prog = "SysTest.py"
src = "test.src"
dest = "desc.dest"

def show_config():
	print("Program:\t%s" %prog)
	print("Source:\t%s" %src)
	print("Destination\t%s" %dest)
	print("\n\n\n", sys.platform)
	

if __name__=="__main__":
	import sys
	print("This is sys.argv: \t%s" %sys.argv)
	if len(sys.argv) >2:
		prog, src, dest = sys.argv[:3]
	elif len(sys.argv) >1:
		prog, src = sys.argv[:2]
	else:
		prog = sys.argv[0]
	show_config()


