from django import forms
from properties import models


class TelephoneForm(forms.ModelForm):

    class Meta:
        model = models.Telephone
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AddressForm(forms.ModelForm):

    class Meta:
        model = models.Address
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
