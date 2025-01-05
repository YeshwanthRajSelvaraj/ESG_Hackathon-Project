from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

app = Flask(__name__)

data_path = "green_finance_data.csv"
green_finance_data = pd.read_csv(data_path)

roi_predictor = LinearRegression()
roi_predictor.fit(
    green_finance_data[["ESG_Score", "Budget"]],
    green_finance_data["ROI"]
)

success_predictor = RandomForestClassifier()
success_predictor.fit(
    green_finance_data[["ESG_Score", "Risk"]],
    green_finance_data["Success"]
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    esg_score = float(request.form['esg_score'])
    budget = float(request.form['budget'])

    predicted_roi = roi_predictor.predict([[esg_score, budget]])[0]
    predicted_success = success_predictor.predict([[esg_score, 0]])[0]  

    return render_template(
        'results.html',
        predicted_roi=predicted_roi,
        predicted_success=predicted_success
    )

if __name__ == '__main__':
    app.run(debug=True)
