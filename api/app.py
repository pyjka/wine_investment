from flask import Flask, jsonify, request
from service.models import Country, Region, Wine, database
import os
app = Flask(__name__)

regions_warp = {2: "Bordeaux Premier Cru - left bank", 3:"Bordeaux Margaux, France",
                5: "Bordeaux Pessac-Léognan/ Graves", 6: "Bordeaux St Emilion- right bank",
                7: "Bordeaux Pomerols - right bank"}

regions_wanm = {}
@app.route('/warp', methods=["GET"])
def warp_view():
    data = database(os.getenv('DATABASE_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_warp[wine.region_id],
                       "wine_country": regions_warp[wine.country_id]})
    return jsonify(output)

@app.route('/wanm', methods=["GET"])
def wanm_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_RED_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

@app.route('/walpb', methods=["GET"])
def walpb_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_OLIVE_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

@app.route('/wajs', methods=["GET"])
def wajs_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_BLUE_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

if __name__ == '__main__':
    app.run(threaded=True, port=1337)
