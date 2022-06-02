from django.shortcuts import render,redirect
import pickle
import numpy as np
from django.http import HttpResponse
from .models import Disease
from home.models import Specialization,Hospital,Doctor
# django messages
from django.contrib import messages
# Create your views here.


def liverPred(request):
    return render(request, 'predict/LiverPage.html')

def liverPredResult(request):
    if request.method == 'POST':
        age=float(request.POST['age'])
        sex=float(request.POST['sex'])
        total_bilirubin=float(request.POST['total_bilirubin'])
        Direct_Bilirubin=float(request.POST['Direct_Bilirubin'])
        Alkaline_Phosphotase=float(request.POST['Alkaline_Phosphotase'])
        Alamine_Aminotransferase=float(request.POST['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase=float(request.POST['Aspartate_Aminotransferase'])
        Total_Protiens=float(request.POST['Total_Protiens'])
        Albumin=float(request.POST['Albumin'])
        Albumin_and_Globulin_Ratio=float(request.POST['Albumin_and_Globulin_Ratio'])
        input_value=(age,sex,total_bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio)
        input_data_as_numpy_array= np.asarray(input_value)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        with open('liver_scaling.pkl', 'rb') as f:
            scaling = pickle.load(f)
            scaled_data=scaling.transform(input_data_reshaped)
        with open('liver_model.pkl', 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict(scaled_data)
        data=Disease.objects.filter(name='Liver')
        for i in data:
            primarymedication=i.primarymedication.split('@')
            symptoms=i.symptoms.split('@')
            preventions=i.preventions.split('@')
        if int(prediction)==1:
            msg='70% chance of having liver disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Liver'})
        else:
            msg='30% chance of having liver disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Liver'})
    else:
        return HttpResponse('<h1>Please enter the values</h1>')

def diPred(request):
    return render(request, 'predict/diabetesPage.html')

def diPredResult(request):
    if request.method == 'POST':
        age=float(request.POST['age'])
        glucose=float(request.POST['glucose'])
        Insulin=float(request.POST['Insulin'])
        BMI=float(request.POST['BMI'])
        DiabetesPedigreeFunction=float(request.POST['DiabetesPedigreeFunction'])
        input_value=(age,glucose,Insulin,BMI,DiabetesPedigreeFunction)
        input_data_as_numpy_array= np.asarray(input_value)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        with open('diabetes_scaling.pkl', 'rb') as f:
            scaling = pickle.load(f)
            scaled_data=scaling.transform(input_data_reshaped)
        with open('diabetes_model.pkl', 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict(scaled_data)
        data=Disease.objects.filter(name='Diabetes')
        
        for i in data:
            primarymedication=i.primarymedication.split('@')
            symptoms=i.symptoms.split('@')
            preventions=i.preventions.split('@')

        if int(prediction)==1:
            msg='70% chance of having diabetes'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Diabetes'})
        else:
            msg='30% chance of having diabetes'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Diabetes'})
    else:
        return HttpResponse('<h1>Please enter the values</h1>')


def heartPred(request):
    return render(request, 'predict/HeartPage.html')

def heartPredResult(request):
    if request.method == 'POST':
        age=float(request.POST['age'])
        sex=float(request.POST['sex'])
        chestPain=float(request.POST['chestPain'])
        restingBP=float(request.POST['restingBP'])
        cholestoral=float(request.POST['cholestoral'])
        bloodSugar=float(request.POST['bloodSugar'])
        restingCardio=float(request.POST['restingCardio'])
        maxHeartRate=float(request.POST['maxHeartRate'])
        angina=float(request.POST['angina'])
        flourosopy=float(request.POST['flourosopy'])
        Thalassemia=float(request.POST['Thalassemia'])
        input_value=(age,sex,chestPain,restingBP,cholestoral,bloodSugar,restingCardio,maxHeartRate,angina,flourosopy,Thalassemia)
        input_data_as_numpy_array= np.asarray(input_value)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
        with open('heart_model.pkl', 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict(input_data_reshaped)
        data=Disease.objects.filter(name='Heart')
        for i in data:
            primarymedication=i.primarymedication.split('@')
            symptoms=i.symptoms.split('@')
            preventions=i.preventions.split('@')
        if int(prediction)==1:
            msg='70% chance of having heart disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Heart'})
        else:
            msg='30% chance of having heart disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Heart'})
    else:
        return HttpResponse('<h1>Please enter the values</h1>')


def kidneyPred(request):
    return render(request, 'predict/KidneyPage.html')


def kidneyPredResult(request):
    if request.method == 'POST':
        age=float(request.POST['age'])
        sex=float(request.POST['sex'])
        blood_pressure=float(request.POST['blood_pressure'])
        albumin=float(request.POST['albumin'])
        blood_glucose_random=float(request.POST['blood_glucose_random'])
        blood_urea=float(request.POST['blood_urea'])
        serum_creatinine=float(request.POST['serum_creatinine'])
        haemoglobin=float(request.POST['haemoglobin'])
        packed_cell_volume=float(request.POST['packed_cell_volume'])
        white_blood_cell_count=float(request.POST['white_blood_cell_count'])
        red_blood_cell_count=float(request.POST['red_blood_cell_count'])
        hypertension=float(request.POST['hypertension'])
        diabetes_mellitus=float(request.POST['diabetes_mellitus'])
        coronary_artery_disease=float(request.POST['coronary_artery_disease'])
        appetite=float(request.POST['appetite'])
        aanemia=float(request.POST['aanemia'])

        input_value=(age,blood_pressure,albumin,blood_glucose_random,blood_urea,serum_creatinine,haemoglobin,packed_cell_volume,white_blood_cell_count,red_blood_cell_count,hypertension,diabetes_mellitus,coronary_artery_disease,appetite,aanemia)
        input_data_as_numpy_array= np.asarray(input_value)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        

        
        with open('kidney_model.pkl', 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict(input_data_reshaped)
        
        data=Disease.objects.filter(name='Kidney')
        for i in data:
            primarymedication=i.primarymedication.split('@')
            symptoms=i.symptoms.split('@')
            preventions=i.preventions.split('@')
        if int(prediction)==1:
            msg='70% chance of having kidney disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Kidney'})
        else:
            msg='30% chance of having kidney disease'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Kidney'})
    else:
        return HttpResponse('<h1>Please enter the values</h1>')


def cancerPred(request):
    return render(request, 'predict/breastcancerPage.html')

def cancerPredResult(request):
    if request.method == 'POST':
        mean_radius=float(request.POST['mean_radius'])
        mean_texture=float(request.POST['mean_texture'])
        mean_perimeter=float(request.POST['mean_perimeter'])
        mean_area=float(request.POST['mean_area'])
        mean_smoothness=float(request.POST['mean_smoothness'])
        mean_compactness=float(request.POST['mean_compactness'])
        mean_concavity=float(request.POST['mean_concavity'])
        mean_concave_points=float(request.POST['mean_concave_points'])
        mean_symmetry=float(request.POST['mean_symmetry'])
        mean_fractal_dimension=float(request.POST['mean_fractal_dimension'])
        radius_error=float(request.POST['radius_error'])
        texture_error=float(request.POST['texture_error'])
        perimeter_error=float(request.POST['perimeter_error'])
        area_error=float(request.POST['area_error'])
        smoothness_error=float(request.POST['smoothness_error'])
        compactness_error=float(request.POST['compactness_error'])
        concavity_error=float(request.POST['concavity_error'])
        concave_points_error=float(request.POST['concave_points_error'])
        symmetry_error=float(request.POST['symmetry_error'])
        fractal_dimension_error=float(request.POST['fractal_dimension_error'])
        worst_radius=float(request.POST['worst_radius'])
        worst_texture=float(request.POST['worst_texture'])
        worst_perimeter=float(request.POST['worst_perimeter'])
        worst_area=float(request.POST['worst_area'])
        worst_smoothness=float(request.POST['worst_smoothness'])
        worst_compactness=float(request.POST['worst_compactness'])
        worst_concavity=float(request.POST['worst_concavity'])
        worst_concave_points=float(request.POST['worst_concave_points'])
        worst_symmetry=float(request.POST['worst_symmetry'])
        worst_fractal_dimension=float(request.POST['worst_fractal_dimension'])
        
        input_value=(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
        mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
        perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
        symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,
        worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension)
        input_data_as_numpy_array= np.asarray(input_value)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        with open('breast_cancer_model.pkl', 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict(input_data_reshaped)
        
        data=Disease.objects.filter(name__icontains='Breast cancer')
        for i in data:
            primarymedication=i.primarymedication.split('@')
            symptoms=i.symptoms.split('@')
            preventions=i.preventions.split('@')    
        if int(prediction)==1:
            msg='70% chance of having breast cancer'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Breast Cancer'})
        else:
            msg='30% chance of having breast cancer'
            return render(request,'predict/ResultPage.html',{'msg':msg,'symptoms':symptoms,'preventions':preventions,'primarymedication':primarymedication,'d_name':'Breast Cancer'})

    else:
        return HttpResponse('<h1>Please enter the values</h1>')

def backpred(request,d_name):
    data=Specialization.objects.filter(description__icontains=d_name)
    # get with this specialization
    
    if data:
        dr=Doctor.objects.filter(s_name__in=data,h_name__district="Kottayam").values_list('h_name',flat=True)
        drop_spec=Specialization.objects.filter(description__icontains=d_name).values_list('s_name',flat=True)
        drop_location=Hospital.objects.filter(district="Kottayam").values_list('district',flat=True).distinct()
        # get with this hospital
        hsptl=Hospital.objects.filter(id__in=dr)
        return render(request,'home/hospital.html',{'drop_spec':data,'hospitals':hsptl,'drop_location':drop_location,'drop_spec':drop_spec})
    else:
        messages.info(request,"Currently we didnot add any hospitals to this disease")
        return redirect('home')


    