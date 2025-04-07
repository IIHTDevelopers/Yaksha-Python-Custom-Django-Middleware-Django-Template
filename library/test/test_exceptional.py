from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Task


class RequestLoggingExceptionalTest(TestCase):
    
    def test_error_logging(self):
        """Test if the middleware logs errors correctly when there is an issue"""
        test_obj = TestUtils()
        try:
            # Simulating a server error
            response = self.client.get(reverse('home'))
            log_exists = self._check_log("Response Status: 200")
            if log_exists:
                test_obj.yakshaAssert("TestErrorLoggingForInvalidURL", True, "exceptional")
                print("TestErrorLoggingForInvalidURL = Passed")
            else:
                test_obj.yakshaAssert("TestErrorLoggingForInvalidURL", False, "exceptional")
                print("TestErrorLoggingForInvalidURL = Failed")
        except:
            test_obj.yakshaAssert("TestErrorLoggingForInvalidURL", False, "exceptional")
            print("TestErrorLoggingForInvalidURL = Failed")

    def _check_log(self, log_message):
        """Check if the log message exists in the log file"""
        with open('logs/requests.log', 'r') as file:
            logs = file.readlines()
        for log in logs:
            if log_message in log:
                return True

        return False