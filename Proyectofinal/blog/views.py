from django.shortcuts import render


# Create your views here.
posts = [
    {
        'Autor':'Adriel',
        'titulo':'Post 1',
        'fecha_post':'20/09',
        'contenido':'HolasoyAdriel'
    },
    {
        'Autor':'Wanda',
        'titulo':'Post 2',
        'fecha_post':'20/09',
        'contenido':'HolasoyWanda'
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

