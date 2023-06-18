from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
token = pickle.load(open("model/cv.pkl", 'rb'))
model = pickle.load(open("model/clf.pkl", 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        email_text = request.form.get("email-content")
    tokenized_email = token.transform([email_text])
    predicted = model.predict(tokenized_email)
    predicted = 1 if predicted == 1 else -1
    return render_template("index.html", predicted = predicted, email_text = email_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)#debug is requried to refresh changes to code