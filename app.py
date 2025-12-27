import os
from flask import Flask , render_template, request, redirect, url_for, flash
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.densenet import preprocess_input
from utils.allowed_file import allowed_file
from utils.upload_file import upload_file

import numpy as np


app  =  Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


MODEL_PATH = os.path.join('model', 'model_dense121.keras')
model = load_model(MODEL_PATH)


CLASSES_NAME = [
    'Downdog',
    'Goddess', 
    'Plank', 
    'Tree', 
    'Warrior2'
]


# routes

@app.route('/', methods = ['GET', 'POST'])

def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            
            # preprocess
            img = load_img(filepath, target_size=(224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            # predict
            preds = model.predict(x)
            idx = np.argmax(preds[0])
            label = CLASSES_NAME[idx]
            confidence = preds[0][idx]


            return render_template('index.html',
                                    filename = file.filename,
                                    label = label,
                                    confidence = f"{confidence*100:.1f}%"

                                   )
        
        return redirect(request.url)
    
    return render_template('index.html')


@app.route('/uploads/<filename>')

def uploaded_file(filename):
    return upload_file(filename)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug = True)



