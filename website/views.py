from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def ic(request):
	if request.method == "POST":
		inches = request.POST['inches']
		cent = int((int(inches) * 2.54))
		return render(request, 'ic.html', {
			'inches': inches,
			'cent': cent,
			})	
	else:
		return render(request, 'ic.html', {})	

def ci(request):
	if request.method == "POST":
		cm = request.POST['cm']
		inches = int((int(cm) / 2.54))
		return render(request, 'ci.html', {
			'cm': cm,
			'inches': inches,			
			})	
	else:
		return render(request, 'ci.html', {})	