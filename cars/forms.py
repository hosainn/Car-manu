from django import forms

from cars.models import CarModel,CarParts



class CarsForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

class PartsForm(forms.ModelForm):
    class Meta:
        model = CarParts
        fields = '__all__'

