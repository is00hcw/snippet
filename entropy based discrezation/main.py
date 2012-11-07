import csv
import numpy as np
import matplotlib.pylab as plt

class_dict = {}
class_list = []
with open("data.txt", 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		class_dict[ int (row[4]) ] = int (row[5])
		#class_list.append( row[4] )


print class_dict.keys()
print "###########################"
print class_dict
plt.xlim(0, len(class_dict)+1)
plt.ylim(0,4)
#x = np.linspace(0, 15, len(class_list))
plt.plot(class_dict.keys(),class_dict.values(), "gp")
x = plt.arange(100)
##plt.plot(20*plt.ones(100), x , 'ro', label = 'x = 10')
plt.show()



