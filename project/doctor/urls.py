


from django.urls import path
from . import views
from doctor.views import HomeTemplateView, AppointmentTemplateView,ManageAppointmentTemplateView


urlpatterns = [
path("",HomeTemplateView.as_view(), name="home"),
path("make-an-appointment/",AppointmentTemplateView.as_view(), name="appointment"),
path("manage-appointment/", ManageAppointmentTemplateView.as_view(),name="manage")
]
