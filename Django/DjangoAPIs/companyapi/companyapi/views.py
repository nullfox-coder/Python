from django.http import HttpResponse
# function based view
def home_page(request):
    print("home page requested")
    return HttpResponse("This is home page")