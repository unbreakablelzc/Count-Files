#Count image folders in each folders
import os
import sys

def count_images(path):
	count = 0
	for lists in os.listdir(path):
		count += 1
		current_path = os.path.join(path, lists)
		if os.path.isdir(current_path):
			count_images(current_path)
	tmp_count = count - 1
	a,b = os.path.split(current_path)
	os.chdir(a)
	f = open("readme.txt", "w")
	print >> f, tmp_count
	
if __name__ == "__main__":
	path = sys.argv[1]
	count_images(path)