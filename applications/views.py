from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import JobApplication
from .forms import UserRegisterForm, JobApplicationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('application_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = 'applications/application_list.html'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class JobApplicationDetailView(LoginRequiredMixin, DetailView):
    model = JobApplication
    template_name = 'applications/application_detail.html'

class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'applications/application_form.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Job application added successfully!')
        return super().form_valid(form)

class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'applications/application_form.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        messages.success(self.request, 'Job application updated successfully!')
        return super().form_valid(form)

class JobApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    template_name = 'applications/application_confirm_delete.html'
    success_url = reverse_lazy('application_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Job application deleted successfully!')
        return super().delete(request, *args, **kwargs)