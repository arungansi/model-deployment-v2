import pickle

app = Flask(__name__)
token = pickle.load(open("model/cv.pkl", 'rb'))
model = pickle.load(open("model/clf.pkl", 'rb'))

def make_prediction(email_text):
    if email_text == "":
        return ""
    tokenized_email = token.transform([email_text])
    predicted = model.predict(tokenized_email)
    predicted = 1 if predicted == 1 else -1
    return predicted