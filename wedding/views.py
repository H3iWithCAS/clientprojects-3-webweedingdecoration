from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

def home(request):
    return render(request, 'home.html')

# Halaman login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('booking')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

# Halaman untuk registrasi
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('booking')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# View untuk logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Halaman booking (hanya bisa diakses setelah login)
@login_required
def booking(request):
    # Cek apakah pengguna sudah login
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect ke halaman login jika belum login

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        date = request.POST.get('date')

        # Simpan data booking baru
        Booking.objects.create(name=name, phone=phone, service=service, date=date)
        messages.success(request, 'Booking successful!')

        return redirect('list_bookings')  # Arahkan ke halaman daftar list_bookings setelah booking berhasil
    
    return render(request, 'booking.html')

def list_bookings(request):
    # Cek apakah pengguna sudah login
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect ke halaman login jika belum login

    # Ambil daftar booking yang terkait dengan pengguna
    bookings = Booking.objects.all()  # Anda bisa memfilter berdasarkan pengguna yang login jika diperlukan

    return render(request, 'list_bookings.html', {'bookings': bookings})

# Create Booking
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('list_bookings')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

# List all bookings
def list_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'list_bookings.html', {'bookings': bookings})

# Update Booking
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('list_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'update_booking.html', {'form': form})

# Delete Booking
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('list_bookings')
    return render(request, 'delete_booking.html', {'booking': booking})

def blog(request):
    return render(request, 'blog.html')

def layanan(request):
    return render(request, 'layanan.html')

def contact(request):
    return render(request, 'contact.html')