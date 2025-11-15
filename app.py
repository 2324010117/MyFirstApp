from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import tensorflow as tf
from sklearn.externals import joblib
from models import predict_with_cnn, predict_with_knn, predict_with_svm, predict_with_rf, ensemble_prediction

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Get selected algorithms
            selected_algorithms = request.form.getlist('algorithms')
            
            # Process image
            img = Image.open(filepath).resize((150, 150))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            # Initialize results
            results = {}
            
            # Run predictions based on selected algorithms
            if 'cnn' in selected_algorithms:
                cnn_pred, cnn_prob = predict_with_cnn(img_array)
                results['CNN'] = {
                    'prediction': cnn_pred,
                    'probability': cnn_prob
                }
            
            if 'knn' in selected_algorithms:
                knn_pred, knn_prob = predict_with_knn(img_array)
                results['KNN'] = {
                    'prediction': knn_pred,
                    'probability': knn_prob
                }
            
            if 'svm' in selected_algorithms:
                svm_pred, svm_prob = predict_with_svm(img_array)
                results['SVM'] = {
                    'prediction': svm_pred,
                    'probability': svm_prob
                }
            
            if 'rf' in selected_algorithms:
                rf_pred, rf_prob = predict_with_rf(img_array)
                results['Random Forest'] = {
                    'prediction': rf_pred,
                    'probability': rf_prob
                }
            
            # Ensemble prediction if more than one algorithm selected
            if len(selected_algorithms) > 1:
                ensemble_pred, ensemble_prob = ensemble_prediction(img_array)
                results['Ensemble'] = {
                    'prediction': ensemble_pred,
                    'probability': ensemble_prob
                }
            
            return render_template('results.html', 
                                 image_file=filename, 
                                 results=results)
    
    return render_template('detect.html')

if __name__ == '__main__':
    app.run(debug=True)