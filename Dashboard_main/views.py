from django.shortcuts import render

# Create your views here.
def dashboard_main(request):
    return render(request, 'dashboard_main.html')