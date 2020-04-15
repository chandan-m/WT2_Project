# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:06:17 2020

@author: samar
"""
import pandas as pd
import numpy as np
import random
def xLogX(x):
    return x * np.log(x) if x != 0 else 0.0
def entropy(x1, x2=0, x3=0, x4=0):
    return xLogX(x1 + x2 + x3 + x4) - xLogX(x1) - xLogX(x2) - xLogX(x3) - xLogX(x4)
def LLR(k11, k12, k21, k22):
    rowEntropy = entropy(k11 + k12, k21 + k22)
    columnEntropy = entropy(k11 + k21, k12 + k22)
    matrixEntropy = entropy(k11, k12, k21, k22)
    if rowEntropy + columnEntropy < matrixEntropy:
        return 0.0
    return 2.0 * (rowEntropy + columnEntropy - matrixEntropy)
def rootLLR(k11, k12, k21, k22):
    llr = LLR(k11, k12, k21, k22)
    sqrt = np.sqrt(llr)
    if k11 * 1.0 / (k11 + k12) < k21 * 1.0 / (k21 + k22):
        sqrt = -sqrt
    return sqrt
 
def recommendations(df,prod_id):
    #df = pd.read_csv('views.csv')
    #df.shape
    #df.head()

    #df.Likes.unique()
    trans = df
    trans.shape

    visitors = trans['Cust_id'].unique()
    items = trans['Prod_id'].unique()

    trans2 = trans.groupby(['Cust_id']).head(50)
    trans2.shape

    trans2['visitors'] = trans2['Cust_id'].apply(lambda x : np.argwhere(visitors == x)[0][0])
    trans2['items'] = trans2['Prod_id'].apply(lambda x : np.argwhere(items == x)[0][0])


    from scipy.sparse import csr_matrix

    occurences = csr_matrix((visitors.shape[0], items.shape[0]), dtype='int8')
    def set_occurences(visitor, item):
        occurences[visitor, item] += 1
    trans2.apply(lambda row: set_occurences(row['visitors'], row['items']), axis=1)
    occurences

    cooc = occurences.transpose().dot(occurences)
    cooc.setdiag(0)

    row_sum = np.sum(cooc, axis=0).A.flatten()
    column_sum = np.sum(cooc, axis=1).A.flatten()
    total = np.sum(row_sum, axis=0)
    pp_score = csr_matrix((cooc.shape[0], cooc.shape[1]), dtype='double')
    cx = cooc.tocoo()
    for i,j,v in zip(cx.row, cx.col, cx.data):
        if v != 0:
            k11 = v
            k12 = row_sum[i] - k11
            k21 = column_sum[j] - k11
            k22 = total - k11 - k12 - k21
            pp_score[i,j] = rootLLR(k11, k12, k21, k22)
            
            
    #result = np.flip(np.sort(pp_score.A, axis=1), axis=1)
    result_indices = np.flip(np.argsort(pp_score.A, axis=1), axis=1)

    #return result
    m=[]
    num=6
    start=1
    end=34

    if int(prod_id) >= len(result_indices):
        for j in range(num): 
            m=random.sample(range(start, end), num)
    else:
        l=np.unique(result_indices[int(prod_id)][:6]).tolist()
        for k in l:
            m.append(trans2['Prod_id'][k])
    print(m)
    return m