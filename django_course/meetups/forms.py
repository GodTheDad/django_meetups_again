from django import forms


class Reg_Form(forms.Form):
    email = forms.EmailField(label='Your Email')