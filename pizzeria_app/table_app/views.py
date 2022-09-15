from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render, HttpResponse, \
    HttpResponseRedirect
from .models import booking
from .forms import booking_form, ContactForm
from django.template import loader
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "home.html")


def booking_options(request):
    return render(request, "booking_options.html")


def table_booking(request):
    form = booking_form()
    reference = booking.booking_reference

    if request.method == "POST":
        form = booking_form(request.POST)

        if not booking.objects.filter(booking_reference=reference).exists():
            if form.is_valid():
                try:
                    send_mail(
                        "Booking reference",
                        reference,
                        "alexander_daley@icloud.com",
                        ["alexander_daley@icloud.com"],
                    )
                except BadHeaderError:
                    return HttpResponse("Invalid header found.")
                form.save()
                return redirect("index")
        else:
            messages.success(
                request,
                "There is already a booking with that reference,\
                    try again with a new reference",
            )
            return redirect("table_booking")

    context = {"form": form}
    return render(request, "booking_form.html", context)


def booking_search_update(request):
    if request.GET.get("MyBtn"):
        return add_booking(request, request.GET.get("reference_search"))

    return render(request, "booking_search.html")


def booking_search_delete(request):
    if request.GET.get("MyBtn"):
        return delete_booking(request, request.GET.get("reference_search"))

    return render(request, "booking_search.html")


def add_booking(request, booking_reference):
    booking_details = booking.objects.get(booking_reference=booking_reference)
    template = loader.get_template("add_booking.html")
    context = {
        "booking": booking_details,
    }
    return HttpResponse(template.render(context, request))


def update_booking(request, booking_ref):
    booking_details = booking.objects.get(booking_reference=booking_ref)

    booking_details.first_name = request.POST["first_name"]
    booking_details.last_name = request.POST["last_name"]
    booking_details.booking_date = request.POST["booking_date"]
    booking_details.booking_ToD = request.POST["booking_ToD"]
    booking_details.number_of_guests = request.POST["number_of_guests"]
    booking_details.phone_number = request.POST["phone_number"]

    booking_details.save()

    context = {"booking": booking_details}

    return HttpResponseRedirect(reverse("index"), context)


def delete_booking(request, booking_ref):
    booking_details = booking.objects.filter(booking_reference=booking_ref)
    booking_details.delete()

    context = {"booking": booking_details}

    return HttpResponseRedirect(reverse("index"), context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "alexander_daley@icloud.com",
                    ["alexander_daley@icloud.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("index")

    form = ContactForm()
    return render(request, "contact_form.html", {"form": form})
