import logging

# Configure the logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs/requests.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    """
    Middleware that logs request URL and response status code.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        response = self.get_response(request)
        
        # Log the request URL and response status code
        # logger.info(f"Request URL: {request.path}, Response Status: {response.status_code}")
        
        return response
