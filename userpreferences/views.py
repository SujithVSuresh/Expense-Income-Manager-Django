from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    preference = UserPreference.objects.get(user=request.user)
    form = PreferenceForm(instance=preference)
    if request.method == 'POST':
        form = PreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            messages.success(request, 'saved changes')
            return redirect('userpreferences:preferences')
    
    context = {'form':form}
    return render(request, 'userpreferences/index.html', context)