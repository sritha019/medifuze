from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import TestCategory, Test, Doctor, Appointment, Report, CustomUser
from .forms import BookTestForm, BookAppointmentForm, CustomUserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    return render(request, 'home.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def book_test(request):
    categories = TestCategory.objects.prefetch_related('test_set').all()
    if request.method == 'POST':
        form = BookTestForm(request.POST)
        if form.is_valid():
            test_id = form.cleaned_data['test_id']
            test = get_object_or_404(Test, id=test_id)
            # Send an email to the patient
            send_mail(
                'Test Booking Confirmation',
                f'You have successfully booked {test.name} for {test.price} CZK.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email]
            )
            return render(request, 'book_test_success.html', {'test': test})
    else:
        form = BookTestForm()
    return render(request, 'book_test.html', {'categories': categories, 'form': form})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            # Send an email to the patient
            send_mail(
                'Appointment Booking Confirmation',
                f'You have successfully booked an appointment with {appointment.doctor.name}.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email]
            )
            return render(request, 'book_appointment_success.html', {'appointment': appointment})
    else:
        form = BookAppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

@login_required
def download_report(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, 'download_report.html', {'reports': reports})

@login_required
def redirect_dashboard(request):
    user = request.user
    if user.user_type == 'doctor':
        return redirect('doctor_dashboard')
    elif user.user_type == 'patient':
        return redirect('patient_dashboard')
    elif user.user_type == 'agent':
        return redirect('agent_dashboard')
    elif user.user_type == 'technician':
        return redirect('technician_dashboard')
    return redirect('home')

@login_required
def doctor_dashboard(request):
    if request.method == 'POST' and request.FILES.get('prescription'):
        prescription = request.FILES['prescription']
        fs = FileSystemStorage()
        filename = fs.save(prescription.name, prescription)
        uploaded_file_url = fs.url(filename)
        return render(request, 'doctor_dashboard.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'doctor_dashboard.html')

@login_required
def agent_dashboard(request):
    appointments = Appointment.objects.select_related('user').all()
    return render(request, 'agent_dashboard.html', {'appointments': appointments})
