from  django.forms import ModelForm
from .models import * 
    
class DojoForm(ModelForm):
    class Meta:
        model = Dojo
        fields = '__all__'

class NijaForm(ModelForm):
    class Meta:
        model = Nija
        fields = '__all__'