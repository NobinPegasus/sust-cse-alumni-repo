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
    title = forms.CharField(disabled = True,initial=None)
    email = forms.CharField(disabled = True)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'email','chamber','address','fees','days','start_time','end_time','image','review','rating','overall_rating']

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
