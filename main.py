from flask import Flask, jsonify, render_template, request

from project_app.utils import Loan_data

app = Flask(__name__)

@app.route("/") 
def hello_Patient():
    print("Welcome to Loan Approval Status")   
    return render_template("index.html")

@app.route("/predict_loan_status", methods = ["POST", "GET"])
def get_prediction_loan():
    if request.method == "GET":
        print("We are in a GET Method")

        credit_policy=eval(request.args.get("credit_policy"))
        int_rate=eval(request.args.get("int_rate"))
        installment=eval(request.args.get("installment"))
        log_annual_inc=eval(request.args.get("log_annual_inc"))
        dti=eval(request.args.get("dti"))
        fico =eval(request.args.get("fico"))
        days_with_cr_line=eval(request.args.get("days_with_cr_line"))
        revol_bal =eval(request.args.get("revol_bal"))
        revol_util =eval(request.args.get("revol_util"))
        inq_last_6mths =eval(request.args.get("inq_last_6mths"))
        delinq_2yrs = eval(request.args.get("delinq_2yrs"))
        pub_rec=eval(request.args.get("pub_rec"))
        purpose=request.args.get("purpose")


        loan = Loan_data(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,
        inq_last_6mths,delinq_2yrs,pub_rec,purpose)
    
        pred = loan.get_prediction()

        return render_template("index.html",prediction=pred)
    
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)