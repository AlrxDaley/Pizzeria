from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render , HttpResponse
from .models import booking
from .forms import booking_form, ContactForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

def booking_options(request):
    return render(request, 'booking_options.html')

def table_booking(request):
    
    form = booking_form()
    
    if request.method == 'POST':
        form = booking_form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {'form':form}
    return render(request, 'booking_form.html', context)

def update_booking(request, id):
    
    bookings = booking.objects.get(id = id)
    form = booking_form(instance=bookings)
        
    context = {'form':form}
    return render(request, 'booking_form.html', context)



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'subject': form.cleaned_data['subject'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'alexander_daley@icloud.com', ['alexander_daley@icloud.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("index")
      
	form = ContactForm()
	return render(request, "contact_form.html", {'form':form})