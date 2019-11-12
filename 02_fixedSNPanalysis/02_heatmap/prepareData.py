#!/usr/bin/env python3
f_in = open("distance.matrix.txt")
f_out = open("distance.ggplot2.txt", "w")
clock = 0
for line in f_in.readlines():
	clock += 1
	if clock > 1:
		columns = line.split()
		if clock < 11:
			for j in range(1,25):
				f_out.write("M_0{}".format(clock - 1))
			
				if j < 10:
					f_out.write("\tM_0{}".format(j))
				else:
					f_out.write("\tM_{}".format(j))
				diff = columns[j]
				f_out.write("\t{}\n".format(diff))
		else:
			
			for j in range(1,25):
				f_out.write("M_{}".format(clock - 1))
				if j < 10:
					f_out.write("\tM_0{}".format(j))
				else:
					f_out.write("\tM_{}".format(j))
				diff = columns[j]
				f_out.write("\t{}\n".format(diff))
f_in.close()
f_out.close()
