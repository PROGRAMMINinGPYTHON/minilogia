from flask import Flask

app = Flask(__name__)

data={
    "name":"Grzegorz",
    "surname":"Pierdoła",
    "age":"18",
    "hobby":"smoking weed"
}
@app.route("/data.json")
def getAlljson():
    return data

if __name__ == "__main__":
    app.run(debug=True,port=5000)