from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)


@app.route('/')
def index():

    return render_template("create.html")



@app.route('/create_user', methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/all_users')

@app.route('/all_users')
def all_user():
    users = User.get_all()
   

    return render_template('read.html', all_users = users)





if __name__ == "__main__":
    app.run(debug=True)
