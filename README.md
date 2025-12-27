# Yoga Pose Classification – Deep Learning Web Application

## Overview

This project presents an **end-to-end Yoga Pose Classification system** that integrates **Deep Learning (DenseNet121)** with a **Flask-based web application**. Users can upload an image of a yoga pose and obtain the predicted pose along with confidence scores.

The project follows **industry best practices**, including modular code structure, clean separation of concerns, and deployment-ready architecture. It is suitable for **portfolio presentation**, **internship submissions**, and **real-world AI application demos**.



## Key Skills and Technologies

* **Deep Learning / Transfer Learning:** DenseNet121, TensorFlow, Keras
* **Computer Vision:** Image preprocessing, augmentation, classification
* **Web Development:** Flask, Jinja templating, HTML/CSS
* **Data Handling & Analysis:** NumPy, Pandas, visualization
* **Deployment Readiness:** Modular structure, model serialization, upload handling

This highlights transferable skills relevant to AI, ML, and full-stack roles.


## Dataset Information

* **Dataset Name:** Yoga Pose Classification Dataset
* **Source:** Kaggle
* **Link:** [https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification](https://www.kaggle.com/datasets/ujjwalchowdhury/yoga-pose-classification)
* **Structure:** Class-wise folders containing labeled images of yoga poses

---

## Model Architecture

* **Architecture:** DenseNet121 (transfer learning)
* **Pre-trained on:** ImageNet
* **Input Size:** 224 × 224 × 3
* **Loss Function:** Categorical Crossentropy
* **Optimizer:** Adam (Learning Rate: 1e-4)
* **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score

The DenseNet base layers are frozen and a custom classification head is trained on the yoga pose dataset.

---

## Project Structure

```
yoga-pose-classifier/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Project dependencies
├── notebook/                  # Jupyter notebook containing 
│   └── yoga_pose_classification.ipynb
│
├── model/
│   └── model_dense121.keras   # Trained DenseNet121 model
│
├── utils/
│   ├── allowed_file.py        # File extension validation
│   └── upload_file.py         # Upload redirection helper
│
├── static/
│   ├── css/
│   │   └── style.css     # styling
│   └── uploads/          # Uploaded images
│
├── templates/
│   └── index.html             # Main UI template
└── README.md             
```


## Application Workflow

1. User uploads an image via the web interface.
2. File is validated using `allowed_file()`.
3. Image is saved to `static/uploads/`.
4. Image is preprocessed for DenseNet121 input.
5. Model predicts pose and confidence.
6. Result displayed on UI.

## UI Preview:


![downdog](https://github.com/user-attachments/assets/a9bc97e4-dc22-41b6-b8f8-e7b0ba769bf3)


![warrrior 2](https://github.com/user-attachments/assets/91d9ab76-5803-4d89-bb0d-9440d5fb7080)

![plank](https://github.com/user-attachments/assets/c92e9226-8e23-4e9a-92c5-c1f1f92e5ca4)

![godeness](https://github.com/user-attachments/assets/a5ea1395-1078-455a-958d-76a69d677083)



## Utility Modules

* **`allowed_file.py`**: Ensures only supported image formats are accepted.
* **`upload_file.py`**: Handles clean routing for uploaded images.

Modular utilities improve code readability and maintainability.


## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/batoolarifa/yoga-pose-classifier
cd yoga-pose-classifier
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Access the app at: `http://localhost:8080`


## Model Inference Example

* Upload a yoga pose image (JPG / PNG).
* Model predicts one of the following poses:

  * Downdog
  * Goddess
  * Plank
  * Tree
  * Warrior2
* Confidence score displayed alongside prediction.


## Deployment 

* Ready for deployment on platforms such as **Hugging Face Spaces, Render, AWS EC2, or Docker environments**.
* Model loaded once at startup for efficient inference.
* Supports easy class extension and integration into larger systems.


## Industry Relevance & Value

This project demonstrates:

* **End-to-end ML application development**
* **Deep learning expertise**
* **Full-stack AI system implementation**
* **Reproducible and scalable code practices**
* Skills aligned with **AI/ML, Computer Vision, and Software Engineering roles**

> This section highlights the project’s alignment with industry standards and professional portfolios.

## Future Improvements

* Real-time webcam inference
* Pose correction feedback and tips
* REST API conversion (FastAPI)
* Enhanced UI accessibility and responsiveness



## 👤 Author

**Syeda Arifa Batool**  
SE @ Karachi University | AI & ML Practitioner | Applying technology to create real-world value 📈



## 🔗 Connect with Me

- **LinkedIn:** https://www.linkedin.com/in/arifa-batool/  
- **Kaggle:** https://www.linkedin.com/in/arifa-batool/  
- **Email:** thearifabatool@gmail.com


⭐ If you find this project useful, feel free to star the repository!