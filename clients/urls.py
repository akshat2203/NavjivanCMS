from django.urls import path
from .views import ClientProfileCreateView, ClientDashboardView, SuperuserLoginView


urlpatterns = [
    path('login/', SuperuserLoginView.as_view(), name='login'),
    path('', ClientDashboardView.as_view(), name='client-dashboard'),
    path('profile/', ClientProfileCreateView.as_view(), name='client-profile'),

]