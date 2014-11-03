#/usr/bin/env python
##########################################################################
# Write a program in [ruby, lua, python] (ada.ius.edu) that will implement a usage message and interrogate the command line.
#
# C:\ruby fred.rb
#
# fred::usage::
#
# fred [ -debug | -java | -ada | -report | -o out_dir | -l lib_dir ] filename
#
# fred is a wonderful program
#
# -d = debug
#
# -j = java
#
# -a = ada
#
# -r = report
#
# -p = print
#
# -l = library directory
#
# -o = output directory
##########################################################################
# If no parameters, print usage statement
# Any parameter can be abbreviated to the first letter, i.e. -r == -report.
# Some of the parameters are singletons.
# Some of the parameters are part of a pair.
# X Any errors to be reported to the CRT.
# Should print a report summarizing
# Verify that the two parameters that are directories do actually exist
##########################################################################

import os, sys, getopt

def usage():
	print("fred [ -debug | -java | -ada | -report | -o out_dir | -l lib_dir ] filename")
	print("fred is a wonderful program")
	print("-d = debug")
	print("-j = java")
	print("-a = ada")
	print("-r = report")
	print("-p = print")
	print("-l = library directory")
	print("-o = output directory")

def debug_mode():
	print("Debug parameter found")

def java_mode():
	print("Java parameter found.")

def ada_mode():
	print("Ada parameter found.")

def report():
	print("Report would be printed.")

def print_mode():
	print("Print parameter detected.")

def check_dir(path):
	if not os.path.isdir(path):
		print_error(path + " does not exist.")
		return False
	else:
		return True

def lib_dir(path):
	if check_dir(path):
		print("[" + path + "] was passed as the lib_dir")

def out_dir(path):
	if check_dir(path):
		print("[" + path + "] was passed as the out_dir")

def print_error(err):
	print("[ERR] An error has occurred:\n\t" + err + "\n")

def main(argv):
	if len(argv) == 0:
		usage()
	else:
		try:
			opts, args = getopt.getopt(argv,"djarpl:o:",["l=","o="])
		except getopt.GetoptError:
			usage()
			sys.exit(-1)

		for opt, arg in opts:
			if opt == "-d":
				debug_mode()
			if opt == "-j":
				java_mode()
			if opt == "-a":
				ada_mode()
			if opt == "-p":
				print_mode()
			if opt == "-r":
				report()
			if opt in ("-l"):
				lib_dir(arg)
			if opt in ("-o"):
				out_dir(arg)

		inputfile = argv[-1]
		print("Input file entered: \"" + inputfile + "\"")

if __name__ == "__main__":
	main(sys.argv[1:])
