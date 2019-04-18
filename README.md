# PaperQA
To create a classification model for recommending selected articles. Course Work for [EE448 Big Data Mining](https://www.kaggle.com/c/ee448-paperqa).

## Instruction
In this project, you are given the answers to 19 different queries of 2k+ abstracts of the latest academic papers in the field of Artificial Intelligent. By proposing a QA model, your goal is to select a better answer from the two answers given towards each abstract and question pair. To some extend, the problem of QA is transformed into a two classification task.

## First Attempt
Since SQuAD is familiar with the given dataset. Here is my first attempt 
- [x] csv format -> json format
- [ ] use [QA-Net](https://github.com/NLPLearn/QANet)/[BERT](https://github.com/google-research/bert) to train [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)
- [x] use [BERT](https://github.com/google-research/bert) to train my data
- [x] compare with two choices

### USAGE
 Put train.csv, test.csv, train_csv2json.py under same folder.    
     
     
    python train_csv2json.py    
    
    
 Download BERT    
    
    git clone https://github.com/google-research/bert.git
    
 RUN    
    
    #PBS -l walltime=24:00:00
    
    source activate my_env
    cd /path/to/bert/

    export BERT_BASE_DIR=/path/to/bert/uncased_L-12_H-768_A-12
    export GLUE_DIR=/path/to/bert/glue_data
    export BERT_DIR=/path/to/bert/bert/
    export SQUAD_DIR=/path/to/squad/datasets

    python run_squad.py \
      --vocab_file=$BERT_BASE_DIR/vocab.txt \
      --bert_config_file=$BERT_BASE_DIR/bert_config.json \
      --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
      --do_train=True \
      --train_file=$SQUAD_DIR/train-v1.1.json \
      --do_predict=True \
      --predict_file=$SQUAD_DIR/dev-v1.1.json \
      --train_batch_size=12 \
      --learning_rate=3e-5 \
      --num_train_epochs=2.0 \
      --max_seq_length=384 \
      --doc_stride=128 \
      --output_dir=$BERT_DIR/tmp/squad_base/
    
**Note:Top 3 lines are for qsub**

### Results

    {'same0': 608, 'same': 105}
    {"exact_match": 23.25959001420743, "f1": 53.63440247072295}

Best public leaderboard: 0.78287
