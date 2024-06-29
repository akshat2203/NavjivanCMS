from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import ClientProfileForm
from django.contrib.auth.views import LoginView


class SuperuserLoginView(LoginView):
    template_name = 'login.html'


class ClientDashboardView(TemplateView):
    template_name = "client-dashboard.html"


class ClientProfileCreateView(FormView):
    template_name = 'client-profile-form.html'
    form_class = ClientProfileForm
    success_url = reverse_lazy('client-dashboard')  # Replace 'success_url' with the actual URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
