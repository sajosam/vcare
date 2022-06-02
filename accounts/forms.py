# from django import forms
# from .models import Account


# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Enter Password',
#         'class': 'form-control',
#     }))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Confirm Password'
#     }))

#     class Meta:
#         model = Account
#         fields = ['first_name', 'last_name', 'phone_number', 'email', 'password','state','district','dob','sex']

#     def clean(self):
#         cleaned_data = super(RegistrationForm, self).clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "Password does not match!"
#             )

#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
#         self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
#         self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
#         self.fields['dob'].widget.attrs['placeholder'] = 'Enter the dob'
#         self.fields['sex'].widget.attrs['placeholder'] = 'Male/Female'
#         self.fields['state'].widget.attrs['placeholder'] = 'Enter state '
#         self.fields['district'].widget.attrs['placeholder'] = 'Enter district '
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'