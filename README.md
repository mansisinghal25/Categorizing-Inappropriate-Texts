# Categorizing-Inappropriate-Texts
Built a multi-label classification model that detects inappropriate texts and help us to further categorize them. 

## Dataset
We have used a [kaggle dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) which contains Wikipedia comments labeled by human raters for inappropriate behaviour. The dataset has 6 labels: `’toxic’`, `’severe toxic’`,`’obscene’`, `’threat’`, `’insult’` and `’identity hate’`. We have a total of 2,23,286 data points in our dataset and we have divided it into: 80% training, 10% validation and 10% testing
set. Thus the training set has 1,78,626 samples and the validation and testing set have 22,329 samples each.

### NLP 
As we have a natural language processing problem, we have first performed text cleaning which involves: converting to lowercase,removing special characters,removing numbers,removing stop words,replacing contractions with their full forms and lemmitization.

For factorizing the text data we have used 3 feature extraction techniques: `Bag of word`, `TF-IDF`, `word2vec`.

### Baseline Models
* Naive Bayes 
* Logistic Regression 

### Advanced Models
* SVM
* Random Forest 
* Neural Networks

Out of these, tuned Neural Network with feature engineering, text cleaning and oversampling gave the best results for us with a score of 0.7 (Using 60% Recall + 40% Precision).

For further details please check the [final report](https://github.com/mansisinghal25/Categorizing-Inappropriate-Texts/blob/main/19_Aditi_Mansi_Nimisha_FinalReport.pdf). 
