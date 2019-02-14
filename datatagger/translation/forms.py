from django import forms

class TranslateForm(forms.Form):
    translated_text = forms.CharField(max_length=250,widget=forms.Textarea)
    language = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)