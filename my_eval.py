""" Official evaluation script for v1.1 of the SQuAD dataset. """
from __future__ import print_function
from collections import Counter
import string
import re
import argparse
import json
import sys
import os
import pandas as pd


def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def f1_score(prediction, ground_truth):
    prediction_tokens = normalize_answer(prediction).split()
    ground_truth_tokens = normalize_answer(ground_truth).split()
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return 0
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)

    return f1


def exact_match_score(prediction, ground_truth):
    return (normalize_answer(prediction) == normalize_answer(ground_truth))


def metric_max_over_ground_truths(metric_fn, prediction, ground_truths,total):
    scores_for_ground_truths = []
    for ground_truth in ground_truths:
        score = metric_fn(prediction, ground_truth)
        scores_for_ground_truths.append(score)
    return (scores_for_ground_truths)


def evaluate(dataset, predictions):
    f1 = exact_match = total = 0
    same = same0 = 0
    for article in dataset:
        for paragraph in article['paragraphs']:
            for qa in paragraph['qas']:
                total += 1
                one_answer=[total]
                if qa['id'] not in predictions:
                    message = 'Unanswered question ' + qa['id'] + \
                              ' will receive score 0.'
                    print(message, file=sys.stderr)
                    continue
                ground_truths = list(map(lambda x: x['text'], qa['answers'])) #dev答案
                prediction = predictions[qa['id']]  #预测答案
                exact_match_list = metric_max_over_ground_truths(
                    exact_match_score, prediction, ground_truths,total)
                f1_list= metric_max_over_ground_truths(
                    f1_score, prediction, ground_truths,total)
                print('f1score: ')
                print(f1_list)
                print('\n')
                if(f1_list[0]>f1_list[1]):
                    Category=1
                if(f1_list[0]<f1_list[1]):
                    Category=2
                if(f1_list[0]==f1_list[1]):
                    Category=1
                    if(f1_list[0]==0):
                        same0+=1
                    else:
                        same+=1
                one_answer.append(f1_list[0])    #使用f1score
                one_answer.append(f1_list[1])  
                answer.append(one_answer)

                one_answer=[total]
                one_answer.append(Category)
                answer0.append(one_answer)

                if(f1_list[0]==f1_list[1]):
                    Category=2
                one_answer=[total]
                one_answer.append(Category)
                answer1.append(one_answer)

                
                exact_match +=max(exact_match_list)
                f1+=max(f1_list)

    exact_match = 100.0 * exact_match / total
    f1 = 100.0 * f1 / total
    print({'same0':same0,'same':same})


    return {'exact_match': exact_match, 'f1': f1}


if __name__ == '__main__':
    answer=[]  #[[1,0.1,0.2],[2,0.2,0.8],...]
    answer0=[]
    answer1=[]

    expected_version = '1.1'
    parser = argparse.ArgumentParser(
        description='Evaluation for SQuAD ' + expected_version)
    parser.add_argument('dataset_file', help='Dataset file')
    parser.add_argument('prediction_file', help='Prediction File')
    args = parser.parse_args()
    with open(args.dataset_file,'r', encoding='UTF-8') as dataset_file:
        dataset_json = json.load(dataset_file)
        if (dataset_json['version'] != expected_version):
            print('Evaluation expects v-' + expected_version +
                  ', but got dataset with v-' + dataset_json['version'],
                  file=sys.stderr)
        dataset = dataset_json['data']
    with open(args.prediction_file,'r', encoding='UTF-8') as prediction_file:
        predictions = json.load(prediction_file)
    print(json.dumps(evaluate(dataset, predictions)))
    myans=pd.DataFrame(columns=['Id','Ans1','Ans2'],data=answer)
    myans.to_csv('ydc_first_try.csv')


    ans0=pd.DataFrame(columns=['Id','Category'],data=answer0)
    ans0[['Id','Category']].to_csv('ydc_first_try_0.csv',index=0)
    ans1=pd.DataFrame(columns=['Id','Category'],data=answer1)
    ans1[['Id','Category']].to_csv('ydc_first_try_1.csv',index=0)