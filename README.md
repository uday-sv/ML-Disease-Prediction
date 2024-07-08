
---

# ML Disease Prediction

🌐 Project Deployed at: [https://ml-disease-prediction.onrender.com](https://ml-disease-prediction.onrender.com)

This project uses Flask and a pre-trained K-Nearest Neighbors (KNN) model to predict diseases based on symptoms provided by the user.

## Overview

This repository contains a Flask web application that serves a machine learning model (`knn_model.pkl`) to predict diseases based on user-input symptoms. The model is loaded into memory when the Flask server starts (`app.py`). HTML templates (`index.html`, `details.html`, `results.html`) are used for user interface and result rendering.

## Deployment

The project is deployed using [Render.com](https://render.com). 

### Files

- **app.py**: Flask application handling HTTP requests and serving predictions.
- **templates/**: HTML templates for user interface.
- **knn_model.pkl**: Pre-trained KNN model for disease prediction.
- **requirements.txt**: Python dependencies required for the project.

### Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ML-Disease-Prediction.git
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   Open a web browser and go to [http://localhost:5000](http://localhost:5000)

### Dependencies

- Flask==2.3.3
- numpy==1.24.3
- pandas==2.0.3
- scikit-learn==1.2.2

---



![Screenshot 2023-11-20 184533](https://github.com/smartinternz02/SI-GuidedProject-611642-1700551037/assets/129844163/30f88cac-05d2-4bbc-a894-7ea77f06ae99)

