from django.shortcuts import render, redirect

# Create your views here.
from polka.models import Person


def login(request):
    if request.method == "GET":
        return render(request, 'loginForm.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Person.objects.get(username=username, password=password)
        except (Person.DoesNotExist, Person.MultipleObjectsReturned) as e:
            print(e)
            return redirect("/login/")
        url_redirect = request.GET.get('next', '/')
        request.session['user_id'] = user.id
        return redirect(url_redirect)

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')