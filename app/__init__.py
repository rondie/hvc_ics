from io import BytesIO

from flask import Flask, send_file

from hvc_ics.get_data import get_data
from hvc_ics.make_ics import make_ics


app = Flask(__name__)


@app.route('/hvc-<postalcode>-<streetnumber>.ics')
def calendar(postalcode, streetnumber):
    ophaaldata = get_data(postalcode, streetnumber)
    file = BytesIO(make_ics(ophaaldata))
    return send_file(
        file,
        attachment_filename='hvc-' + postalcode + '-' + streetnumber + '.ics',
        as_attachment=True)
    file.close
