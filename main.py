from flask import Flask, render_template, request;
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mannus1234@HOST/DATABASE'
db = SQLAlchemy(app)

# Define db model
class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email_= db.Column(db.String(120), unique = True)
    username_ = db.Column(db.String(120))

def __init__(self,email_, username_):
    self.email_ = email_
    self.username_ = username_


@app.route("/")
def Hello():
    return render_template("checkout.html")



@app.route('/', methods=['POST'])

def thankyou():
    if request.method == 'POST':
      email =request.form["email"]
      username = request.form["Username"]
      print(request.form)
      data = Data(email,username)
      db.session.add(data)
      db.session.commit()
      return render_template('Thankyou.html')
if __name__ == "__main__":
     app.debug=True
     app.run()
