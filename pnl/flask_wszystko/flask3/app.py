from flask import Flask, render_template, request, session
import MyDataSource as mds

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mojehasło'


@app.route("/testSession")
def testSession():
    print("umieszczanie uższkodnika w sesji")
    session['loggesUser'] = "ThePaniHalynaKsięgowa"
    print("użytkownik zalogowany to " + session['loggedUser'])
    return "";


@app.route("/products")
def products():
    return render_template("products.html", products=mds.getAll())


@app.route("/showProduct")
def showProduct():
    id = request.args.get('id')
    imie = request.args.get('imie')
    p = mds.getOne(id)
    return render_template("showProduct.html", product=p, imie=imie)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/hello")
def hello_template():
    return render_template("hello.html", name="Staszek", surname="RODO", age="12", hobby="cars,python")


@app.route("/countries")
def hello_world_next():
    tab = ["polska", "anglia", "rosja", "niemcy", "czechy", "francja", "włochy", "szwecja", "litwa", "austria"]
    return render_template("countries.html", countries_in_europe=tab)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
