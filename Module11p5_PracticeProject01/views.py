from django.shortcuts import render
def base(request):
    return render(request, template_name='base.html')
