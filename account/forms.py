from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True)

    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')

#TODO: какие методы отвечают за валидацию написать : clean; etc;

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Such username already exists.')
        return username

    def clean(self):
        data = self.cleaned_data
        # print(data)
        password = data.get('password')
        # TODO: спросить про pop, почему удаляем password_confirm ? и почему была ошибка до этого?
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user
