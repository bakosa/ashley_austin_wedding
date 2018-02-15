from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request, 'home/index.html', {})

def venue_view(request):
	return render(request, 'home/venue.html', {})

def about_view(request):
	return render(request, 'home/about_us.html', {})

