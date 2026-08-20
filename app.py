from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "jessica")
    Rname = request.args.get("rapist", "tickles")
    return render_template("game_page.html",name=name,rapist=Rname)

if __name__ == "__main__":
    app.run(debug=True)