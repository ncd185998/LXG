# import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, apology_register

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/homepage")
@login_required
def homepage():

    # set session to know whos logged in
    user_id = session["user_id"]

    # set name
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    #information for keepers table
    keepers_db = db.execute("SELECT team, manager, keeper FROM keepers")

    """Show LXG Homepage"""
    return render_template("homepage.html", manager_name_real=manager_name_real, database=keepers_db)


@app.route("/members")
@login_required
def members():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show members page"""
    return render_template("members.html", manager_name_real = manager_name_real)

@app.route("/noah")
@login_required
def noah():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show noah page"""
    return render_template("members_noah.html", manager_name_real = manager_name_real)

@app.route("/angelo")
@login_required
def angelo():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show angelo page"""
    return render_template("members_angelo.html", manager_name_real = manager_name_real)

@app.route("/bobby")
@login_required
def bobby():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show bobby page"""
    return render_template("members_bobby.html", manager_name_real = manager_name_real)

@app.route("/jd")
@login_required
def jd():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show jd page"""
    return render_template("members_jd.html", manager_name_real = manager_name_real)

@app.route("/jeremy")
@login_required
def jeremy():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show jeremy page"""
    return render_template("members_jeremy.html", manager_name_real = manager_name_real)

@app.route("/jimmy")
@login_required
def jimmy():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show jimmy page"""
    return render_template("members_jimmy.html", manager_name_real = manager_name_real)

@app.route("/josh")
@login_required
def josh():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show josh page"""
    return render_template("members_josh.html", manager_name_real = manager_name_real)

@app.route("/mike")
@login_required
def mike():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show mike page"""
    return render_template("members_mike.html", manager_name_real = manager_name_real)

@app.route("/rj")
@login_required
def rj():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show rj page"""
    return render_template("members_rj.html", manager_name_real = manager_name_real)

@app.route("/roy")
@login_required
def roy():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """Show roy page"""
    return render_template("members_roy.html", manager_name_real = manager_name_real)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM managers WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/homepage")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/homepage")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # check for errors
        # ensure username was submitted
        if not request.form.get("manager"):
            return apology_register("must provide manager name", 400)

        # ensure username was submitted
        if not request.form.get("team"):
            return apology_register("must provide team name", 400)

        # ensure username was submitted
        if not request.form.get("username"):
            return apology_register("must provide username", 400)

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology_register("must provide password", 400)

         # ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology_register("must provide password confirmation", 400)

        # ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology_register("password and confirmation must match", 400)

        # insert new user into the users table of database/check for username already existing
        hash = generate_password_hash(request.form.get("password"))
        try:
            new_user = db.execute("INSERT INTO managers (manager, team, username, hash) VALUES (?, ?, ?, ?)", request.form.get("manager"), request.form.get("team"), request.form.get("username"), hash)
        except:
            return apology_register("username already exists", 400)

        # log user in
        session["user_id"] = new_user

        # return to homepage
        return redirect("/homepage")

    else:
        return render_template("register.html")



@app.route("/constitution")
@login_required
def constitution():
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    """display constitution"""
    return render_template("constitution.html", manager_name_real=manager_name_real)


@app.route("/amendments", methods=["GET", "POST"])
@login_required
def amendments():

    """display amendments page"""

    if request.method == "GET":
        # set session to know whos logged in
        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]


        #displaying amenendments table
        amendments_db = db.execute("SELECT number, manager, team, date, name, description, reason FROM amendments")

        return render_template("amendments.html", database=amendments_db, manager_name_real=manager_name_real)



    #post method for adding amenedments
    else:
        # error messages for any missing fields
        if not request.form.get("name"):
            return apology("must provide name of proposal", 400)

        if not request.form.get("description"):
            return apology("must provide detailed description of proposal", 400)

        if not request.form.get("reason"):
            return apology("must provide reason for submitting proposal", 400)

        # set user id
        user_id = session["user_id"]

        #set variables
        #manager/team
        manager_team = db.execute("SELECT manager, team FROM managers WHERE id = ?", user_id)
        manager = manager_team[0]["manager"]
        team = manager_team[0]["team"]

        #date
        date = datetime.datetime.now()

        #name
        name = request.form.get("name")

        #description
        description = request.form.get("description")

        #reason
        reason = request.form.get("reason")

        # insert the amendments into the table
        db.execute("INSERT INTO amendments (user_id, manager, team, date, name, description, reason) VALUES (?, ?, ?, ?, ?, ?, ?)", user_id, manager, team, date, name, description, reason)

        flash("Amendment Submitted!")

        return redirect("/amendments")


@app.route("/voting", methods=["GET", "POST"])
@login_required
def voting():

    """display voting page"""

    if request.method == "GET":
        # set session to know whos logged in
        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]

        #displaying amenendments table
        amendments_db = db.execute("SELECT number, name, description, reason FROM amendments")

        return render_template("voting.html", database=amendments_db, manager_name_real=manager_name_real)

    #post for voting
    else:
        # set user id
        user_id = session["user_id"]

        #set variables
        #number
        number = request.form.get("number")

        #vote
        vote = request.form.get("vote")

        #date
        date = datetime.datetime.now()

        #error messages for no inputs
        if not number:
            return apology("please insert amendment number", 400)

        if vote == "Select":
            return apology("please select vote from dropdown menu", 400)

        #name
        name = db.execute("SELECT name FROM amendments WHERE number = ?", number)
        name_real = name[0]["name"]

        #check for vote submission
        vote_sub = db.execute("SELECT vote FROM voting WHERE number = ? AND user_id = ?", number, user_id)

        if vote_sub:
            return apology("vote already submitted", 400)

        else:
            #insert the amendments into the table
            db.execute("INSERT INTO voting (user_id, number, vote, name, date) VALUES (?, ?, ?, ?, ?)", user_id, number, vote, name_real, date)

            flash("Vote Submitted!")

            return redirect("/voting")


@app.route("/votelog")
@login_required
def votelog():

    """display votelog page"""
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    #display vote log
    vote_log_db = db.execute("SELECT user_id, number, name, vote, date FROM voting")

    #yes/no counts
    vote_log_yn = db.execute("SELECT number, name FROM voting GROUP BY number")

    #numbers
    number = db.execute("SELECT number FROM voting GROUP BY number")
    number_real = number[0]["number"]

    #vote count
    vote_count_yes = db.execute("SELECT COUNT() as Count FROM voting WHERE vote = 'yes' AND number = ?", number_real)
    vote_count_no = db.execute("SELECT COUNT() as Count FROM voting WHERE vote = 'no' AND number = ?", number_real)


    if user_id == 1:
        return render_template("vote_log.html", manager_name_real = manager_name_real, database = vote_log_db, database1 = vote_log_yn, vote_count_yes = vote_count_yes, vote_count_no = vote_count_no)

    else:
        return apology("you do not have permission to view this page", 400)


@app.route("/history")
@login_required
def history():

    """display history page"""
    # set session to know whos logged in
    user_id = session["user_id"]
    manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
    manager_name_real = manager_name[0]["manager"]

    return render_template("history.html", manager_name_real=manager_name_real)

@app.route("/keeper", methods=["GET", "POST"])
@login_required
def keeper():

    """display keeper page"""
    # set session to know whos logged in
    if request.method == "POST":

        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]

        #set variables
        #keeper
        keeper = request.form.get("keeper")

        #keeper submitted or not
        keeper_present = db.execute("SELECT keeper FROM keepers WHERE id = ?", user_id)

        #manager/team
        id_manager_team = db.execute("SELECT id, manager, team FROM managers WHERE id = ?", user_id)
        manager = id_manager_team[0]["manager"]
        team = id_manager_team[0]["team"]
        id = id_manager_team[0]["id"]

        #error messager for missing fields
        if not request.form.get("keeper"):
            return apology("must provide keeper", 400)

        #initial submission
        if not keeper_present:
            db.execute("INSERT INTO keepers (keeper, manager, team, id) VALUES (?, ?, ?, ?)", keeper, manager, team, id)

            flash("Keeper Submitted!")

            return redirect("/keeper")

        #changing keeper
        if keeper_present:
            return apology("keeper already submitted. please follow 'change keeper' link", 400)



    #get method
    else:

        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]

        return render_template("keeper.html", manager_name_real=manager_name_real)



@app.route("/changekeeper", methods=["GET", "POST"])
@login_required
def changekeeper():

    """display changekeeper page"""
    # set session to know whos logged in
    if request.method == "POST":

        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]

        #set variables
        #keeper
        keeper = request.form.get("keeper")

        #keeper submitted or not
        keeper_present = db.execute("SELECT keeper FROM keepers WHERE id = ?", user_id)

        #manager/team
        id_manager_team = db.execute("SELECT id, manager, team FROM managers WHERE id = ?", user_id)
        manager = id_manager_team[0]["manager"]
        team = id_manager_team[0]["team"]
        id = id_manager_team[0]["id"]

        #error messager for missing fields
        if not request.form.get("keeper"):
            return apology("must provide keeper", 400)

        #initial submission
        if keeper_present:
            db.execute("UPDATE keepers SET keeper = ? WHERE id = ?",keeper, user_id)

            flash("Keeper Updated!")

            return redirect("/keeper")


    #get method
    else:

        user_id = session["user_id"]
        manager_name = db.execute("SELECT manager FROM managers WHERE id = ?", user_id)
        manager_name_real = manager_name[0]["manager"]

        return render_template("change_keeper.html", manager_name_real=manager_name_real)
