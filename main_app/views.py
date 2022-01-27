from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Dog, Outfit
from .forms import ExerciseForm

# Define the home view
def assoc_outfit(request, dog_id, outfit_id):
	dog = Dog.objects.get(id=dog_id)
	dog.outfits.add(outfit_id)
	return redirect('detail', dog_id=dog_id)

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    exercise_form = ExerciseForm()
    outfits_dog_doesnt_have = Outfit.objects.exclude(id__in=dog.outfits.all().values_list('id'))
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'exercise_form': exercise_form,
        'outfits': outfits_dog_doesnt_have
        })

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

def add_exercise(request, dog_id):
  form = ExerciseForm(request.POST)
  if form.is_valid():
      new_exercise = form.save(commit=False)
      new_exercise.dog_id = dog_id
      new_exercise.save()
  return redirect('detail', dog_id=dog_id)

class OutfitList(ListView):
    model = Outfit


class OutfitDetail(DetailView):
    model = Outfit


class OutfitCreate(CreateView):
    model = Outfit
    fields = '__all__'


class OutfitUpdate(UpdateView):
    model = Outfit
    fields = ['style', 'color']


class OutfitDelete(DeleteView):
    model = Outfit
    success_url = '/outfits/'