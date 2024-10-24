from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message


class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1' ,  'password2' ]
        labels = {
            'first_name': "Name",
        }
        
        # For Adding the Styling Class to Model From 
        
    def __init__(self, *args , **kwargs):
        super(CustomUserCreationFrom, self).__init__(*args, **kwargs)
        
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Enter Title '})
        
        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio','short_intro', 'profile_image','social_github','social_linkedin', 'social_twitter','social_website']
        
        
        
    def __init__(self, *args , **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})
            
class SkillForm(ModelForm):
    class Meta:
        
        model = Skill
        fields = ['name', 'description']
        
        
    def __init__(self, *args , **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        
        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})
            
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
        
    def __init__(self, *args , **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        
        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})
        