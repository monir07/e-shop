from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()    
        self.helper.form_id = 'id-signupForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
    

    def save(self, commit=True):
        obj = super(UserRegistrationForm, self).save(commit=False)
        obj.email = self.cleaned_data['email']
        obj.first_name = self.cleaned_data['first_name']
        obj.last_name = self.cleaned_data['last_name']
        if commit:
            obj.save()
        return obj