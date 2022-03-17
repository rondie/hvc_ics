from io import BytesIO

from app.get_data import get_hvc_data
from app.make_ics import make_ics

from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return render_template("data.html")
    if request.method == "POST":
        postalcode = request.form['Postal Code']
        streetnumber = request.form['Streetnumber']
        ophaaldata = get_hvc_data(postalcode, streetnumber)
        return render_template("data.html", **locals())


@app.route('/hvc-<postalcode>-<streetnumber>.ics')
def calendar(postalcode, streetnumber):
    ophaaldata = get_hvc_data(postalcode, streetnumber)
    file = BytesIO(make_ics(ophaaldata))
    return send_file(
        file,
        attachment_filename='hvc-' + postalcode + '-' + streetnumber + '.ics',
        as_attachment=True)
    file.close
