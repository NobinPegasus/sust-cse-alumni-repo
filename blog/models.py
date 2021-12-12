from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from multiselectfield import MultiSelectField
# from djangoratings.fields import RatingField
from django.utils.translation import gettext_lazy as _
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# from datetime import datetime
# from django.utils import timezone



DAYS_OF_WEEK = [
    (0, '  Monday'),
    (1, '  Tuesday'),
    (2, '  Wednesday'),
    (3, '  Thursday'),
    (4, '  Friday'),
    (5, '  Saturday'),
    (6, '  Sunday'),
]



class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
        return is_liked







class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Name',max_length=100)
    # email = models.EmailField(_('email address'), unique=True)
    email = models.EmailField('Email',max_length=100)
    chamber = models.CharField('Chamber\'s Name',max_length=200)
    address = models.CharField('Address',max_length=100, blank=True)
    fees = models.IntegerField(default=0)
    # days = models.ManyToManyField(Days)
    days = MultiSelectField('Available Days', choices= DAYS_OF_WEEK)
    # hours = models.DateTimeField()
    start_time = models.TimeField('Chamber Beginning Time')
    end_time = models.TimeField('Chamber Ending Time')
    image = models.ImageField( upload_to='profile_pics')
    review = models.TextField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # rating = models.ManyToManyField(MyRating)
    rating = models.IntegerField('Behavior')
    overall_rating = models.PositiveIntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])

    # rating = GenericRelation(Rating, related_query_name='foos')
    # rating = Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')
    # Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    date_posted = models.DateTimeField(default=timezone.now)

    objects = PostManager()

    class Meta:
        ordering = ('-date_posted', )

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    # def __str__(self):
    #     return f'{self.title} Post'

    def save(self):
        print('Author   ', self.author.first_name)
        print("Age   ", self.title)
        self.title = self.author.first_name
        print("Pore   ", self.title)
        print('Auth user Model  ', settings.AUTH_USER_MODEL)
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if (img.height > 1020 or img.width > 1920):
            new_img = (1020, 1920)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.author
