from flask import Flask, request, render_template
import json
import os
app = Flask(__name__)
def load_data():
    if os.path.exists('data.json'):
        with open('data.json','r') as f:
            data=json.load(f)
            return data
def write_data(d):
    with open('data.json','w') as n:
        json.dump(d,n) 
@app.route("/")
@app.route("/")
def home():
    data = load_data()

    name = request.args.get("name")
    rapist = request.args.get("rapist")

    if name is not None:
        data["name"] = name#type:ignore
        write_data(data)

    if rapist is not None:
        data["rapist"] = rapist#type:ignore
        write_data(data)

    return render_template(
        "game_page.html",
        name=data["name"],#type:ignore
        rapist=data["rapist"]#type:ignore
    )

if __name__ == "__main__":
    app.run(debug=True)