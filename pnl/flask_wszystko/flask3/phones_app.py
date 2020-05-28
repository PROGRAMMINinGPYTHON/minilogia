from flask import Flask,render_template,request,session
import PhonesDataSource as mds

app = Flask(__name__)
app.config['SECRET_KET']='mypassword'

@app.route("/addPhone")
def addPhone():
    return render_template("addPhone.html")

@app.route("/addPhone",methods=['POST'])
def addPhonePost():
    name = request.form['nazwa']
    price= request.form['opis']
    print(f"name={name},opis = {price}")
    return render_template("addPhone.html")

@app.route("/testSession")
def testSession():
    print("umieszczanie usera w sesji")
    session['loggedUser']="ThePaniHalynaKsiegowa"
    print("user zalogowany to "+session['loggedUser'])
    return"";



@app.route('/')
def hello_phones():
    return 'x'

@app.route('/reviev')
def hello():
    nameA=["John","Poul","Marc"]
    return render_template("szablon.html",nameA=nameA, nameB="Poul",numberA= 7,numberB = 13)

@app.route("/phones")
def phones():
    print(mds.getAll())
    for p in mds.getAll():
        print("p: ", p.nr)
    return render_template("phones.html",phones=mds.getAll())

@app.route("/showPhones")
def showPhones():
    nr = request.args.get('nr')
    p = mds.getOne(nr)
    print(f'odczytanie nr={nr}')
    return render_template("showPhones.html",phone=p)

if __name__ == '__main__':
    app.run(debug=True,port=8080)