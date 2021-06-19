from flask import Flask, render_template, request, redirect

app = Flask("ByeognhoScrapper")

@app.route("/")
def home():
  return render_template("1.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
  else:
    return redirect("/")
  return render_template("2.html", searchingBy=word)


app.run() 