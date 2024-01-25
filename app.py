import yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/warrior_iii_bedford")
def warrior_iii_bedford():
    with open('./data.yml', 'r') as f:
        data = yaml.safe_load(f)
    return render_template('warrior_iii_bedford/landscape.html.j2', data=data)


