from django import forms

class TranslateForm(forms.Form):
    translated_text = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder': 'Enter the translation here.','cols': 80, 'rows': 10}))
    language = forms.CharField(max_length=100, initial='en')
    origin = forms.CharField(max_length=100, widget=forms.HiddenInput())
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)