
# coding: utf-8

# In[6]:


import string
import csv
import json
import pickle
def main(filename):
    count=[]
    all_words=[]
    txt=open(filename)
    text=txt.readlines()
    for line in text:
        base=line.split()
        for word in base:
            for QQ in string.punctuation:
                while word.endswith(QQ) is True:
                    word=word[:-1]
                while word.startswith(QQ) is True:
                    word=word[1:]
                
            if word=="":
                pass
            else:
                all_words.append(word)
            
    from collections import Counter
    number = Counter(all_words)
    for key,value in number.items():
        count.append((key,value))
    with open('wordcount.csv','w', newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(count)
    with open('wordcount.json','w')as csv_file:
        json.dump(number,csv_file)
    with open('wordcount.pkl','wb')as csv_file:
        pickle.dump(number,csv_file)
if __name__ == '__main__':
    main("i_have_a_dream.txt")

