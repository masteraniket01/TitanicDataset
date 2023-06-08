import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class  TitanicDataset():

    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):

        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp =  SibSp
        self.Parch = Parch
        self.Fare = Fare

        self.Embarked_col = 'Embarked_' + Embarked

    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.logistic_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.save_data  = json.load(f)

            self.column_names = np.array(self.save_data["columns"])


    def get_predicted_person_servived(self):
        self.load_models()

        Embarked_col_index = np.where(self.column_names == self.Embarked_col)[0][0]

        array = np.zeros(len(self.save_data['columns']))

        array[0] = self.Pclass
        array[1] = self.save_data["Gender"][self.Gender]
        array[2] = self.Age
        array[3] = self.SibSp
        array[4] = self.Parch
        array[5] = self.Fare 

        array[Embarked_col_index] = 1
        print("TESTING an Array -->\n", array)

        yes_no = self.logistic_model.predict([array])[0]

        return yes_no
    
if __name__ == "__main__":

    Pclass = 1.0
    Gender = 'male'
    Age = 35.0
    SibSp = 1.0	
    Parch = 0.0
    Fare = 53.1
    Embarked  = 'Q'

    Person_servived =  TitanicDataset(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)

    yes_no = Person_servived.get_predicted_person_servived()

    if yes_no == 1:
       print("person has been survived")
    else:
       print("sorry...! person may you search has been not survived")

        