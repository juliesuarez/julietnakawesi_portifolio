from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def skills(request):
    return render(request, "skills.html")


def innovation(request):
    return render(request, "innovation.html")


def mentorship(request):
    return render(request, "mentorship.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def thank_you(request):
    return render(request, 'message.html')

def interest(request):
    return render(request, 'interest.html')

def my_view(request):
    admin_url = reverse('admin:index')
    return redirect(admin_url)
