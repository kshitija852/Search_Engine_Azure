
import os 
from flask import Flask, render_template, request
#nltk is "Natural Language Toolkit used for applying in natural language processing(NLP)"
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

app = Flask(__name__)

ps = PorterStemmer()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def FileCleaning():
    file_path = "static/"
    l_d = os.listdir(file_path)
    # This would print all the files and directories
    print(l_d)
    for tx in l_d:
        print('The value of tx is:',tx)
        
        # IT indicates to consider only the words and punctuation and digits will be ignored
        # It '\w+' only matches a single word char, not a whole word. 
        # Returns a match where the string contains any word characters 
        # (characters from a to Z, digits from 0-9, and the underscore _ character)
        # r is used for regular expression it matches the 

        tokenizer = RegexpTokenizer(r'\w+')

        file = open("static/"+tx, encoding="utf8")
    
        new_file = 'new/{}'.format(tx)
        #Lines = files.readlines()
        #print(Lines)
        for i in file:
                # To convert all the words into lower case letters 
                i = i.lower()
                tokenizer1 = tokenizer.tokenize(i)
                # It will eliminate all the stop words
                filtered = [w for w in tokenizer1 if not w in stopwords.words('english')]
                # It will join the satisfying the condition using space.
                filter = " ".join(filtered)
                # It will write the sentences to the text file which is present in the new folder
                newfile = open(new_file, 'a',encoding="utf8")
                newfile.write(filter+ "\n")
                newfile.close()
    file.close()


@app.route("/search_word", methods=['POST','GET'])
def search_word():
    name = []
    sentence = []
    no = []
    pos = []
    if request.method=='POST':
        word=str(request.form['word'])
        path="new/"
        l_d = os.listdir(path)

        for tx in l_d:
            file = open('new/{}'.format(tx), encoding="utf8")
            count = 0
            
            for i in file:
                count=count+1
                if word in i:
                    wordpos=0
                    # The strip() removes the left and right side white spaces and also splits
                    # The words by spaces contained in the particular line i
                    getword = i.strip().split(' ')
                    
                    for w1 in getword:
                        wordpos = wordpos + 1
                        if w1 == word:
                            no.append(count)
                            pos.append(wordpos)
                            sentence.append(i)
                            name.append(tx.split('.')[0])
                        else:
                            continue
            file.close()
        result = zip(name,sentence,no,pos)
        return render_template('search_word.html', result=result, word=word)

    else:
        return render_template('search_word.html')


@app.route("/word_combination",methods=['POST','GET'])
def word_combination():
    name = []
    sentence = []
    no = []
    pos = []
    if request.method=='POST':
        word_comb = str(request.form['word_comb'])
        path="new/"
        l_d = os.listdir(path)
        for tx in l_d:
            file = open('new/{}'.format(tx), encoding="utf8")
            count = 0
            
            for i in file:
                count=count+1
                if word_comb in i:
                    no.append(count)
                    sentence.append(i)
                    name.append(tx.split('.')[0])
            file.close()
        result = zip(name,sentence,no)
        return render_template('word_combination.html', result=result, word=word_comb)
    else:
        return render_template('word_combination.html')


if __name__ == '__main__':
   # FileCleaning()
    app.run(debug=True)

