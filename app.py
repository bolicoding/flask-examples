from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', name="Boli")

app.route("/slug/<id>")
def slug(id):
  return render_template('slug.html', id=id)


@app.route('/loops')
def loops():
  return render_template('loops.html', content=['cory', 'zac', 'boli', 'eva', 'dan'])



if __name__ == "__main__":
  app.run(debug=True)

