from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import *
from . import views
from garden_app.forms import *
# Create your views here.

def index(request):
    return render( request, 'index.html')

class PlanterListView (generic.ListView):
    model = Planter
    template_name = 'planter_list.html'

class PlanterDetailView(generic.DetailView):
    model = Planter
    template_name = 'planter_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        planter = self.get_object()
        plants = planter.plant_set.all()

        context['plants'] = plants

        return context

class PlantDetailView(generic.DetailView):
    model = Plant
    template_name = 'plant_detail.html'
    
def createPlant(request, planter_id):
    form = PlanterForm()
    planter = Planter.objects.get(pk=planter_id)

    if request.method == 'POST':
        plant_data = request.POST.copy()
        plant_data['planter_id'] = planter_id

        form = PlantForm(plant_data)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.box = planter
            plant.save()

            return redirect('planter-detail', planter_id)
        
    context = {'form': form}
    return render(request, 'plant_form.html', context)

def deletePlant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == 'POST':
        if request.POST.get('confirm') == 'yes':
            plant.delete()
            return redirect('planter-detail', pk=plant.box.pk)
        elif request.POST.get('cancel') == 'yes':
            return redirect('planter-detail', pk=plant.box.pk)
    context = {'plant': plant, 'planter': plant.box}
    return render(request, 'plant_delete.html', {'plant': plant}) 

def updatePlant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect('planter-detail', pk=plant.box.pk)
    else:
        form = PlantForm(instance=plant)

        return render(request, 'plant_update.html', {'form': form, 'plant': plant})

