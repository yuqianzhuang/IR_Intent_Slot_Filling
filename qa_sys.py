import re
import torch
from transformers import DistilBertTokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

def convert_to_BERT_tensors(questions, contexts):
    '''takes a parallel list of question strings and answer strings'''
    outputs = tokenizer(questions, contexts , return_tensors="pt", return_attention_mask = True, padding = True, truncation = True, max_length = 512)
    return outputs["input_ids"], outputs["attention_mask"]

def get_answer_span_tensor(question,context,answer):
    input_tokens = tokenizer.tokenize('[CLS] ' + question + ' [SEP] ' + context)
    answer_tokens = tokenizer.tokenize(answer)
    span_len = len(answer_tokens)
    for i in range(min(len(input_tokens) - span_len+1, 512 - span_len - 1)):
        if input_tokens[i:i+span_len] == answer_tokens:
            span = torch.tensor([i,i+span_len - 1])
            break
    else:
        span = torch.tensor([0,0])
    return span

def generate_QA(utts, answers):
    food_lst, name_lst, food_Q, name_Q = [],[],[],[]
    
    for utt,ans in zip(utts, answers):
        food_Q.append('What is the type of food?')
        name_Q.append('What is the name?')
        if re.search(r"(food=)(\w+)", ans):
            food_lst.append(re.search(r"(food=)(\w+)",ans).group(2))
        else:
            food_lst.append('None')
            
        if re.search(r"(name=)(\w+)", ans):
            name_lst.append(re.search(r"(name=)((\w| )+)",ans).group(2))
        else:
            name_lst.append('None')
    return food_lst, name_lst, food_Q, name_Q

class QAdataset(Dataset):
    '''A dataset for housing QA data, including input_data, output_data, and padding mask'''
    def __init__(self, input_data, output_data,mask):
        self.input_data = input_data
        self.output_data = output_data
        self.mask = mask
        
    def __len__(self):
        return len(self.input_data)
    
    def __getitem__(self, index):
        target = self.output_data[index]
        data_val = self.input_data[index]
        mask = self.mask[index]
        return data_val,target,mask
    
def prepare_QA_dataset(questions, contexts, answers, split):  
    QA_input, masks = convert_to_BERT_tensors(questions, contexts)
    spans = []
    if split != "test":
        for i in range(len(questions)):
            spans.append(get_answer_span_tensor(questions[i], contexts[i], answers[i]))
    else:
        spans = [torch.tensor([0,0])]*len(questions)
    return QAdataset(QA_input,spans, masks)