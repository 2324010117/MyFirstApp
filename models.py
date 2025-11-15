import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import os

# Load models
cnn_model = load_model('models/brain_tumor_cnn.h5')
knn_model = joblib.load('models/knn_model.pkl')
svm_model = joblib.load('models/svm_model.pkl')
rf_model = joblib.load('models/rf_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Class labels
CLASS_LABELS = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def preprocess_image(img_array):
    """Preprocess image for traditional ML models"""
    if len(img_array.shape) == 4:
        img_array = img_array[0]  # Remove batch dimension if present
    
    # Convert to grayscale and flatten
    if img_array.shape[-1] == 3:
        gray_img = np.mean(img_array, axis=-1)
    else:
        gray_img = img_array
    
    # Reshape and scale
    flat_img = gray_img.flatten().reshape(1, -1)
    scaled_img = scaler.transform(flat_img)
    return scaled_img

def predict_with_cnn(img_array):
    """Predict using CNN model"""
    pred = cnn_model.predict(img_array)
    pred_class = np.argmax(pred, axis=1)[0]
    probability = np.max(pred)
    return CLASS_LABELS[pred_class], float(probability)

def predict_with_knn(img_array):
    """Predict using KNN model"""
    processed_img = preprocess_image(img_array)
    pred = knn_model.predict_proba(processed_img)
    pred_class = np.argmax(pred, axis=1)[0]
    probability = np.max(pred)
    return CLASS_LABELS[pred_class], float(probability)

def predict_with_svm(img_array):
    """Predict using SVM model"""
    processed_img = preprocess_image(img_array)
    pred = svm_model.predict_proba(processed_img)
    pred_class = np.argmax(pred, axis=1)[0]
    probability = np.max(pred)
    return CLASS_LABELS[pred_class], float(probability)

def predict_with_rf(img_array):
    """Predict using Random Forest model"""
    processed_img = preprocess_image(img_array)
    pred = rf_model.predict_proba(processed_img)
    pred_class = np.argmax(pred, axis=1)[0]
    probability = np.max(pred)
    return CLASS_LABELS[pred_class], float(probability)

def ensemble_prediction(img_array):
    """Combine predictions from all models"""
    # Get predictions from all models
    cnn_pred, cnn_prob = predict_with_cnn(img_array)
    knn_pred, knn_prob = predict_with_knn(img_array)
    svm_pred, svm_prob = predict_with_svm(img_array)
    rf_pred, rf_prob = predict_with_rf(img_array)
    
    # Collect all predictions
    predictions = [cnn_pred, knn_pred, svm_pred, rf_pred]
    
    # Simple majority voting
    unique, counts = np.unique(predictions, return_counts=True)
    ensemble_pred = unique[np.argmax(counts)]
    
    # Average probability
    avg_prob = (cnn_prob + knn_prob + svm_prob + rf_prob) / 4
    
    return ensemble_pred, float(avg_prob)