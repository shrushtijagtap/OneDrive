from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensures only logged-in users can access this page
def home(request):
    return render(request, 'home.html')
