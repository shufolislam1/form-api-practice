from django.shortcuts import render
from .forms import practiceForm

def practice_form_view(request):
    if request.method == 'POST':
        form = practiceForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = practiceForm()

    return render(request, './first_app/django_form.html', {'data': form})
