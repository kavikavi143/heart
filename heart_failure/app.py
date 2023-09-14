# GITHUB: https://github.com/hfhoffman1144/Heart-Disease-Prediction
#         https://towardsdatascience.com/an-end-to-end-machine-learning-project-heart-failure-prediction-part-2-4518d2596421
from flask import Flask, render_template
from api_routes import bp1

app = Flask(__name__)

app.register_blueprint(bp1)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
