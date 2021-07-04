# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("Index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
           # reading the inputs given by the user
           Pclass = (request.form["Pclass"])

           count = {'Upper': 1, 'Middle': 2, 'Lower': 3}
           key_list = list(count.keys())
           val_list = list(count.values())
           val = key_list.index(Pclass)
           pclass = val_list[val]

           age = float(request.form['age'])

           SibSp = float(request.form["SibSp"])

           Parch = float(request.form["Parch"])

           Fare = float(request.form["Fare"])

           Gender = (request.form["Gender"])
           if Gender == "Female":
               gender = 1
           else:
               gender = 0


           filename = 'modelForPrediction.sav'
           model = pickle.load(open(filename, 'rb'))

           prediction = model.predict([[pclass,age,SibSp,Parch,Fare,gender]])

           print('prediction value is ', prediction)
           # showing the prediction results in a UI
           return render_template('predict.html', prediction = prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

