from django import forms
from .models import Product
#class ProductForm(forms.Form):

 #   title = forms.CharField()

class ProductForm(forms.ModelForm):
    #title = forms.CharField()
    class Meta:
        model = Product
        fields = [
            'title',
            'content'
        ]
    def clean_title(self):# to validate data with clean_ 
        data = self.cleaned_data.get("title")
        if len(data) < 4:
            raise forms.ValidationError("this is not long enough")
        return data 
