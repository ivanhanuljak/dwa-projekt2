from flask import Flask, Response, jsonify, request
from domain import Igraci, Timovi, Bodovi_igraca_,Rezultati_timova
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/igraci', methods=['GET', 'POST'])
def handle_igraci():
    if request.method == 'GET':
        igraci = Igraci.listaj()
        return jsonify({"igraci": igraci})
    elif request.method == 'POST':
        status, greske = Igraci.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/igrac/<id>', methods=['DELETE'])
def handle_igrac_delete(id):
    if request.method == 'DELETE':
        status,greske = Igraci.delete(id)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/timovi', methods=['GET', 'POST','PUT'])
def handle_timovi():
    if request.method == 'GET':
        timovi = Timovi.listaj()
        return jsonify({"timovi": timovi})
    elif request.method == 'PUT':
        status, greske = Timovi.update(request.get_json())
    elif request.method == 'POST':
        status, greske = Timovi.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/tim/<id>', methods=['DELETE'])
def handle_tim_delete(id):
    if request.method == 'DELETE':
        status,greske = Timovi.delete(id)
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


@app.route('/bodovi_igraca', methods=['GET', 'POST','PUT'])
def handle_bodove():
    print(request.get_json())
    if request.method == 'GET':
        print('TU SAM PRIJEEEEEE')
        bodovi_igraca = Bodovi_igraca_.listaj()
        print('okeej')
        return jsonify({"bodovi_igraca": bodovi_igraca})
    elif request.method == 'PUT':
        status, greske = Bodovi_igraca_.update(request.get_json())
    elif request.method == 'POST':
        status, greske = Bodovi_igraca_.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


@app.route('/rezultati_timova', methods=['GET', 'POST','PUT'])
def handle_rezultate():
    if request.method == 'GET':
        rezultati_timova = Rezultati_timova.listaj()
        return jsonify({"rezultati_timova": rezultati_timova})
    elif request.method == 'PUT':
        status, greske = Rezultati_timova.update(request.get_json())
    elif request.method == 'POST':
        status, greske = Rezultati_timova.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


if __name__ == '__main__':
    app.debug = True
    app.run()
