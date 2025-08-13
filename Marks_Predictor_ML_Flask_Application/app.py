from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

# Load the saved model
model = load('attendance_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')  # Serve frontend

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Expect JSON {"attendance": 85}
    attendance = float(data['attendance'])
    
    # Clip attendance to valid range
    attendance = max(0, min(attendance, 100))
    
    # Make prediction (input as 2D array)
    pred = model.predict([[attendance]])
    
    # Clip predicted scores to ≤ 100
    math_score = min(pred[0][0], 100)
    science_score = min(pred[0][1], 100)
    
    # Prepare response
    response = {
        'Math_Score': float(math_score),
        'Science_Score': float(science_score)
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
