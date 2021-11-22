import flask
from flask import request
import pandas as pd

df = pd.read_csv('gdp_db.csv', sep=';')


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    codigo_pais = request.args['codigo_pais']
    try:
        df_response = df[df['codigo_pais']==codigo_pais]
        json_response =  df_response.to_json(orient='records', lines=True)
        return json_response
    except KeyError:
        return "Erro!"