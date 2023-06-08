from flask import Flask, render_template, request

from project_app.utils import TitanicDataset

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("person servived in titanic")   
    return render_template("index.html")

@app.route("/predict_Person_servived", methods = ["POST", "GET"])

def diesese_info():

    if request.method == "GET":
        print("GET Method")

        Pclass = eval(request.args.get('Pclass'))
        Gender = request.args.get('Gender')
        Age = eval(request.args.get('Age'))
        SibSp = eval(request.args.get('SibSp'))
        Parch = eval(request.args.get('Parch'))
        Fare = eval(request.args.get('Fare'))
        Embarked = request.args.get('Embarked')

        Person_servived =  TitanicDataset(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)

        yes_no = Person_servived.get_predicted_person_servived()

        if yes_no == 1:
           print("person has been survived")
        else:
           print("sorry...! person may you search has been not survived")

        return render_template("index.html", prediction = yes_no)
    
if __name__ == "__main__":
    app.run()