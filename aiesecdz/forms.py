from django.forms import ModelForm
from django import forms
from .models import *

class TestimonialForm(ModelForm):

    class Meta:
        model = Testimonial
        fields = [
                'comment',
                'attachements',
                ]
