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
        # 'title', 'email','m_uni','phd_uni','current_employer','position','github','linkedIn','research_Area','Personal_website'
    title = models.CharField(max_length=500)
    # email = models.EmailField(_('email address'), unique=True)
    email = models.EmailField('Contact Email', max_length=500)
    personal_website = models.CharField('Personal Website', max_length=500,blank=True)
    m_uni = models.CharField('Master\'s University', max_length=400,blank=True)
    phd_uni = models.CharField('PhD University',max_length=400, blank=True)
    current_employer = models.CharField('Current Employer',max_length=500, blank=True)
    # days = models.ManyToManyField(Days)
    position = models.CharField('Position',max_length=500, blank=True)
    github = models.CharField('Github',max_length=500, blank=True)
    linkedin = models.CharField('LinkedIn',max_length=500, blank=True)
    research_area = models.CharField('Research Area',max_length=500, blank=True)
    work_field = models.CharField('Working Field',max_length=500, blank=True,default=None)



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
        self.title = self.author.name
        self.email = self.author.email
        print('Vuya ID   ', type(self.work_field))
        # self.registration =
        super().save()  # saving image first



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
