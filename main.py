''' Sun Life/Maxwell Health Take-Home Exercise
    Dave Bilotta (davebilotta@gmail.com)

    Back end code containing the following endpoints:
        /v1/amazon-status: Returns status of Amazon.
        /v1/google-status: Returns status of Google
        /v1/all-status: Returns status of both Amazon and Google

'''

from flask import Flask, json
from flask_cors import CORS, cross_origin
import status as status_functions

app = Flask(__name__)
CORS(app)


# ----- Endpoints -----
@app.route('/v1/amazon-status')
def amazon_status():
    ''' Endpoint to get status of Amazon. Returns data in format:
        {
            "url": "https://www.amazon.com",
            "statusCode: Status code of response,
            "duration": Elapsed duration of request in milliseconds
            "time": Timestamp of current date/time (note that this uses
                    the *end* time after response is received)
        }
    '''
    return json.dumps(status_functions.get_status("https://www.amazon.com"))


@app.route('/v1/google-status')
def google_status():
    ''' Endpoint to get status of Google. Returns data in format:
        {
            "url": "https://www.google.com",
            "statusCode: Status code of response,
            "duration": Elapsed duration of request in milliseconds
            "time": Timestamp of current date/time (note that this uses
                    the *end* time after response is received)
        }
    '''
    return json.dumps(status_functions.get_status("https://www.google.com"))


@app.route('/v1/all-status')
def all_status():
    ''' Endpoint to get status of both Amazon and Google. Returns data in format:
        [
            {
                "url": "https://www.google.com",
                "statusCode: Status code of response,
                "duration": Elapsed duration of request in milliseconds
                "time": Timestamp of current date/time (note that this uses
                        the *end* time after response is received)
        },
        {
                "url": "https://www.google.com",
                "statusCode: Status code of response,
                "duration": Elapsed duration of request in milliseconds
                "time": Timestamp of current date/time (note that this uses
                        the *end* time after response is received)
        }
        ]
    '''

    return json.dumps([
        status_functions.get_status("https://www.amazon.com"),
        status_functions.get_status("https://www.google.com")
    ])
