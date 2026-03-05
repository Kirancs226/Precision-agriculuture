import pickle
import numpy as np

# load trained model
model = pickle.load(open("models/crop_model.pkl", "rb"))

def predict_crop(features):

    prediction = model.predict([features])

    return prediction[0]