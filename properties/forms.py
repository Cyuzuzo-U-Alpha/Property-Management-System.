from django import forms

class PropertySearchForm(forms.Form):
    location = forms.CharField(required=False)
    price_min = forms.DecimalField(required=False)
    price_max = forms.DecimalField(required=False)


    class ContactForm(forms.ModelForm):
        class Meta:
            fields = ["name", "email", "message"]
            widgets = {
                "name": forms.TextInput(
                    attrs={"class": "form-control", "placeholder": "Enter your name"}
                ),
                "email": forms.EmailInput(
                    attrs={"class": "form-control", "placeholder": "Enter your email"}
                ),
                "message": forms.Textarea(
                    attrs={"class": "form-control", "placeholder": "Message"}
                ),
            }