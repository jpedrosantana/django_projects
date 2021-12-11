from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import datetime
from django.forms import ModelForm
from catalog.models import BookInstance, Book, Genre

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class RenewBookForm(ModelForm):
    #renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default = 3)')}

    #Easiest way to validate a field is to modify the clean_<dieldname>() method.
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        #check if a date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_ ('Invalid date - renewal in the past'))

        #check if a date is in allowed range (4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_ ('Invalid date - renewal more than 4 weeks ahead.'))

        #Always return cleaned data
        return data

class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre']
        #labels = {'title': 'titulo', 'author': 'autor'}

    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )