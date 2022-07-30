import requests
import time


REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,it;q=0.8,mt;q=0.7"
}

def create_timestamp(time):
    ''' Given a time (number of seconds), return timestamp value '''

    return round(time)


def calculate_duration_ms(start_time, end_time):
    ''' Given start and end times, return a duration in milliseconds '''

    return round((end_time - start_time) * 1000)


def get_time():
    ''' Gets the current time. '''
    return time.time()


def get_response(url):
    ''' For a given URL, make a request and return the response '''
    return requests.get(url, headers=REQUEST_HEADER)


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
    start_time = get_time()
    response = get_response(url)
    end_time = get_time()

    return {
        "url": url,
        "statusCode": response.status_code,
        "duration":  calculate_duration_ms(start_time, end_time),
        "date": create_timestamp(end_time)
    }
