from django.shortcuts import render

import redis
import string





def index(request):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #movies_names = r.lrange("movies", 0,10)
    movies_names = r.lrange("movies:Casablanca", 0,10)

    return render(request, 'movies/index.html', {'movies_names': movies_names})

#def detail(request, movie_name):
   # movie = 
   # return render(request, 'movies/detail.html', {'quote_list': quote_list})

#def search_form(request):
 #   return render(request, 'quotes/search_form.html', {})

#def search_quotes(request):
 #   if request.method == 'POST':
  #      word = request.POST['search_term']
        #quote_list = Quote.objects.all()
    #    result = [q.quote_text for q in quote_list if q.search_quote(word)]

    #return render(request, 'quotes/detail.html', {'quote_list': result})
