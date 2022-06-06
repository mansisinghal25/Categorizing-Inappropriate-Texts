# -*- coding: utf-8 -*-
"""Nimisha - Oversampling_BaselineModels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1erg64pB412xMaNLszLAwGZoDb595zlrB

# Preprocessing
"""

!pip install scikit-multilearn
!pip install contractions

import pandas as pd
import numpy as np
import re
import nltk.corpus
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('all')
from nltk.corpus import stopwords, words
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import contractions
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale, MinMaxScaler
from skmultilearn.problem_transform import BinaryRelevance, LabelPowerset, ClassifierChain
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
import matplotlib.pyplot as plt

test_label = pd.read_csv("test_labels.csv")
test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

# Merging test and train to form one huge dataset
test_data = pd.merge(test, test_label)
dataset = pd.concat([test_data, train])
dataset.drop(columns=['id'], inplace=True)
dataset.drop_duplicates(inplace=True, ignore_index=True)
dataset.drop(dataset.index[dataset['toxic'] == -1], inplace = True)
dataset.reset_index(inplace = True)
dataset

dataset.shape

dataset

import seaborn as sns
df = dataset
targets = list(df.columns[2:])
df_targets = df[targets].copy()

# How many rows are toxic? 
toxic_rows = df_targets.sum(axis=1)
toxic_rows = (toxic_rows > 0)


count_dic = {}
for comment_type in targets:
    counts = list()
    others = list(targets)
    df_selection = df_targets[(df_targets[comment_type]==1)]
    others.remove(comment_type)
    counts.append(('total', len(df_selection)))
    for other in others:
        counts.append((other, df_selection[other].sum()))
    count_dic[comment_type] = counts


del(df_selection)

def heatmap(df, title):
    plt.figure('heatmap', figsize=[10,10])
    plt.title(title)
    df_corr = df.corr()
    #df_corr = np.triu(df_corr, k=1)
    sns.heatmap(df_corr, vmax=0.6, square=True, annot=True, cmap='YlOrRd')
    plt.yticks(rotation = 45)
    plt.xticks(rotation = 45)
    plt.show()

heatmap(df_targets, 'Heatmap of all labels')


print('Training Data Comment Breakdown')
print('=====\n')

print('%d out of %d comments, or %.2f%%, are classified as toxic.' % 
     (np.sum(toxic_rows), len(df), (np.sum(toxic_rows)/len(df))*100))

totals = []
for key, value in count_dic.items():
    totals.append(value[0][1])
    print('\n%d %s comments. (%.2f%% of all data.)' % (value[0][1], key, (value[0][1]/len(df))*100))
    for cnt in value[1:]:
        print('- %d or %.2f%% were also %s.' % (cnt[1], (cnt[1]/value[0][1])*100, cnt[0]))
    

plt.figure('Comment Type Counts', figsize=[8,6])
plt.title('Comment Type Counts')
sns.barplot(x=list(count_dic.keys()), y=totals)
plt.show()

# num=0
# for i in range(10000):
#     if(dataset["severe_toxic"][i]==1):
#         # new = [dataset["index"][i],dataset["comment_text"][i],dataset["toxic"][i],1,dataset["obscene"][i],dataset["threat"][i],dataset["insult"][i],dataset["identity_hate"][i]]
#         new = dataset["comment_text"][i],dataset["identity_hate"][i],[dataset["index"][i],dataset["insult"][i],dataset["obscene"][i],1,dataset["threat"][i],dataset["toxic"][i]] 
#         print(new)
#         dataset= dataset.append(new)
#         num=num+1
# print(num)
# # dataset["toxic"][0]=1
# # dataset

dataset.shape

dd= dataset.loc[dataset['severe_toxic'] == 1]
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset.shape
dd= dataset.loc[dataset['threat'] == 1]
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset.shape
dd= dataset.loc[dataset['identity_hate'] == 1]
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset= pd.concat([dataset, dd])
dataset.shape

dataset

import seaborn as sns
df = dataset
targets = list(df.columns[2:])
df_targets = df[targets].copy()

# How many rows are toxic? 
toxic_rows = df_targets.sum(axis=1)
toxic_rows = (toxic_rows > 0)


count_dic = {}
for comment_type in targets:
    counts = list()
    others = list(targets)
    df_selection = df_targets[(df_targets[comment_type]==1)]
    others.remove(comment_type)
    counts.append(('total', len(df_selection)))
    for other in others:
        counts.append((other, df_selection[other].sum()))
    count_dic[comment_type] = counts


del(df_selection)

def heatmap(df, title):
    plt.figure('heatmap', figsize=[10,10])
    plt.title(title)
    df_corr = df.corr()
    #df_corr = np.triu(df_corr, k=1)
    sns.heatmap(df_corr, vmax=0.6, square=True, annot=True, cmap='YlOrRd')
    plt.yticks(rotation = 45)
    plt.xticks(rotation = 45)
    plt.show()

heatmap(df_targets, 'Heatmap of all labels')


print('Training Data Comment Breakdown')
print('=====\n')

print('%d out of %d comments, or %.2f%%, are classified as toxic.' % 
     (np.sum(toxic_rows), len(df), (np.sum(toxic_rows)/len(df))*100))

totals = []
for key, value in count_dic.items():
    totals.append(value[0][1])
    print('\n%d %s comments. (%.2f%% of all data.)' % (value[0][1], key, (value[0][1]/len(df))*100))
    for cnt in value[1:]:
        print('- %d or %.2f%% were also %s.' % (cnt[1], (cnt[1]/value[0][1])*100, cnt[0]))
    

plt.figure('Comment Type Counts', figsize=[8,6])
plt.title('Comment Type Counts')
sns.barplot(x=list(count_dic.keys()), y=totals)
plt.show()

"""## Text cleaning"""

# Text cleaning
#converting to lower case
dataset['comment_text_cleaned'] = dataset['comment_text'].str.lower()
#removing special characters
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", str(elem)))
#removing numbers
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda elem: re.sub(r"\d+", "", str(elem)))
# Removing stop words
stop = stopwords.words('english')
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
import contractions
# Replacing contractions with their full forms
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda x: contractions.fix(x))
#Tokenizing
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda x: word_tokenize(x))
#Lemmitization
def word_lemmatizer(text):
    lem_text = [WordNetLemmatizer().lemmatize(i) for i in text]
    return lem_text
dataset['comment_text_cleaned'] = dataset['comment_text_cleaned'].apply(lambda x: word_lemmatizer(x))
dataset

"""## Train test dev split"""

# Splitting into train test sets
X = dataset.drop(columns=['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'])
y = dataset[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].copy()

X_train, X_test_and_val, y_train, y_test_and_val = train_test_split(X,y, train_size=0.8)
X_val, X_test, y_val, y_test = train_test_split(X_test_and_val,y_test_and_val, train_size=0.5)

dataset.shape

X_train.shape

X_test.shape

X_val.shape

y_train.shape

y_test.shape

y_val.shape

# dd= dataset.loc[dataset['severe_toxic'] == 1]
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset.shape
# dd= dataset.loc[dataset['threat'] == 1]
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset.shape
# dd= dataset.loc[dataset['identity_hate'] == 1]
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset= pd.concat([dataset, dd])
# dataset.shape

dataset2= X_train.join(y_train)

dd = dataset2.loc[dataset2['severe_toxic'] == 1]
dataset2= pd.concat([dataset2, dd])
dd= dataset2.loc[dataset2['threat'] == 1]
dataset2= pd.concat([dataset2, dd])
dd= dataset2.loc[dataset2['identity_hate'] == 1]
dataset2= pd.concat([dataset2, dd])

X_train = dataset2.drop(columns=['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'])
y_train = dataset2[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].copy()

"""## Word2Vec"""

train_tokens = pd.Series(X_train['comment_text_cleaned']).values
w2v_model = Word2Vec(train_tokens, size= 200, min_count=1)

def buildWordVector(tokens, size):
  vec = np.zeros(size).reshape((1, size))
  count = 0.
  for word in tokens:
    try:
      vec += w2v_model.wv[word].reshape((1, size))
      count += 1.
    except KeyError:
      continue
  if count != 0:
    vec /= count
  return vec

train_vecs_w2v = np.concatenate([buildWordVector(z, 200) for z in train_tokens])
# train_vecs_w2v = scaler.fit_transform(train_vecs_w2v)
train_vecs_w2v = scale(train_vecs_w2v)

val_tokens = pd.Series(X_val['comment_text_cleaned']).values
val_vecs_w2v = np.concatenate([buildWordVector(z, 200) for z in val_tokens])
# val_vecs_w2v = scaler.transform(val_vecs_w2v)
val_vecs_w2v = scale(val_vecs_w2v)

print(accuracy_score)

"""# Models

## Naive Bayes + Binary Relevance
"""

def evaluation_metric(y_true, y_pred):
  print(precision_score(y_true, y_pred, average='micro'))
  if(precision_score(y_true, y_pred, average='micro') > 0.1):
    print(recall_score(y_true, y_pred, average='micro'))
  else:
    print('Precision too low')

classifier = BinaryRelevance(GaussianNB())
classifier.fit(train_vecs_w2v, y_train)
predictions = classifier.predict(val_vecs_w2v)

train_pred = classifier.predict(train_vecs_w2v)

val_vecs_w2v

print("Score = ",evaluation_metric(y_val, predictions))

y_val.shape

!pip install imblearn==0.0

from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter

y_test.shape

# X_train[:, 0]
predictions.shape

def score(y_true, y_pred, label):
  prec = precision_score(y_true, y_pred)
  re = recall_score(y_true, y_pred)
  print('Results for label:', label)
  print('Precision score:', prec)
  print('Recall score:', re)
  print('Final Score:', re*0.6 + prec*0.4, '\n')
  return [re*0.6 + prec*0.4, prec, re]

# predictions = predictions.toarray()
# train_pred = train_pred.toarray()
y_pred = pd.DataFrame({'toxic': predictions[0,:], 'severe_toxic': predictions[1,:], 'obscene': predictions[2,:], 'threat': predictions[3,:], 'insult': predictions[4,:], 'identity_hate': predictions[5,:]}, index=[0])
print(y_pred.shape)
y_pred_train = pd.DataFrame({'toxic': train_pred[0,:], 'severe_toxic': train_pred[1,:], 'obscene': train_pred[2,:], 'threat': train_pred[3,:], 'insult': train_pred[4,:], 'identity_hate': train_pred[5,:]}, index=[0])
print(y_pred_train.shape)
print(y_val.head)
# print(y_test.head)

# y_test= y_test[0:21142]
print('Model: Tuned Random Forest with Classifier Chains \nFeature extraction method: Word2Vec ')
print()
prec_score = []
re_score = []
fina_score = []
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

for label in labels:
  scores = score(y_val[label], y_test[label], label)
  fina_score.append(scores[0])
  prec_score.append(scores[1])
  re_score.append(scores[2])

from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(labels, fina_score, 'b', label='Final score')
line2, = plt.plot(labels, prec_score, 'r', label='Precision score')
line3, = plt.plot(labels, re_score, 'g', label='Recall score')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel('Score')
plt.xlabel('Labels')
plt.show()

"""## Naive bayes + label powerset"""

classifier = LabelPowerset(GaussianNB())
classifier.fit(train_vecs_w2v, y_train)
predictions = classifier.predict(val_vecs_w2v)

print("Score = ",evaluation_metric(y_val, predictions))

"""## Naive Bayes + classifier chains"""

classifier = ClassifierChain(GaussianNB())
classifier.fit(train_vecs_w2v, y_train)
predictions = classifier.predict(val_vecs_w2v)

print("Score = ",evaluation_metric(y_val, predictions))

# def score(y_true, y_pred, label):
#   prec = precision_sco  re(y_true, y_pred)
#   re = recall_score(y_true, y_pred)
#   print('Results for label:', label)
#   print('Precision score:', prec)
#   print('Recall score:', re)
#   print('Final Score:', re*0.6 + prec*0.4, '\n')
#   return [re*0.6 + prec*0.4, prec, re]

# # predictions = predictions.toarray()
# # train_pred = train_pred.toarray()
# y_pred = pd.DataFrame({'toxic': predictions[:, 0], 'severe_toxic': predictions[:, 1], 'obscene': predictions[:, 2], 'threat': predictions[:, 3], 'insult': predictions[:, 4], 'identity_hate': predictions[:, 5]})
# y_pred_train = pd.DataFrame({'toxic': train_pred[:, 0], 'severe_toxic': train_pred[:, 1], 'obscene': train_pred[:, 2], 'threat': train_pred[:, 3], 'insult': train_pred[:, 4], 'identity_hate': train_pred[:, 5]})

# print('Model: Tuned Random Forest with Classifier Chains \nFeature extraction method: Word2Vec ')
# print()
# prec_score = []
# re_score = []
# fina_score = []
# labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# for label in labels:
#   scores = score(y_val[label], y_pred[label], label)
#   fina_score.append(scores[0])
#   prec_score.append(scores[1])
#   re_score.append(scores[2])

# from matplotlib.legend_handler import HandlerLine2D
# line1, = plt.plot(labels, fina_score, 'b', label='Final score')
# line2, = plt.plot(labels, prec_score, 'r', label='Precision score')
# line3, = plt.plot(labels, re_score, 'g', label='Recall score')
# plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
# plt.ylabel('Score')
# plt.xlabel('Labels')
# plt.show()

"""## Logistic Regression + Binary Relevance"""

classifier = BinaryRelevance(LogisticRegression(max_iter=1000, solver = 'newton-cg'))
classifier.fit(train_vecs_w2v, y_train)
predictions = classifier.predict(val_vecs_w2v)

print("Score = ",evaluation_metric(y_val, predictions))

"""# Feature extraction

## Bag of words
"""

bow_transform = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False, max_features = 1000)
X_tr_bow = bow_transform.fit_transform(X_train['comment_text_cleaned'])
X_te_bow = bow_transform.transform(X_val['comment_text_cleaned'])

classifier = BinaryRelevance(GaussianNB())
classifier.fit(X_tr_bow, y_train)
predictions = classifier.predict(X_te_bow)

"""## TF - IDF"""

tfidf_transform = TfidfTransformer(norm=None)
X_tr_tfidf = tfidf_transform.fit_transform(X_tr_bow)
X_te_tfidf = tfidf_transform.transform(X_te_bow)

classifier = BinaryRelevance(GaussianNB())
classifier.fit(X_tr_tfidf, y_train)
predictions = classifier.predict(X_te_tfidf)

"""# Other code"""

from sklearn.svm import SVC
classifier = BinaryRelevance(SVC())
classifier.fit(train_vecs_w2v, y_train)
predictions = classifier.predict(val_vecs_w2v)
train_pred = classifier.predict(train_vecs_w2v)

import pickle
filename = 'random_forest_model.sav'
pickle.dump(clf, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
train_pred = loaded_model.predict(train_vecs_w2v)

result_test = evaluation_metric('SVM with Binary Relevance', 'Word2Vec', y_val, predictions)

result_train = evaluation_metric('SVM with Binary Relevance', 'Word2Vec', y_train, train_pred)

print("Variance is: ",result_train - result_test)

print('Model: Random Forest with Multi Output classifier \nFeature extraction method: Word2Vec ')
print()
prec_score = []
re_score = []
fina_score = []
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

for label in labels:
  scores = score(y_val[label], y_pred[label], label)
  fina_score.append(scores[0])
  prec_score.append(scores[1])
  re_score.append(scores[2])

from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(labels, fina_score, 'b', label='Final score')
line2, = plt.plot(labels, prec_score, 'r', label='Precision score')
line3, = plt.plot(labels, re_score, 'g', label='Recall score')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel('Score')
plt.xlabel('Labels')
plt.show()

print('Model: Random Forest with Multi Output classifier \nFeature extraction method: Word2Vec ')
print()

fina_score = []
labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

for label in labels:
  scores = score(y_train[label], y_pred_train[label], label)
  fina_score.append(scores[0])

from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(labels, fina_score, 'b', label='Final score')
line2, = plt.plot(labels, prec_score, 'r', label='Precision score')
line3, = plt.plot(labels, re_score, 'g', label='Recall score')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel('Score')
plt.xlabel('Labels')
plt.show()

solver = [0.1,1, 10, 100]
train_results = []
test_results = []
for estimator in solver:
   classifier = ClassifierChain(SVC(C = estimator))
   classifier.fit(train_vecs_w2v, y_train)
   train_pred = classifier.predict(train_vecs_w2v)
   score = evaluation_metric('SVM with classifier chain', 'Word2Vec', y_train, train_pred)
   train_results.append(score)

   y_pred = classifier.predict(val_vecs_w2v)
   score = evaluation_metric('SVM with classifier chain', 'Word2Vec', y_val, y_pred)
   test_results.append(score)

from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(solver, train_results, 'b', label='Train score')
line2, = plt.plot(solver, test_results, 'r', label='Test score')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel('Score')
plt.xlabel('C')
plt.show()

"""<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=d4bbcc8e-b933-469c-9184-16f0c72be264' target="_blank">
<img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
"""