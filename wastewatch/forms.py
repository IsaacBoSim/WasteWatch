from django import forms
from django.forms import ModelForm
from .models import Report

# class FileUploadForm(forms.Form):
#     title = forms.CharField(label='Report Title', required=True)
#     description = forms.CharField(max_length=3000, required=True)
#     text_file = forms.FileField(label='Upload txt/pdf file', required=False)
#     jpg_file = forms.ImageField(label='Upload jpg file', required=False)

class SubmitReportForm(ModelForm):
    file = forms.FileField(label='Upload File', required=False,
                           widget=forms.FileInput(attrs={'accept': '.pdf, .txt, .jpg', 'class': 'form-control-file'}))

    class Meta:
        model = Report
        fields = ['title', 'description', 'file']
        exclude = ['user', 'text_file', 'image_file', 'date', 'status', 'resolve_explanation']
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Description'}),
        'file': forms.FileField(widget=forms.FileInput(attrs={'style': 'display: 0;', 'accept': '.txt,.pdf,.jpg'})),
    }


class AdminReportForm(ModelForm):
    REPORT_STATUS_CHOICES = (
        (1, "In Progress"),
        (2, "Resolved"),
    )
    status = forms.ChoiceField(choices=REPORT_STATUS_CHOICES)
    class Meta:
        model = Report
        fields = ['status', 'resolve_explanation']
        exclude = ['user', 'title', 'description', 'file', 'date', 'text_file', 'image_file']
    widgets = {
        'resolve_explanation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        'status': forms.RadioSelect(attrs={'class': 'form-select visually-hidden'})
    }
