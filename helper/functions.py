from helper.libraries import nltk, WordNetLemmatizer, stopwords, re, pickle

def pre(q):
    stpwrd = nltk.corpus.stopwords.words('english')
    
    STOP_WORDS =stopwords.words("english")
    q =re.sub(r'[^A-Za-z]', " ",str(q))
    q =q.lower().split()
    clean =[]
    for word in q:
        if word not in stpwrd:
            clean.append(word)
    tx =WordNetLemmatizer()
    root =[ ]
    for word in clean:
        word = tx.lemmatize(word)
        root.append(word)
    return " ".join(root)

# For Loading the Pickle File
def load_model():
    with open('./pickle/model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
