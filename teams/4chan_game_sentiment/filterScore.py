import numpy as np
import math
import glob

def replace_word(infile,old_word,new_word):
	f1=open(infile,'r').read()
	f2=open(infile,'w')
	m=f1.replace(old_word,new_word)
	f2.write(m)
	
def get_score(file):
	try:
		score_list = []
		inFile = open(file)
		for data in inFile:
			try:
				score = "".join(data[data.index("[")+1:data.index("]")])
				x = int(score)
				digits = int(math.log10(x))+1
				if x > 20 and x < 101 and digits < 4 and score_list == 0:
					score_list = np.array(float(x))
				elif x > 20 and x < 101 and digits < 4:
					score_list.append(float(x))
			except:
				pass
		try:
			if not score_list:
					print "No Scores Found in " + file
			else:
					average = np.average(score_list)
					print "File: " + file + " - Score Average = " + str(average)
					return average
		except Exception:
			print "File: "+np.NAN+" average = nan"
			pass
	except:
		print "File: "+file+" not Found"
		pass
	
def get_all_scores():
	average_list = []
	files = glob.glob('data*[0-9].txt')
	for index, fn in enumerate(files):
		try:
			x = get_score(fn)
			print x
			if average_list == 0:
				average_list = np.array([x])
			else:
				average_list.append([x])
			
			print "Average List = " + str(average_list)
			with open('4chandata.txt', 'w') as myFile:
				myFile.write(str(average_list))
				
			next = files[index + 1]
		except:
			pass

get_all_scores()
replace_word('4chandata.txt', '], [','\n')
replace_word('4chandata.txt', '[','')
replace_word('4chandata.txt', ']','')      
replace_word('4chandata.txt', ',','')
