from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///login.db"
db = SQLAlchemy(app)

#class for making profile object
class profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        Name = request.form["username"]
        Password = request.form["password"]
        print("hello1")
        if db.session.query(profile).filter_by(username=Name, password=Password).all():
        
            print("hello2")
        
            return render_template("user.html", user=Name)
        else:
            return render_template("login.html")

    else:
        return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
       
        newName = request.form["username"]
        newPassword = request.form["password"]
        newProfile = profile( username=newName, password=newPassword)
        db.session.add(newProfile)
        db.session.commit()
        return redirect("/")
    return render_template("signup.html")


##creating DB and running app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)