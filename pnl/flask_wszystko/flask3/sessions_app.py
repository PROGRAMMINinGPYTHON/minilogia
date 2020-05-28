from flask import Flask, render_template, request, session
import sessions.SessionsDataSource as mds

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mojehsło'


@app.route("/Session_review")
def test_session():
    print("umieszczanie usera w sesji ")
    session['loggedUser'] = "TheHalynaPaniKsięgowa"
    session['imie'] = request.args.get("imieOsoby")
    session['nazwisko'] = request.args.get("nazwiskoOsoby")
  #  zwieksz_licznik()
    print("user logged to" + session['loggedUser'] + " " + session['imie'] + " " + session["nazwisko"] + " " )
    return "";


@app.route("/wyswietl")
def showProduct():
 #   zwieksz_licznik()
    id = request.args.get('id')
    imie = session["imie"]
    nazwisko = session["nazwisko"]
    p = mds.getOne(id)
    licznik = 2
 #   licznik = session['licznik']

    return render_template("showProduct.html", product=p, imie=imie, nazwisko=nazwisko, licznik=licznik)


def zwieksz_licznik():
    licznik = session['licznik']
    if (licznik == None):
        licznik = 0
    licznik = licznik + 1
    session['licznik'] = licznik


if __name__ == '__main__':
    app.run(debug=True, port=8080)
