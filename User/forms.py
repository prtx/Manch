from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from models import member
		
		
class member_registration_form(forms.ModelForm):
    
    password1 = forms.CharField( label=("Password"), widget=forms.PasswordInput )
    password2 = forms.CharField( label=("Retype Password"), widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ('username','email','first_name')


    def clean_username(self):

    	print self.cleaned_data
        username = self.cleaned_data['username']
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Already In Use')


    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords Mismatch')
        return password2


    def save(self, commit=True):

        user = super(member_registration_form, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

       
class member_update_form(forms.ModelForm):
	
	class Meta:
		model = member
		fields = ('location','about_me',)
		#fields = ('display_picture','location','description',)
