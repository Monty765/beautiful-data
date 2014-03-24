import sys
import matplotlib.mlab as mlab
import numpy as np
import numpy as numpy
import argparse
import scipy
import pylab as plt
from collections import defaultdict
from country import  fun
import collections
totalArry=[]
def readData(year,country):
    datArray=[]
    row = 0 
    col = 0
    f = open(''+year+'.csv')
    lines = f.readlines()
    f.close()
    for line in lines:
        ta = line.rstrip().split('\n')
        datArray.extend(ta)
        row += 1
        col = len(ta)
    rown=fun(country)
    row= datArray[rown]
    array3=[]
    array3=row.split(',')
    totalArry.append(array3[1])
    return array3
upCount=0
downCount=0
f = open('1999.csv')
lines = f.readlines()
f.close()
for line in lines:
        ta = line.rstrip().split(',')
        print ta[0]
con = raw_input('Choose a Country')
year1=readData("1998","1")
i=0;
for title in year1:
    print i,title
    i=i+1
coef =int(raw_input('Choose a the Analysis Factor'))


def mean(numberList):
    if len(numberList) == 0:
        return float('nan')
    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)
def percentage(avg,a):
    variance=0;
    upr=10
    for data in a:
        
        variance= (float(data)-avg)
        print variance
        if(variance==0):
            print"Does not Apply"
        if(variance<0):
            print "down"
        else:
            print "up"
year1=readData("1995",""+con+"")
year2=readData("1996",""+con+"")
year3=readData("1998",""+con+"")
year4=readData("1999",""+con+"")
year5=readData("2000",""+con+"")
year6=readData("2001",""+con+"")
year7=readData("2002",""+con+"")
year8=readData("2003",""+con+"")
year9=readData("2004",""+con+"")
year10=readData("2005",""+con+"")
a = [float(year1[coef]), float(year2[coef]),float(year3[coef]),float(year4[coef]),float(year5[coef]),float(year6[coef]),float(year7[coef]),float(year8[coef]),float(year9[coef]),float(year10[coef])]
i=5
total=0.0
datu=[]
print"From 1995-2001"
for info in a:
    print info,"Millions US Dollar"
    total=total+(float(info))
    datu.append(float(info))
    i=i+1
average=(total/len(a))
print "average",average
stDev=(numpy.sqrt(numpy.var(datu)))
print "1 Bars"
print "2 Histogram"
type = raw_input('Choose a PLotting Type')
# if(type==1):
label = ('1995', '1996', '1998', '1999', '2000','2001','2002','2003','2004','2005')
y_pos = np.arange(len(label))
performance = a
error = np.random.rand(len(label))
plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.6)
plt.yticks(y_pos, label)
plt.xlabel('Millions US Dollar')
plt.ylabel('Year')
year1=readData("1998","1")
plt.title("year1[coef]")
plt.show()
     

from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
x =np.arange(10)
money = a
fig, ax = plt.subplots()
plt.bar(x, money)
plt.xticks( x + 0.3,  ('1995', '1996', '1998', '1999', '2000','2001','2002','2003','2004','2005'))
plt.show()














