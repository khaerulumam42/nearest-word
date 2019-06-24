from flask import Flask, render_template, request
from gensim.models import KeyedVectors
model_name = 'models/wiki_skipgram.vec'
try:
    model = KeyedVectors.load_word2vec_format(model_name)
except FileNotFoundError:
    import os
    print("download model")
    os.system('./download.sh')
    print("download selesai")
app = Flask(__name__)

def toDict(result):
    tmp = {}
    for token, distance in result:
        try:
            tmp[token] = round(float(distance), 3)
        except ValueError:
            tmp[token] = distance
    return tmp

def inference(word, top=5):
    # 5 top similar words
    if type(word) == list:
        word[0] = word[0].lower()
    else:
        word = word.lower()
    try:
        return(model.most_similar(word)[:top])
    except KeyError:
        return([("peringatan", "kata yang Anda masukkan tidak ada dalam vocabulary")])
    

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/top',methods = ['POST'])
def result():
   if request.method == 'POST':
      result = dict(request.form)
      top = toDict(inference(result['kata']))
      return render_template("result.html", result = top)

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 1234)
