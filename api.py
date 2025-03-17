from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import io
import json

# Charger le fichier class_mapping.json
try:
    with open("/home/afdel/Desktop/COURS/L3/Computer_Vision/exam/models/class_mapping.json", "r") as f:
        class_mapping = json.load(f)
except FileNotFoundError:
    raise Exception("Le fichier class_mapping.json est introuvable.")
except json.JSONDecodeError:
    raise Exception("Le fichier class_mapping.json est mal formaté.")

# Charger le modèle
chemin = "models/best_model.h5"
model = load_model(chemin)

# Paramètres de prétraitement 
IMAGE_SIZE = (224, 224) 
NORMALIZATION_FACTOR = 1.0 / 255.0  

# Initialiser l'application Flask
app = Flask(__name__)

def preprocess_image(image):
    """Prétraite l'image avant de l'envoyer au modèle."""
    image = image.resize(IMAGE_SIZE)
    image = img_to_array(image) * NORMALIZATION_FACTOR  
    image = np.expand_dims(image, axis=0) 
    return image

@app.route('/predict', methods=['POST'])
def predict():
    """API pour recevoir une image et renvoyer une prédiction."""
    if 'file' not in request.files:
        return jsonify({"error": "Aucune image envoyée"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Aucun fichier sélectionné"}), 400

    # Lire l'image directement en mémoire
    image = Image.open(io.BytesIO(file.read()))

    # Prétraiter l'image
    processed_img = preprocess_image(image)

    # Faire la prédiction
    predictions = model.predict(processed_img)
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_class_str = str(predicted_class)  # Convertir en chaîne de caractères
    predicted_label = class_mapping.get(predicted_class_str, "Inconnu")  # Récupérer le nom du fruit

    return jsonify({
        "prediction": predicted_label,  # Renvoyer le nom du fruit
        "confidence": float(np.max(predictions))
    })

if __name__ == '__main__':
    app.run(debug=True)