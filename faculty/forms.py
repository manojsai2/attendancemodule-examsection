from django import forms
from login.models import Report





class ReportForm(forms.ModelForm):
    fac_id = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Report
        fields = ['message']
