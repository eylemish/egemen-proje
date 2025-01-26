from django.shortcuts import render
from .models import Article

# Create your views here.

def aboutproject_screen_view(request):
   
   context = {}
#    context['some_string'] = "this is some string that i'm passing to the view"

#    context = {
#       'some_string': "yeyy yine some string passliyorum"
#    }
   list_of_values = []
   list_of_values.append("first entry")
   list_of_values.append("second entry")
   list_of_values.append("third entry")
   list_of_values.append("fourth entry")
   context['list_of_values'] = list_of_values

   return render(request, "first/aboutproject.html", context)


def articles_view(request):

   articles = Article.objects.all()
   context = {
      'articles': articles,
   }
   return render(request, "first/articles.html", context)

def aboutus_view(request):

   context = {}
   return render(request, "first/aboutus.html", context)