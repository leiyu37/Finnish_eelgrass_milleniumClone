#!/usr/bin/env python3
#01 combine the information from all three modules to "01_formatFreqChange.txt".
f_in = open("05_s8x_DPaAF.txt")
f_out = open("01_formatFreqChange.txt", "w")
for line in f_in.readlines():
	columns = line.split()
	if not line.startswith("LFYR"):
		f_out.write("SNP\t{}\t{}\tModule\n".format(columns[2],columns[3]))
	else:
		f_out.write("{}_{}\t{}\t{}\tM_08\n".format(columns[0],columns[1],columns[2],columns[3]))
f_in.close()

f_in = open("05_s10x_DPaAF.txt")
for line in f_in.readlines():
	columns = line.split()
	if line.startswith("LFYR"):
		f_out.write("{}_{}\t{}\t{}\tM_10\n".format(columns[0],columns[1],columns[2],columns[3]))
f_in.close()

f_in = open("05_s12x_DPaAF.txt")
for line in f_in.readlines():
	columns = line.split()
	if line.startswith("LFYR"):
		f_out.write("{}_{}\t{}\t{}\tM_12\n".format(columns[0],columns[1],columns[2],columns[3]))
f_in.close()
f_out.close()

#02 separate the data to different categories.
f_in = open("01_formatFreqChange.txt")
snp_dict = {}
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		snp = columns[0]
		if snp in snp_dict.keys():
			snp_dict[snp].append(columns[3])
		else:
			snp_dict[snp] = []
			snp_dict[snp].append(columns[3])
f_in.close()

f_8 = open("02_A_08_FreqChange.txt", "w") # present in only module 8
f_10 = open("02_A_10_FreqChange.txt", "w") # present in only module 10
f_12 = open("02_A_12_FreqChange.txt", "w") # present in only module 12
f_810 = open("02_B_08_10_FreqChange.txt", "w") # present in module 8 and module 10
f_812 = open("02_B_08_12_FreqChange.txt", "w") # present in module 8 and module 12
f_1012 = open("02_B_10_12_FreqChange.txt", "w") # present in module 10 and module 12
f_t = open("02_C_08_10_12_FreqChange.txt", "w") # present in module 8, module 10, and module 12

for snp in snp_dict.keys():
	if ("M_08" in snp_dict[snp]) and (not "M_10" in snp_dict[snp]) and (not "M_12" in snp_dict[snp]):
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				f_8.write(line)
				break
		f_in.close()

	elif (not "M_08" in snp_dict[snp]) and ("M_10" in snp_dict[snp]) and (not "M_12" in snp_dict[snp]):
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				f_10.write(line)
				break
		f_in.close()

	elif (not "M_08" in snp_dict[snp]) and (not "M_10" in snp_dict[snp]) and ("M_12" in snp_dict[snp]):
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				f_12.write(line)
				break
		f_in.close()

	elif ("M_08" in snp_dict[snp]) and ("M_10" in snp_dict[snp]) and (not "M_12" in snp_dict[snp]):
		i = 0
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				i += 1
				f_810.write(line)
				if i == 2:
					break
		f_in.close()

	elif ("M_08" in snp_dict[snp]) and (not "M_10" in snp_dict[snp]) and ("M_12" in snp_dict[snp]):
		i = 0
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				i += 1
				f_812.write(line)
				if i == 2:
					break
		f_in.close()

	elif (not "M_08" in snp_dict[snp]) and ("M_10" in snp_dict[snp]) and ("M_12" in snp_dict[snp]):
		i = 0
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				i += 1
				f_1012.write(line)
				if i == 2:
					break
		f_in.close()

	elif ("M_08" in snp_dict[snp]) and ("M_10" in snp_dict[snp]) and ("M_12" in snp_dict[snp]):
		i = 0
		f_in = open("01_formatFreqChange.txt")
		for line in f_in.readlines():
			columns = line.split()
			if columns[0] == snp:
				i += 1
				f_t.write(line)
				if i == 3:
					break
		f_in.close()

f_8.close()
f_10.close()
f_12.close()
f_810.close()
f_812.close()
f_1012.close()
f_t.close()

#03 format "02_B_08_10_FreqChange.txt" to ggplot2 format.
f_in = open("02_B_08_10_FreqChange.txt")
snp_dict = {}
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		snp = columns[0]
		if snp in snp_dict.keys():
			snp_dict[snp].append(columns[3])
		else:
			snp_dict[snp] = []
			snp_dict[snp].append(columns[3])
f_in.close()

f_out = open("03_B_08_10_ggplot2_FreqChange.txt", "w")
f_out.write("SNP\tDP08\tVRF08\tDP10\tVRF10\n")

for pos in snp_dict.keys():
	f_out.write("{}".format(pos))
	f_in = open("02_B_08_10_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_08":
			f_out.write("\t{}\t{}".format(columns[1], columns[2]))
			break
	f_in.close()

	f_in = open("02_B_08_10_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_10":
			f_out.write("\t{}\t{}\n".format(columns[1], columns[2]))
			break
	f_in.close()
f_out.close()

#04 format "02_B_08_12_FreqChange.txt" to ggplot2 format.
f_in = open("02_B_08_12_FreqChange.txt")
snp_dict = {}
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		snp = columns[0]
		if snp in snp_dict.keys():
			snp_dict[snp].append(columns[3])
		else:
			snp_dict[snp] = []
			snp_dict[snp].append(columns[3])
f_in.close()

f_out = open("03_B_08_12_ggplot2_FreqChange.txt", "w")
f_out.write("SNP\tDP08\tVRF08\tDP12\tVRF12\n")

for pos in snp_dict.keys():
	f_out.write("{}".format(pos))
	f_in = open("02_B_08_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_08":
			f_out.write("\t{}\t{}".format(columns[1],columns[2]))
			break
	f_in.close()

	f_in = open("02_B_08_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_12":
			f_out.write("\t{}\t{}\n".format(columns[1], columns[2]))
			break
	f_in.close()
f_out.close()

#05 format "02_B_10_12_FreqChange.txt" to ggplot2 format.
f_in = open("02_B_10_12_FreqChange.txt")
snp_dict = {}
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		snp = columns[0]
		if snp in snp_dict.keys():
			snp_dict[snp].append(columns[3])
		else:
			snp_dict[snp] = []
			snp_dict[snp].append(columns[3])
f_in.close()

f_out = open("03_B_10_12_ggplot2_FreqChange.txt", "w")
f_out.write("SNP\tDP10\tVRF10\tDP12\tVRF12\n")

for pos in snp_dict.keys():
	f_out.write("{}".format(pos))
	f_in = open("02_B_10_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_10":
			f_out.write("\t{}\t{}".format(columns[1], columns[2]))
			break
	f_in.close()

	f_in = open("02_B_10_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_12":
			f_out.write("\t{}\t{}\n".format(columns[1], columns[2]))
			break
	f_in.close()
f_out.close()


#03 format "02_C_08_10_12_FreqChange.txt" to ggplot2 format.
f_in = open("02_C_08_10_12_FreqChange.txt")
snp_dict = {}
for line in f_in.readlines():
	if line.startswith("LFYR"):
		columns = line.split()
		snp = columns[0]
		if snp in snp_dict.keys():
			snp_dict[snp].append(columns[3])
		else:
			snp_dict[snp] = []
			snp_dict[snp].append(columns[3])
f_in.close()

f_out = open("03_C_08_10_12_ggplot2_FreqChange.txt", "w")
f_out.write("SNP\tDP08\tVRF08\tDP10\tVRF10\tDP12\tVRF12\n")

for pos in snp_dict.keys():
	f_out.write("{}".format(pos))
	f_in = open("02_C_08_10_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_08":
			f_out.write("\t{}\t{}".format(columns[1], columns[2]))
			break
	f_in.close()
	f_in = open("02_C_08_10_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_10":
			f_out.write("\t{}\t{}".format(columns[1], columns[2]))
			break
	f_in.close()
	f_in = open("02_C_08_10_12_FreqChange.txt")
	for line in f_in.readlines():
		columns = line.split()
		if pos == columns[0] and columns[3] == "M_12":
			f_out.write("\t{}\t{}\n".format(columns[1], columns[2]))
			break
	f_in.close()
f_out.close()
