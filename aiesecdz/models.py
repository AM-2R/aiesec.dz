from django.db import models

class Testimonial(models.Model):
    comment = models.TextField(blank=False)
    attachements = models.CharField(null=True, max_length=255)
    tkey = models.ForeignKey('TKey', on_delete=models.CASCADE)
    submission_date = models.DateTimeField()

    def __str__(self):
        return "%s" % (self.author)

class TKey(models.Model):
    author = models.CharField(null=False, max_length=255)
    used = models.BooleanField(null=False, default=False)
    value = models.CharField(null=False, max_length=255)

    def __str__(self):
        return "%s -> %s" % (self.author, self.used)
