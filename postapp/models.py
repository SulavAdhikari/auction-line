from django.db import models
from django.contrib.auth import get_user_model

import random, string, pytz
from datetime import datetime
from userapp.models import UserProfile

utc = pytz.UTC
# Create your models here.


# creates a random letter/number slug
def generate_slug():
    while True:
        letters = string.ascii_letters
        slug = ''.join(random.choice(letters) for i in range(10))
        if Post.objects.filter(slug=slug):
            continue
        else:
            return slug
        
# 'post' table in database
class Post(models.Model):
     # function to make new name for images       
    def namecomFile1(self, filename):
        return '/'.join([f"{self.category}_pics", str(self.slug), 'comp_pic.jpg'])
    
    def nameFile1(self, filename):
        return '/'.join([f"{self.category}_pics", str(self.slug), f'optional_pic{1}.jpg'])
    def location(self):
        usrp = UserProfile.objects.filter(user=self.user).first()
        location = usrp.primary_location
        return location

    slug = models.CharField(default=None, max_length=16)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    category = models.CharField(max_length=255, default='Any')
    description = models.TextField(null=True)
    comp_image = models.ImageField(upload_to=namecomFile1,null=True)
    sell_location = models.CharField(default='any', max_length=128)

    sold = models.BooleanField(default=False)
    winner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, default=None)

    bidstart = models.IntegerField(default=0)
    buynow = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=datetime.now())
    date_end = models.DateTimeField(default=None)

    # to identify if the post is available or not
    @property
    def is_available(self):
        if self.sold or self.date_end < datetime.now(self.date_end.tzinfo) and self.date_end is not None:
            return False
        return True



    
    