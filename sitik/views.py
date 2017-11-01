from django.shortcuts import render
def post_list(request):
    return render(request, 'sitik/post_list.html', {})
# Create your views here.
