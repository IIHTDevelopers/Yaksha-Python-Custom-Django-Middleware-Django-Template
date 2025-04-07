from django.http import HttpResponse

# View to simulate a successful response
def home_view(request):
    return HttpResponse("Welcome to the homepage!")

# View to simulate another request (e.g., an about page)
def about_view(request):
    return HttpResponse("This is the about page.")

# View to simulate an error (will log 404 status code)
def error_view(request):
    return HttpResponse("Page not found", status=404)
