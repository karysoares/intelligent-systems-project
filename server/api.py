# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
from model import load_model

app = Flask(__name__)

def _convert_label_to_category(label):
    translate_label_dict = {
        0: 'Bebê',
        1: 'Bijuterias e Jóias',
        2: 'Decoração',
        3: 'Lembrancinhas',
        4: 'Outros',
        5: 'Papel e Cia'
    }
    return translate_label_dict[label]


def _validate_data(data):
    title = data.get('title')
    if title is None:
        return (False, 'title key not found')
    if not isinstance(title, str):
        return (False, 'title value is not a string')
    
    return (True, "All values seem ok.")

@app.route("/v1/categorize", methods=["POST"])
def predict():

    model = load_model()
    
    data = request.get_json(force=True)
    validated, msg = _validate_data(data)

    if not validated:
        return (jsonify({"error": msg}), 400)

    # Use o modelo pré-treinado para predizer o Y
    prediction = model.predict([data['title']])
    # Retorne o primeiro resultado
    output = prediction[0]
    return jsonify(
        {
            "category": _convert_label_to_category(int(output))
        }
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)