from __future__ import division
import sys
import glob
import numpy as np
import matplotlib.pyplot as plt
import re
from string import punctuation
from operator import itemgetter

def sorted_nicely(l, key):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda item: [ convert(c) for c in re.split('([0-9]+)', key(item)) ]
    return sorted(l, key = alphanum_key)

def replace_word(infile,old_word,new_word):
    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)
    
divide_sum = 0
count = 0
next = None
average_list = []
finalList = []
files = glob.glob('data*')
for index, fn in enumerate(files):
    words = {}
    output_words, output_count = [], []
    eachList = []
    words_list = (word.strip(punctuation).lower() for line in open(fn) for word in line.split())
    eachList.append(fn)
    for word in words_list:
        words[word] = words.get(word, 0) + 1
    
    top_words = sorted(words.items(), key=itemgetter(1), reverse=True)
    for word, frequency in top_words:
        output_words.append("%s" % (word))
        output_count.append("%d" % (frequency))
    
    # Seach in output_words for words
    bad_words = ["bad", "mediocre",  "empty", "broken", "dissappoint", "dissappointed", "fail", "lacking", "shill", "shilling", "pass", "sucks", "stupid"]                                    #Define Bad Words
    good_words = ["good", "fun", "love", "enjoyable", "fantastic", "great", "great", "thrilling", "epic", "solid", "awesome", "having fun", "it's cool", "it's alright", "amazing", "spectacular"]        #Define Good Words
    value_listB, value_listG = [] , []
    for bad in bad_words:
        try:
            x = output_words.index(bad)
            value_listB.append(output_count[x])
        except:
            print bad + " not in words list"
            bad_words.remove(bad)
            pass
    if not bad_words:
        print " No bad words in words list"
        
    print "\n=======================    " + fn + "    =======================" 
    print "\nCount available bad words in words list " +  str(bad_words) + " = " + str(value_listB) +"\n"                    # Print list of number
    value_listB = map(int, value_listB)                                    # Convert list to integer list
    sum_bad = sum(value_listB)    
    eachList.append(sum_bad)                                        # Add numbers in list
    print "Total bad words in list = " + str(sum_bad)                    # Print total Bad Word
    
    for good in good_words:
        try:
            y = output_words.index(good)
            value_listG.append(output_count[y])
        except:
            print good + " not in words list"
            good_words.remove(good)
            pass
    if not good_words:
        print " No good words in words list"

    print "\nCount available good words in words list " +  str(good_words) + " = " + str(value_listG)+"\n"                    # Print list of number
    value_listG = map(int, value_listG)                                    # Convert list to integer list
    sum_good = sum(value_listG)    
    eachList.append(sum_good)                                        # Add numbers in list
    print "Total good words in list = " + str(sum_good)                    # Print total Good Words
    
    try:
        next = files[index + 1]
    except:
        print str(index) + " files have been processed"
        pass
    
    try:
        divide_sum = sum_bad / sum_good
    except ZeroDivisionError:
        pass
    
    average_list.append(divide_sum)
    finalList.append(eachList)
    
print "\n"
print finalList

with open("success_score.txt", 'w') as file:
    for item in average_list:
        file.write("{}\n".format(item))

with open("success_list.txt", 'w') as file:
    sort_finalList = sorted_nicely(finalList, itemgetter(0))
    for item in sort_finalList:
        file.write("{}\n".format(item))

replace_word("success_list.txt","["," ")
replace_word("success_list.txt","]"," ")
replace_word("success_list.txt","'"," ")
replace_word("success_list.txt"," ","")



