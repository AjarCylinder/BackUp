from django.shortcuts import render


# Create your views here.
def base(request):
   data = {
      "games": get_all_games()
   }
   return render(request, "main/index.html", data)
