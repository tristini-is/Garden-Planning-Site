from django.forms import ModelForm
from .models import Planter, Plant
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PlanterForm (ModelForm) :
    class Meta:
        model = Planter
        fields = ('name',)

class PlantForm (ModelForm):
    class Meta:
        model = Plant
        fields = ('name', 'care','plantDate', )

        widgets = {
            'plantDate': DateInput(attrs={'class': 'datepicker'})
        }
    def createPlant(request, planter_id):
        form = PlantForm()
        box = Planter.objects.get(pk=planter_id)
    
        if request.method == 'POST':
            plant_data = request.POST.copy()
            plant_data['planter_id'] = planter_id
        
            form = PlantForm(plant_data)

            if form.is_valid():

                plant = form.save(commit=False)
                plant.box = box
                plant.save()

                return redirect('planter-detail', planter_id)

        context = {'form': form}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']