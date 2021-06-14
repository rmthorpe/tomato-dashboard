from flask import Flask, request, make_response, render_template, jsonify
from utils import checkDate, initDate, getTomato, incTomato
from helper import getDateStr
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.datetime.now()
    day = today.day
    month = today.month
    year = today.year
    dateStr = str(month) + "/" + str(day) + "/" + str(year)
    tomato = None
    if checkDate(dateStr):
        initDate(dateStr)
    tomato = getTomato(dateStr)
    return make_response(render_template("index.html", 
                                          month=month, 
                                              day=day, 
                                            year=year, 
                                        tomato=tomato))

@app.route('/tomInc', methods=["POST"])
def tomInc():
    response = jsonify(success=True)
    ct = incTomato(getDateStr())
    return jsonify({"count": str(ct)})

if __name__=='__main__':
    app.run(host='localhost', port=12345, debug=True)