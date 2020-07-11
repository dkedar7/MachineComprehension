import numpy as np
import string
from nltk import word_tokenize
import onnxruntime as nxrun
import joblib

import torch
from transformers.pipelines import pipeline
from transformers.modeling_auto import AutoModelForQuestionAnswering
from transformers.tokenization_auto import AutoTokenizer

model_path = './models'

def bidaf_answer(context, query):
    '''
    Callback for BiDAF
    '''
    
    def preprocess(text):
       tokens = word_tokenize(text)
       # split into lower-case word tokens, in numpy array with shape of (seq, 1)
       words = np.asarray([w.lower() for w in tokens]).reshape(-1, 1)
       # split words into chars, in numpy array with shape of (seq, 1, 1, 16)
       chars = [[c for c in t][:16] for t in tokens]
       chars = [cs+['']*(16-len(cs)) for cs in chars]
       chars = np.asarray(chars).reshape(-1, 1, 1, 16)
       return words, chars


    sess = nxrun.InferenceSession(model_path+"/BiDAF.pkl")

    cw, cc = preprocess(context)
    qw, qc = preprocess(query)
    
    answer = sess.run(None, 
                  {'context_word': cw,
                   'context_char': cc,
                   'query_word': qw,
                   'query_char': qc})
    
    answer = sess.run(None, 
                  {'context_word': cw,
                   'context_char': cc,
                   'query_word': qw,
                   'query_char': qc})
    
    # assuming answer contains the np arrays for start_pos/end_pos
    start = np.asscalar(answer[0])
    end = np.asscalar(answer[1])
    return (" ".join([w for w in cw[start:end+1].reshape(-1)]))

def transformer_models(model_name):
    model =  AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return qa_pipeline

def distilbert_answer(context, query):
    '''
    Callback for DistilBERT
    '''
    distilbert_model = pipeline('question-answering')
#     distilbert_model = joblib.load(model_path+'/DistilBERT.pkl')
    try:
        res = distilbert_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."

def roberta_answer(context, query):
    '''
    Callback for RoBERTa
    '''
    roberta_model = transformer_models("deepset/roberta-base-squad2")
#     roberta_model = joblib.load(model_path + '/RoBERTa.pkl')
    try:
        res = roberta_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."

def albert_answer(context, query):
    '''
    Callback for ALBERT
    '''
    albert_model = transformer_models("twmkn9/albert-base-v2-squad2")
#     albert_model = joblib.load(model_path + '/ALBERT.pkl')
    try:
        res = albert_model(question=query, context=context)
        return res['answer']
    except:
        return "Snap! The model couldn't find an answer. Try a different query."