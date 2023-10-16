from flask import Flask,render_template,request
import sqlite3
#import webview
import os
import traceback
import sys

###################################################################################################################################################
# System Database Section #
###################################################################################################################################################

db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
cr = db.cursor()
cr.execute(f"CREATE TABLE IF NOT EXISTS Emploees(Name TEXT , Id INTEGER , Address TEXT, Mobile INTEGER , Email TEXT , Gender TEXT , MStatuts TEXT , Salary INTEGER , BirthDay DATE , VactionNum INTEGER , AVactionNum INTEGER)")

cr.execute(f"CREATE TABLE IF NOT EXISTS HRs(Name TEXT , Id INTEGER , Address TEXT, Mobile INTEGER , Email TEXT , Gender TEXT , MStatuts TEXT , Salary INTEGER , BirthDay DATE , VactionNum INTEGER , AVactionNum INTEGER)")

cr.execute(f"CREATE TABLE IF NOT EXISTS Vactions(Name TEXT , Id INTEGER , Reason TEXT, StartDate DATE , EndDate DATE , HRStatus TEXT , MStatus TEXT )")

###################################################################################################################################################
# Applaction Section #
###################################################################################################################################################

app = Flask(__name__)

###################################################################################################################################################
# Pages Setion #
###################################################################################################################################################
@app.route('/') 
def Home():
    return render_template('Home.html', title = "Home Page")

@app.route('/HRHome') 
def HRHome():
    return render_template('HHome.html', title = "HR Home Page")

@app.route('/MHome') 
def MHome():
    return render_template('MHome.html', title = "M Home Page")

@app.route('/ShowHRS') 
def ShowHRS():
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM HRs")
    Data = [list(tup) for tup in cur.fetchall()]
    con.close()
    return render_template('Show HRS.html' , Data = Data, title = "Show HRS Page")

@app.route('/ShowEmplyooes') 
def ShowEmplyooes():
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Emploees")
    Data = [list(tup) for tup in cur.fetchall()]
    con.close()
    return render_template('Show Employees.html' , Data = Data, title = "Show Employees Page")

@app.route('/LogIn') 
def LogIn():
    return render_template('Log in.html', title = "Log In Page")

@app.route('/InsertEmployee' , methods=['GET', 'POST']) 
def InsertEmployee():
    if request.method == "POST":
        try:
            UserName = request.form.get("UserName")
            Address = request.form.get("Address")
            Mobile = request.form.get("Mobile")
            Email = request.form.get("Email")
            Salary = request.form.get("Salary")
            BirthDay = request.form.get("BirthDay")
            MSatuts = request.form.get("MSatuts")
            Gender = request.form.get("Gender")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute("SELECT Id FROM Emploees")
                Id = len(cur.fetchall())
                cur.execute(f"INSERT INTO Emploees VALUES('{UserName}' , {Id} , '{Address}' , {Mobile} , '{Email}' , '{Gender}' , '{MSatuts}' , {Salary} , '{BirthDay}' , 0 , 6)")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            con.close()
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT Id FROM Emploees")
    Id = len(cur.fetchall())
    con.close()
    return render_template('Add Employee.html', title = "Add Employee Page" ,  Id = f"{Id}" )

@app.route('/RemoveEmployee' , methods=['GET', 'POST']) 
def RemoveEmployee():
    if request.method == "POST":
        try:
            Id = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM Emploees WHERE Id = {Id}")
                cur.execute(f"UPADTE Emploees SET Id = Id-1 WHERE Id > {Id}")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    return render_template('Remove Employee.html', title = "Remove Employee Page")

@app.route('/ModifyEmployee' , methods=['GET', 'POST']) 
def ModifyEmployee():
    if request.method == "POST":
        try:
            UserName = request.form.get("UserName")
            Address = request.form.get("Address")
            Mobile = request.form.get("Mobile")
            Email = request.form.get("Email")
            Salary = request.form.get("Salary")
            BirthDay = request.form.get("BirthDay")
            MSatuts = request.form.get("MSatuts")
            Gender = request.form.get("Gender")
            Id = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if UserName:
                    cur.execute(f"UPDATE Emploees SET Name ='{UserName}' WHERE Id = {Id}")
                if Address:
                    cur.execute(f"UPDATE Emploees SET Address ='{Address}' WHERE Id = {Id}")
                if Mobile:
                    cur.execute(f"UPDATE Emploees SET Mobile ={Mobile} WHERE Id = {Id}")
                if Email:
                    cur.execute(f"UPDATE Emploees SET Email ='{Email}' WHERE Id = {Id}")
                if BirthDay:
                    cur.execute(f"UPDATE Emploees SET BirthDay ='{BirthDay}' WHERE Id = {Id}")
                if MSatuts:
                    cur.execute(f"UPDATE Emploees SET MStatuts ='{MSatuts}' WHERE Id = {Id}")
                if Gender:
                    cur.execute(f"UPDATE Emploees SET Gender ='{Gender}' WHERE Id = {Id}")
                if Salary:
                    cur.execute(f"UPDATE Emploees SET Salary ={Salary} WHERE Id = {Id}")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    return render_template('Modify Employee.html', title = "Modify Employee Page")

@app.route('/SubmitVaction' , methods=['GET', 'POST']) 
def SubmitVaction():
    if request.method == "POST":
        try:
            Id = request.form.get("Id")
            StartDate = request.form.get("StartDate")
            EndDate = request.form.get("EndDate")
            Reason = request.form.get("Reason")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Name FROM Emploees WHERE Id = {Id}")
                UserName= cur.fetchone()[0]
                cur.execute(f"INSERT INTO Vactions(Name, Id, Reason, StartDate, EndDate , HRStatus) VALUES('{UserName}' , {Id} , '{Reason}' , '{StartDate}' , '{EndDate}' , 'Panding')")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    return render_template('Submit Vaction.html', title = "Submit Vaction Page")

@app.route('/HShowVactions') 
def HShowVactions():
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Vactions")
    Data = [list(tup) for tup in cur.fetchall()]
    con.close()
    return render_template('H Show Vactions.html', Data = Data , title = "H Show Vactions")

@app.route('/ForgetPassword') 
def ForgetPassword():
    return render_template('Forget Password.html', title = "Forget Password Page")

@app.route('/InsertHR' , methods=['GET', 'POST']) 
def InsertHR():
    if request.method == "POST":
        try:
            UserName = request.form.get("UserName")
            Address = request.form.get("Address")
            Mobile = request.form.get("Mobile")
            Email = request.form.get("Email")
            Salary = request.form.get("Salary")
            BirthDay = request.form.get("BirthDay")
            MSatuts = request.form.get("MSatuts")
            Gender = request.form.get("Gender")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute("SELECT Id FROM HRs")
                Id = len(cur.fetchall())
                cur.execute(f"INSERT INTO HRs VALUES('{UserName}' , {Id} , '{Address}' , {Mobile} , '{Email}' , '{Gender}' , '{MSatuts}' , {Salary} , '{BirthDay}' , 0 , 6)")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT Id FROM HRs")
    Id = len(cur.fetchall())
    con.close()
    return render_template('Add HR.html', title = "Add HR Page" ,  Id = f"{Id}" )

@app.route('/RemoveHR' , methods=['GET', 'POST']) 
def RemoveHR():
    if request.method == "POST":
        try:
            Id = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM HRs WHERE Id = {Id}")
                cur.execute(f"UPADTE HRs SET Id = Id-1 WHERE Id > {Id}")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    return render_template('Remove HR.html', title = "Remove HR Page")

@app.route('/ModifyHR' , methods=['GET', 'POST']) 
def ModifyHR():
    if request.method == "POST":
        try:
            UserName = request.form.get("UserName")
            Address = request.form.get("Address")
            Mobile = request.form.get("Mobile")
            Email = request.form.get("Email")
            Salary = request.form.get("Salary")
            BirthDay = request.form.get("BirthDay")
            MSatuts = request.form.get("MSatuts")
            Gender = request.form.get("Gender")
            Id = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if UserName:
                    cur.execute(f"UPDATE HRs SET Name ='{UserName}' WHERE Id = {Id}")
                if Address:
                    cur.execute(f"UPDATE HRs SET Address ='{Address}' WHERE Id = {Id}")
                if Mobile:
                    cur.execute(f"UPDATE HRs SET Mobile ={Mobile} WHERE Id = {Id}")
                if Email:
                    cur.execute(f"UPDATE HRs SET Email ='{Email}' WHERE Id = {Id}")
                if BirthDay:
                    cur.execute(f"UPDATE HRs SET BirthDay ='{BirthDay}' WHERE Id = {Id}")
                if MSatuts:
                    cur.execute(f"UPDATE HRs SET MStatuts ='{MSatuts}' WHERE Id = {Id}")
                if Gender:
                    cur.execute(f"UPDATE HRsHRs SET Gender ='{Gender}' WHERE Id = {Id}")
                if Salary:
                    cur.execute(f"UPDATE HRs SET Salary ={Salary} WHERE Id = {Id}")
                con.commit()
        except sqlite3.Error as er:
            print( f"Sorry Have Error Is: {er}")
        finally:
            con.close()
    return render_template('Modify HR.html', title = "Modify HR Page")

@app.route('/MShowVactions') 
def MShowVactions():
    con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Vactions")
    Data = [list(tup) for tup in cur.fetchall()]
    con.close()
    return render_template('M Show Vaction.html', Data = Data , title = "M Show Vactions")

###################################################################################################################################################
# Running Setion #
###################################################################################################################################################

if __name__  == "__main__":
    app.run()