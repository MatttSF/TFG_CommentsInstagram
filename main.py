import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# download stopwords and wordnet if not already downloaded
nltk.download('stopwords')
nltk.download('wordnet')

#dic of contractions
contractions_dict = {
    "ain't": "am not / are not / is not / has not / have not", "aren't": "are not / am not", "can't": "cannot",
    "could've": "could have",    "couldn't": "could not",    "didn't": "did not",    "doesn't": "does not",
    "don't": "do not",    "hadn't": "had not",    "hasn't": "has not",    "haven't": "have not",
    "he'd": "he had / he would",    "he'll": "he shall / he will",    "he's": "he has / he is",    "how'd": "how did",
    "how'll": "how will",    "how's": "how has / how is / how does",    "I'd": "I had / I would",    "I'll": "I shall / I will",
    "I'm": "I am",    "I've": "I have",    "isn't": "is not",    "it'd": "it had / it would",
    "it'll": "it shall / it will",    "it's": "it has / it is",    "let's": "let us",    "might've": "might have",
    "mightn't": "might not",    "must've": "must have",    "mustn't": "must not",    "shan't": "shall not",
    "she'd": "she had / she would",    "she'll": "she shall / she will",    "she's": "she has / she is",    "should've": "should have",
    "shouldn't": "should not",    "that's": "that has / that is",    "there'd": "there had / there would",    "there's": "there has / there is",
    "they'd": "they had / they would",    "they'll": "they shall / they will",    "they're": "they are",    "they've": "they have",    "wasn't": "was not",
    "we'd": "we had / we would",    "we'll": "we shall / we will",    "we're": "we are",    "we've": "we have",    "weren't": "were not",
    "what'll": "what shall / what will",    "what're": "what are",    "what's": "what has / what is",    "what've": "what have",    "where's": "where has / where is",
    "who'd": "who had / who would",    "who'll": "who shall / who will",    "who're": "who are",    "who's": "who has / who is",
    "who've": "who have",    "won't": "will not",    "would've": "would have",    "wouldn't": "would not",
    "you'd": "you had / you would",    "you'll": "you shall / you will",    "you're": "you are",    "you've": "you have"
}
# noise suppression
def remove_noise(text):
    text = re.sub('@[^\s]+', '', text)  # remove usernames
    text = re.sub('\[.*?\]', '', text)  # remove square brackets and contents
    text = re.sub('\w*\d\w*', '', text)  # remove words containing digits
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # remove punctuation
    text = re.sub('\s{2,}', ' ', text)  # remove extra spaces
    return text.strip().lower()

# tokenization
def tokenize(text):
    return word_tokenize(text)

# delete stop words
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word.casefold() not in stop_words]

# stemming and lemmatization
def apply_stemming_and_lemmatization(tokens):
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(stemmer.stem(word)) for word in tokens]

# Define a function to handle contractions in the text
def handle_contractions(text, contractions_dict):
    # Define a regular expression pattern to find contractions
    pattern = re.compile("|".join(contractions_dict.keys()), flags=re.IGNORECASE|re.DOTALL)

    # Define a function to replace each contraction with its expanded form
    def replace(match):
        return contractions_dict[match.group(0).lower()]

    # Replace contractions with their expanded forms in the text
    expanded_text = pattern.sub(replace, text)

    return expanded_text
 
# Iterate over each row in the database
for index, row in database.iterrows():
    # Get the twit from the row
    twit = row["Twit"]
    
    # Call the function to handle contractions
    expanded_twit = handle_contractions(twit, contractions_dict)
    
    # Update the twit field in the row with the expanded twit
    database.at[index, "Twit"] = expanded_twit
    
 
