from django.shortcuts import render
import random

# Create your views here.
def example(request):
    return render(request,'core/first_template.html')

def form_view(request):
    print(request.POST)
    return render(request, 'core/form.html')

def magic_number(request):
    if request.method == 'POST':
        number = request.POST['number']
        number = int(number)
        random_number = random.randint(1,10)
        if random_number == number:
            result = 'you win!'
        else:
            result = f'you lose, number was {random_number} try again'
        return render(request, 'core/magic_number.html', {'result':result})
    return render(request, 'core/magic_number.html')

def old_project(request):
    return render(request, 'core/old_project.html')