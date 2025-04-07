from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from library.models import Task


class RequestLoggingBoundaryTest(TestCase):
    
    def test_boundary_case(self):
        """Test logging when request URL has maximum length"""
        test_obj = TestUtils()
        try:
            url = '/home/' + 'a' * 500  # Long URL for boundary testing
            response = self.client.get(url)
            log_exists = self._check_log(f"Response Status: 404")
            if log_exists:
                test_obj.yakshaAssert("TestLoggingLongURLBoundary", True, "boundary")
                print("TestLoggingLongURLBoundary = Passed")
            else:
                test_obj.yakshaAssert("TestLoggingLongURLBoundary", False, "boundary")
                print("TestLoggingLongURLBoundary = Failed")
        except:
            test_obj.yakshaAssert("TestLoggingLongURLBoundary", False, "boundary")
            print("TestLoggingLongURLBoundary = Failed")


    def _check_log(self, log_message):
        """Check if the log message exists in the log file"""
        with open('logs/requests.log', 'r') as file:
            logs = file.readlines()

        for log in logs:
            if log_message in log:
                return True

        return False