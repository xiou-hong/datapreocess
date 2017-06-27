import re 




def filter(filename,outfilename):
	output = ""
	outfile = open(outfilename,"w")
	pattern = u"[\u4e00-\u9fa5a-zA-Z1-9\t\n]+"
	
	with open(filename,"r") as file:
		file = re.findall(pattern,file.read())
		file = "".join(file)
		outfile.write(file)
	
	outfile.close()



