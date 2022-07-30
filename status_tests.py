''' Unit Tests for methods in status.py '''

import unittest
from unittest import mock
import requests_mock
import status as status_functions


class TestStatusMethods(unittest.TestCase):

    def test_create_timestamp(self):
        ''' Test for create_timestamp method '''

        self.assertEqual(status_functions.create_timestamp(1659188594.206462), 1659188594)

    def test_calculate_duration_ms(self):
        ''' Test for calculate_duration_ms method '''

        self.assertEqual(status_functions.calculate_duration_ms(1659188881.6613538,1659188883.6613538),2000)

    def test_get_status(self):
        ''' Test of get_status method. Note that this uses mocking to replace the call to requests.get
            in get_response. Start/end time are set to the same at 1000, so duration is 0
            This simulates a valid response with a status code of 200 '''

        url = 'http://localhost/v1/amazon-status'

        # Mock get_time method to return a time of 1000 - note that this is used for both the
        # start and end times.
        with mock.patch('status.get_time', return_value=1000):
            with requests_mock.Mocker() as mock_request:
                mock_request.get(url, status_code=200)

                expected_value = {
                    'url': url,
                    'statusCode': 200,
                    'duration': 0,
                    'date': 1000
                }

                self.assertDictEqual(status_functions.get_status(url), expected_value)


if __name__ == '__main__':
    unittest.main()