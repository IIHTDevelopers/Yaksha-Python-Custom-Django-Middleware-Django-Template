from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Task
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse
import re


class RequestLoggingFunctionalTest(TestCase):
    
    def test_logging_request_url_and_status(self):
        """Test if the middleware logs the request URL and response status code correctly"""
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse('home'))
            log_exists = self._check_log("/home")
            if log_exists:
                test_obj.yakshaAssert("TestLoggingRequestURLAndStatus", True, "functional")
                print("TestLoggingRequestURLAndStatus = Passed")
            else:
                test_obj.yakshaAssert("TestLoggingRequestURLAndStatus", False, "functional")
                print("TestLoggingRequestURLAndStatus = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestLoggingRequestURLAndStatus", False, "functional")
            print("TestLoggingRequestURLAndStatus = Failed")
    

    def _check_log(self, log_message):
        """Check if the log message exists in the log file"""
        with open('logs/requests.log', 'r') as file:
            logs = file.readlines()

        for log in logs:
            if log_message in log:
                return True

        return False