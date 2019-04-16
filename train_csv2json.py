#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy
import os
import json
import pandas as pd
csvfile = '\\train.csv'
jsonfile = '\\train.json'


# In[2]:


import csv
csv=csv.reader(open(os.getcwd()+csvfile,'r',encoding="UTF-8"))
total_data=[]


# In[3]:


lines=[row for row in  csv]
nums=1
print("data Processing")
for line in lines:
    if line == ['Question', 'Abs', 'Answer']:
        continue
    if line == ['', '', '']:
        break
    
    question_id=line[0]
    passage=line[1]
    Answer=line[2]

    answer_start=passage.lower().find(Answer.lower())

    send_message={}
    send_message["title"]=passage.split('.')[0]

    paragraphs={}
    paragraphs["context"]=passage
    qas={}
    qas["answers"]=[{"answer_start":answer_start,"text":Answer}]
    qas["question"]=question_id
    qas["id"]=nums
    paragraphs["qas"]=[qas]


    send_message["paragraphs"]=[paragraphs]
    total_data.append(send_message)
    nums+=1

print("data finished")


# In[4]:


total_json={}
total_json["data"]=total_data
total_json["version"]="1.1"
print("total_json completed!")


# In[9]:


with open(os.getcwd()+jsonfile,'w',encoding="UTF-8") as json_file:
    json.dump(total_json,json_file,ensure_ascii=False)


# In[ ]:




