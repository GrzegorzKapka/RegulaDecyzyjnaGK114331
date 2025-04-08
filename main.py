from flask import Flask
from flask import request

# utwórz obiekt app 
app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def get_hello():
    num1 = request.args.get("num1", "0")
    num2 = request.args.get("num2", "0")

    try:
        num1 = float(num1)
    except:
        num1 = 0

    try:
        num2 = float(num2)
    except:
        num2 = 0
        
    prediction = int(num1 + num2 > 5.8)
    
    d = {
        'features': [num1, num2],
        'prediction': prediction
    }

    return d


if __name__ == '__main__':
    app.run()
  
