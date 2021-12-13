from django import forms
from bootstrap_datepicker_plus import TimePickerInput
from django_starfield import Stars
from .models import Post
# from django.conf import settings
from users.models import CustomUser

# from .widgets import BootstrapDateTimePickerInput
Order_BY_Category = [
    (0, '  Current Employee'),
    (1, '  Session'),
    (2, '  Research Area'),
    (3, '  PhD University'),
    (4, '  Master\'s University'),
]


class DropViewForm(forms.Form):
    fields = forms.ChoiceField(choices = Order_BY_Category)



class PostForm(forms.ModelForm):
    title = forms.CharField(label = 'Name',disabled = True,initial=None)
    email = forms.CharField(disabled = True)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'email','personal_website','m_uni','phd_uni','current_employer','position','github','linkedin','research_area','work_field']

    #     date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=BootstrapDateTimePickerInput()
    # )
        widgets = {
            # 'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            # 'hours' : TimePickerInput().start_of('party time'),
            # 'hours': DateInput(attrs={'class': 'datepicker'})
            # 'hours': forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
            # 'hours': TimePickerInput(),
            'start_time':TimePickerInput().start_of('party time'),
            'end_time':TimePickerInput().end_of('party time'),
            'rating': Stars,
        }
