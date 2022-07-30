''' Sun Life/Maxwell Health Take-Home Exercise
    Dave Bilotta (davebilotta@gmail.com)

    Back end code containing the following endpoints:
        /v1/amazon-status: Returns status of Amazon.
        /v1/google-status: Returns status of Google
        /v1/all-status: Returns status of both Amazon and Google

'''

from flask import Flask, json
from flask_cors import CORS, cross_origin
import time
import requests

REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,it;q=0.8,mt;q=0.7"
}

app = Flask(__name__)
CORS(app)

# ----- Miscellaneous methods -----
def create_timestamp(time):
    ''' Given a time (number of seconds), return timestamp value '''

    return round(time)


def calculate_duration_ms(start_time, end_time):
    ''' Given start and end times, return a duration in milliseconds '''

    return round((end_time - start_time) * 1000)


def get_status(url):
    ''' Gets a Status for a given URL
        Returns dictionary of:
        {
            "url": "ex: https://www.amazon.com,
            "statusCode: Status code of response,
            "duration": Elapsed duration of request in milliseconds
            "time": Timestamp of current date/time (note that this uses
                    the *end* time after response is received)
        }
    '''

    # Store start time, make request and store end time
    start_time = time.time()
    response = requests.get(url, headers=REQUEST_HEADER)
    end_time = time.time()

    return {
        "url": url,
        "statusCode": response.status_code,
        "duration":  calculate_duration_ms(start_time, end_time),
        "date": create_timestamp(end_time)
    }


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
    return json.dumps(get_status("https://www.amazon.com"))


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
    return json.dumps(get_status("https://www.google.com"))


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
        get_status("https://www.amazon.com"),
        get_status("https://www.google.com")
    ])
