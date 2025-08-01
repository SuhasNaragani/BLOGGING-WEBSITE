# posts/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# posts/forms.py

from django import forms
from .models import Comment
from django.contrib.auth.models import User # Add this import

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Add this new form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']