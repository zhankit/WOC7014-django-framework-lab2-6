from django.forms import ModelForm
from .models import Model
from .models import Review
from .models import Brand

class ReviewForm(ModelForm): 
    class Meta:
        model = Review
        fields = '__all__'

class PhoneForm(ModelForm): 
    class Meta:
        model = Model
        fields = '__all__'

class BrandForm(ModelForm): 
    class Meta:
        model = Brand
        fields = '__all__'