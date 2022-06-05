from django.shortcuts import redirect, render
from .models import Hospital,Specialization,Doctor,Appointment
from django.contrib import messages
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/AboutUs.html')



def main(request):
    # get details from hospital table
    hospitals = Hospital.objects.all()
    # filter s_name from specialization tables
    drop_spec=Specialization.objects.values_list('s_name',flat=True).distinct()
    drop_location=Hospital.objects.values_list('district',flat=True).distinct()

    context={
        'hospitals': hospitals,
        'drop_spec':drop_spec,
        'drop_location':drop_location
    }
    return render(request, 'home/hospital.html', context)


def hospital(request):

    if request.method == 'POST':
        location=request.POST['location']
        spec=request.POST['spec']
        request.session['location']=location
        request.session['spec']=spec
        specilization=Doctor.objects.filter(s_name__s_name=spec,h_name__district=location).values_list('h_name')
        drop_spec=Doctor.objects.filter(s_name__s_name=spec,h_name__district=location).values_list('s_name')
        hospitals=Hospital.objects.filter(id__in=specilization)
        
        drop_spec=Specialization.objects.filter(id__in=drop_spec).values_list('s_name',flat=True).distinct()
        drop_location=Hospital.objects.filter(district=location).values_list('district',flat=True).distinct()
        if specilization:
            context={
                'hospitals':hospitals,
                'drop_spec':drop_spec,
                # 'spec':spec,
                'drop_location':drop_location
            }
            return render(request, 'home/hospital.html', context)
        else:
            messages.info(request, 'No doctors and hospitals are available for this Specialization plz check another location')
            return render(request, 'home/hospital.html')
    

def doctor(request,id):

    if 'spec' in request.session:
        spec = request.session['spec']
        doctor=Doctor.objects.filter(h_name__id=id,s_name__s_name=spec)
        context={
            'doctor':doctor
        }
    
        return render(request, 'home/doctor.html', context)
    else:
        doctor=Doctor.objects.filter(h_name__id=id)
        context={
            'doctor':doctor
        }
        return render(request, 'home/doctor.html', context)





@login_required(login_url='login')
def appointment(request,id):
    doctor=Doctor.objects.get(id=id)
    context={
        'd':doctor
    }
    return render(request, 'home/appointment.html', context)


@login_required(login_url='login')
def a_confirmation(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['contact']
        date=request.POST['date']
        doctor=request.POST['dr']
        hospital=request.POST['h']
        gender=request.POST['gender']
        spec=request.POST['spec']
        sys=request.POST['sy']
        fee=request.POST['fee']
        age=request.POST['age']
        time=['10:10','10:20','10:30','10:40','10:50','11:00','11:10','11:20','11:30','11:40','11:50','12:00']
        # generate random time for the date
        import random
        r_time=random.choice(time)        
        # save the appointment details in appointment table
        appointment=Appointment(p_name=name,p_email=email,p_contact=phone,date=date,d_name=doctor,h_name=hospital,s_name=spec,time=r_time,fee=fee,symptoms=sys,p_age=age,p_gender=gender)
        appointment.save()

        send_mail(
                'Appointment Success',
                'Your appointment for '+doctor+ 'in' +hospital+ 'has been confirmed. date: '+date+ 'time: '+r_time+'AM',
                'ajcebatchb2023@gmail.com',
                [email],
                fail_silently=False,
            )
        messages.success(request, 'Your appointment has been confirmed . Kindly please check your mail address for further details')
    else:
        messages.error(request, 'Something went wrong')
    return redirect('home')