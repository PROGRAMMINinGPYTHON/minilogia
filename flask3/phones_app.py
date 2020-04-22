from flask import Flask,render_template
import PhonesDataSource as mds

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True,port=8080)