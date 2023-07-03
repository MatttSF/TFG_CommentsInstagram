# Twitter Comment Classifier
This is a machine learning project that aims to classify tweets as positive or negative. The goal is to study the % of negative tweets on a different profiles.

## Dataset
The dataset used for this project is the Sentiment140 dataset, which contains 1.6 million tweets in English labeled as positive or negative.
https://www.kaggle.com/datasets/kazanova/sentiment140?resource=download 

## Preprocessing
The following preprocessing techniques were applied to the comments before training the model:

Noise suppression
Tokenization
Stop word removal
Stemming and Lemmatization

The classification models were SVM, LSTM, Decision Tree

## Evaluation
The model achieved an accuracy of 78% on the test set. 

## Future Work
Improve the model's performance by experimenting with different architectures and hyperparameters.
Extend the model to classify comments in other languages.
Explore the impact of different types of negative comments on the popularity of a profile.
