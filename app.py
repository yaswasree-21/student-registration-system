import mysql.connector
from flask import Flask , render_template,request 

app = Flask(__name__)

db = mysql.connector.connect(host="Localhost",
                             user="root",
                             password="22f61a47I3",
                             database="registrationdb")
cursor = db.cursor()


@app.route('/')
def home():
    return render_template("form.html")

@app.route("/share",methods=['POST'])

def senddata():
    fname=request.form.get("First name")
    lname=request.form.get("Last name")
    roll=request.form.get("Roll number")
    email=request.form.get("EMail")
    phone=request.form.get("Phone number")
    college=request.form.get("College name")
    dept=request.form.get("Department")
    skills=request.form.getlist("Skills")
    if not skills:
        skills=["None"]
        breakpoint()
    comments=request.form.get("comments")
    skills=",".join(skills)
    sql =  """INSERT INTO registration (fname, lname, roll_no, email, phone_no, college, dept,skills, comments)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (fname,lname,roll,email,phone,college,dept,skills,comments)
    cursor.execute(sql,values)
    db.commit()

    return render_template("stored.html")
    #return render_template ("result.html",fname=fname,lname=lname,roll=roll,email=email,phone=phone,college=college,
                          # dept=dept,skills=skills,comments=comments)

if __name__=='__main__':
    app.run(debug=True)