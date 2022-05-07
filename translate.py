from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/translate', methods = ['POST'])
def index():
    variable_name = request.get_json()
    language = variable_name['language'] 
    text = variable_name['text'] 

    translator = Translator()
    translated = (translator.translate(text, dest=language, src='auto')).text

    ret_ob = {"text": translated}
    return jsonify(ret_ob)

if __name__ == "__main__":
    app.run(port=5004)
