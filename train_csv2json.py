#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy
import os
import json
import pandas as pd
csvfile = '\\train.csv'
jsonfile = '\\train-v1.1.json'


# In[2]:


import csv
reader=csv.reader(open(os.getcwd()+csvfile,'r',encoding="UTF-8"))
total_data=[]


# In[3]:

print('train-v1.1.json:')
lines=[row for row in  reader]
nums=1
print("data Processing")
for line in lines:
    if line == ['Question', 'Abs', 'Answer']:
        continue
    if line == ['', '', '']:
        break
    '''if nums==10:           ‘测试前十个数据点
        break '''
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

    if question_id=='A1':
        qas["question"]='What is the objective/aim of this paper?'
    elif question_id=='A2':
        qas["question"]='What problem(s) does this paper address?'
    elif question_id=='A41':
        qas["question"]='What method/approach does this paper propose?'
    elif question_id=='A51':
        qas["question"]='What is this method based on?'
    elif question_id=='A61':
        qas["question"]='How does the proposed method differ from previous methods/approaches?'
    elif question_id=='A42':
        qas["question"]='What model does this paper propose?'
    elif question_id=='A52':
        qas["question"]='What is this model based on?'
    elif question_id=='A62':
        qas["question"]='How does the proposed model differ from previous models?'
    elif question_id=='A43':
        qas["question"]='What algorithm does this paper propose?'
    elif question_id=='A53':
        qas["question"]='What is this algorithm based on?'
    elif question_id=='A63':
        qas["question"]='How does the proposed algorithm differ from previous algorithms?'
    elif question_id=='A44':
        qas["question"]='What framework does this paper propose?'
    elif question_id=='A54':
        qas["question"]='What is this framework based on?'
    elif question_id=='A64':
        qas["question"]='How does the proposed framework differ from previous frameworks?'
    elif question_id=='A45':
        qas["question"]='What datasetdoes this paper propose? '
    elif question_id=='A7':
        qas["question"]='What experiment does this paper carry out to evaluate the result?'
    elif question_id=='A81':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A82':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A83':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A10':
        qas["question"]='How does this result outperform existing work?'
    else:
        qas["question"]=question_id


    
    qas["id"]=str(nums)
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






# In[10]:

csvfile2 = '\\test.csv'
jsonfile2 = '\\dev-v1.1.json'

reader=csv.reader(open(os.getcwd()+csvfile2,'r',encoding="UTF-8"))
total_data=[]


# In[11]:

print('dev-v1.1.json:')
lines=[row for row in  reader]
print("data Processing")
for line in lines:
    if line == lines[0]:
        continue
    if line == ['', '', '']:
        break
    '''if nums==10:           ‘测试前十个数据点
        break '''
    question_id=line[1]
    passage=line[2]
    Answer=line[3]
    Answer2=line[4]

    answer_start=passage.lower().find(Answer.lower())
    answer_start2=passage.lower().find(Answer2.lower())

    send_message={}
    send_message["title"]=passage.split('.')[0]

    paragraphs={}
    paragraphs["context"]=passage
    qas={}
    qas["answers"]=[{"answer_start":answer_start,"text":Answer},{"answer_start":answer_start2,"text":Answer2}]


    if question_id=='A1':
        qas["question"]='What is the objective/aim of this paper?'
    elif question_id=='A2':
        qas["question"]='What problem(s) does this paper address?'
    elif question_id=='A41':
        qas["question"]='What method/approach does this paper propose?'
    elif question_id=='A51':
        qas["question"]='What is this method based on?'
    elif question_id=='A61':
        qas["question"]='How does the proposed method differ from previous methods/approaches?'
    elif question_id=='A42':
        qas["question"]='What model does this paper propose?'
    elif question_id=='A52':
        qas["question"]='What is this model based on?'
    elif question_id=='A62':
        qas["question"]='How does the proposed model differ from previous models?'
    elif question_id=='A43':
        qas["question"]='What algorithm does this paper propose?'
    elif question_id=='A53':
        qas["question"]='What is this algorithm based on?'
    elif question_id=='A63':
        qas["question"]='How does the proposed algorithm differ from previous algorithms?'
    elif question_id=='A44':
        qas["question"]='What framework does this paper propose?'
    elif question_id=='A54':
        qas["question"]='What is this framework based on?'
    elif question_id=='A64':
        qas["question"]='How does the proposed framework differ from previous frameworks?'
    elif question_id=='A45':
        qas["question"]='What datasetdoes this paper propose? '
    elif question_id=='A7':
        qas["question"]='What experiment does this paper carry out to evaluate the result?'
    elif question_id=='A81':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A82':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A83':
        qas["question"]='What does the result of this paper show(demonstrated by the experiment)?'
    elif question_id=='A10':
        qas["question"]='How does this result outperform existing work?'
    else:
        qas["question"]=question_id


    
    qas["id"]=str(nums)
    paragraphs["qas"]=[qas]


    send_message["paragraphs"]=[paragraphs]
    total_data.append(send_message)
    nums+=1

print("data finished")


# In[12]:


total_json={}
total_json["data"]=total_data
total_json["version"]="1.1"
print("total_json completed!")


# In[13]:


with open(os.getcwd()+jsonfile2,'w',encoding="UTF-8") as json_file2:
    json.dump(total_json,json_file2,ensure_ascii=False)


