from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..logreg.models import User
from .models import Quote, Favorite

def index(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    data = {
    'quotes': Quote.objects.exclude(favorite__id = request.session['favorite_id']),
    'favorites': Quote.objects.filter(favorite__id = request.session['favorite_id'])
    }
    return render(request, 'quotes/lander.html', data)

def contribute(request):
    user = User.objects.get(id = request.session['id'])
    quote = Quote.objects.quotevalidator(request.POST['author'], request.POST['content'])
    if quote['errors'] != []:
        for errors in quote['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect(reverse('quotes:index'))
    Quote.objects.create(author = request.POST['author'], content = request.POST['content'], User = user )
    return redirect(reverse('quotes:index'))

def add_fav(request, id):
    try:
        fav = Favorite.objects.get(user__id = request.session['id'])
    except:
        user = User.objects.get(id = request.session['id'])
        fav = Favorite.objects.create(user = user)
    quote = Quote.objects.get(id = id)
    request.session['favorite_id'] = fav.id
    fav.quotes.add(quote)
    return redirect(reverse('quotes:index'))

def user(request, id):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    count = 0
    user = User.objects.get(id = id)
    quotes = Quote.objects.filter(User__id = id)
    for quote in quotes:
        count = count + 1
    data = {
    'user': user,
    'count': count,
    'quotes': quotes
    }
    return render(request, 'quotes/user.html', data)

def remove(request, id):
    myfav = Favorite.objects.get(user__id = request.session['id'])
    target = Quote.objects.get(id = id)
    myfav.quotes.remove(target)
    return redirect(reverse('quotes:index'))

def logout(request):
	del request.session['first_name']
	del request.session['id']
	return redirect(reverse('login:home'))
