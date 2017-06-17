from django.db import models
from django.core.urlresolvers import reverse

class signup(models.Model):
    first_name = models.CharField(max_length=15 , help_text='First Name')
    last_name = models.CharField(max_length=15 , help_text='Last Name')
    date_of_birth = models.DateField(blank=False , help_text='Date Of Birth',)
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender_choice , default='M')
    email = models.EmailField(max_length=100 , help_text='Email address')
    password =models.CharField(max_length=20 , help_text='password')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    one_time_password = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('signup:details', kwargs={'id':self.id})

    class Meta:
        ordering =['-timestamp']




