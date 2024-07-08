from flask import Flask, render_template, request
import numpy as npimport
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('knn_model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/details')
def pred():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    col = ['muscle_pain', 'nausea', 'throat_irritation', 'weight_loss',
       'passage_of_gases', 'skin_peeling', 'blister', 'high_fever',
       'swelling_of_stomach', 'fast_heart_rate', 'muscle_weakness', 'fatigue',
       'red_spots_over_body', 'movement_stiffness', 'malaise', 'headache',
       'yellowing_of_eyes', 'abdominal_pain', 'mild_fever', 'depression',
       'knee_pain', 'swelled_lymph_nodes', 'loss_of_appetite', 'phlegm',
       'blood_in_sputum', 'irritability', 'itching', 'spinning_movements',
       'irregular_sugar_level', 'weight_gain', 'dark_urine',
       'acute_liver_failure', 'lethargy', 'dischromic _patches',
       'excessive_hunger', 'back_pain', 'obesity', 'swelling_joints',
       'loss_of_balance', 'weakness_of_one_body_side', 'neck_pain',
       'joint_pain', 'lack_of_concentration', 'indigestion',
       'toxic_look_(typhos)', 'chills', 'pain_behind_the_eyes', 'sweating',
       'constipation', 'restlessness']

    if request.method == 'POST':
        inputt = [str(x) for x in request.form.values()]

        input_data = {symptom: 1 if symptom in inputt else 0 for symptom in col}

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)[0]
        print(prediction)
        return render_template('results.html', predictedValue=prediction)

if __name__ == "__main__":
    app.run(debug=True)
