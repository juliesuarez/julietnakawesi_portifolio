from django.urls import path

from .views import index,about,skills,innovation,mentorship,contact,thank_you,interest

urlpatterns = [
    path("", index, name="home"),
    path("me/", about, name="me"),
    path("skills/", skills, name="skills"),
    path("innovation/", innovation, name="innovation"),
    path("mentorship/", mentorship, name="mentorship"),
    path("contact/", contact, name="contact"),
    path("thank_you/", thank_you, name="thank_you"),
    path("interest/", interest, name="interest"),
]
