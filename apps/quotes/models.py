from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

class FavoriteManager(models.Manager):
    def total(self, user):
        fav_count = Product.objects.filter(favorite__id = user)
        count = 0
        for quote in fav_count:
            count = count + 1

        return count
class QuoteManager(models.Manager):
    def quotevalidator(self, author, content):
        errors = []
        if len(author) < 3:
            errors.append("Author name must be atleast 3 characters long")
        if len(content) < 10:
            errors.append("Quote too short!")
        return {'errors': errors}

class Quote(models.Model):
    author = models.CharField(max_length = 255)
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    User = models.ForeignKey(User, related_name = "Quote")
    objects = QuoteManager()

class Favorite(models.Model):
    quotes = models.ManyToManyField(Quote, related_name = 'favorite')
    user = models.OneToOneField(User)
    objects = FavoriteManager()
