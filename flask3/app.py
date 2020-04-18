from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/hello")
def hello_template():
    return render_template("hello.html",name="Staszek",surname="RODO",age="12",hobby="cars,python")

@app.route("/countries")
def hello_world_next():
    tab=["polska", "anglia", "rosja", "niemcy", "czechy", "francja", "włochy", "szwecja", "litwa", "austria"]
    return render_template("countries.html",countries_in_europe=tab)



if __name__ == '__main__':
    app.run(debug=True,port=8080)