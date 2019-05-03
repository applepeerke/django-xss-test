from django.shortcuts import render

def post_list(request):
    return render(request, 'xssapp/post_list.html', {})
