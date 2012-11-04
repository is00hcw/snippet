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
#x = plt.arange(100)
#plt.plot(10*plt.ones(100), x , 'ro', label = 'x = 10')
plt.show()
def fuc_purity():
	numerical_list = class_dict.keys()
	#categorical_list = class_dict.values()
	#比較每個點作為分割點的純度
	for split_point in numerical_list[1:]:
		#split_point 為分割點
		categorical_a = 0, categorical_b = 0, categorical_c = 0
		
	pass


