import pandas as pd
import numpy as np
import pickle
import json
import config

class Loan_data():
    

    def __init__(self,credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
    inq_last_6mths,delinq_2yrs,pub_rec,purpose):
        self.credit_policy = credit_policy
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths = inq_last_6mths
        self.delinq_2yrs =delinq_2yrs
        self.pub_rec = pub_rec
        self.purpose = purpose

    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
        #with open("Loan_model.pkl", "rb") as f:
            self.logistic_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
        #with open("Project_data_loan.json", "r") as f:
            self.json_data = json.load(f)

    def get_prediction(self):

        self.load_models()
        
        purpose = "purpose_" + self.purpose
        purpose_index = list(self.json_data["columns"]).index(purpose)

        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.credit_policy
        test_array[1] = self.int_rate
        test_array[2] = self.installment
        test_array[3] = self.log_annual_inc
        test_array[4] = self.dti
        test_array[5] = self.fico
        test_array[6] = self.days_with_cr_line
        test_array[7] = self.revol_bal
        test_array[8] = self.revol_util
        test_array[9] = self.inq_last_6mths
        test_array[10] = self.delinq_2yrs
        test_array[11] = self.pub_rec
        test_array[purpose_index] = 1

        prediction = self.logistic_model.predict([test_array])[0]
        print("Test Array is---->",test_array)
        if prediction == 0:
            return "Loan is Declined"
            
        else:
            return "Congrats Loan is Approved"

if __name__ == "__main__":
    credit_policy=1
    int_rate=0.089400
    installment=190.630000
    log_annual_inc=11.002100
    dti=2.860000
    fico =757
    days_with_cr_line=4830.041667
    revol_bal =7392
    revol_util =42.500000
    inq_last_6mths =0
    delinq_2yrs = 0
    pub_rec=0
    purpose="debt_consolidation"



    loan = Loan_data(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
    inq_last_6mths,delinq_2yrs,pub_rec,purpose)
    
    pred = loan.get_prediction()
    print("Prediction is -->",pred)