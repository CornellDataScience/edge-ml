from flask import flash, Flask, render_template, request, redirect, url_for
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from models import User

# load environment keys
load_dotenv()

# flask config
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Initialize the Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# non-auth user
login_manager.login_view = "login"
login_manager.login_message_category = "warning"

# mongo client, add IP to db on website
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)

# accessing db for login
db = client["auth"]
users = db.users


@login_manager.user_loader
def load_user(user_id):
    u = users.find_one({"email": user_id})
    if not u:
        return None
    return User(u["email"], u["password"])


# landing page
@app.route("/")
def home():
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return render_template("index.html")


# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve data from form
        email = request.form.get("email")
        password = request.form.get("password")

        # check if user exists
        user = users.find_one({"email": email})
        # check if user exists and pwd is correct
        if user and check_password_hash(user["password"], password):
            user_obj = User(user["email"], user["password"])
            login_user(user_obj)  # remember to call this to login the user
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username/password", "error")  # noti. indicator
            return redirect(url_for("login"))
    return render_template("login.html")


# register acc
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # get from html
        email = request.form["email"]
        password = request.form["password"]

        # check if user exists
        existing_user = users.find_one({"email": email})

        if existing_user is None:
            hashed_password = generate_password_hash(
                password, method="pbkdf2:sha256"
            )  # hash password with sha256
            # into db it goes hooray :D
            users.insert_one({"email": email, "password": hashed_password})
            return redirect(url_for("login"))
        else:
            flash("User already exists with this email address.", "warning")
            return redirect(url_for("register"))

    return render_template("register.html")


# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# protected pages
@app.route("/dashboard")
@login_required
def dashboard():
    # endpoints go here
    # some if check to make sure system is connected to nano (therefore online)
    systemStatus = "Online"
    isIndicator = False
    deviceName = "Edge Device #1"
    deviceID = "DEFAULT_EDGE_DEVICE_ID_1"
    return render_template(
        "dashboard.html",
        systemStatus=systemStatus,
        deviceName=deviceName,
        deviceID=deviceID,
        isIndicator=isIndicator,
    )


if __name__ == "__main__":
    app.run(debug=True)
