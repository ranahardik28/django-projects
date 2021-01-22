from django.db import models

# Create your models here.


class Blog_data(models.Model):
    categ = (
        ('Finance', 'Finance'),
        ('Sports', 'Sports'),
        ('Business', 'Business'),
        ('WordPress', 'WordPress'),
        ('Food', 'Food'),
        ('Writing', 'Writing'),
        ('Cars', 'Cars'),
        ('Music', 'Music'),
        ('Games', 'Games'),
        ('Movies', 'Movies'),
        ('Books', 'Books'),
        ('Fitness', 'Fitness'),
        ('Mom', 'Mom'),
        ('Travel', 'Travel'),
        ('Current Events', 'Current Events'),
        ('Entertainment', 'Entertainment'),
        ('Fashion', 'Fashion'),
        ('Lifestyle', 'Lifestyle'),
        ('DIY', 'DIY'),
        ('Politics', 'Politics'),
        ('Parenting', 'Parenting'),
        ('Pets', 'Pets'),
    )

    user = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=200, default="", choices=categ)
    title = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    disc = models.CharField(max_length=10000, default="")
    disc2 = models.CharField(max_length=10000, default="")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)


class Views(models.Model):
    user_id = models.IntegerField(default=0)
    blog_id = models.IntegerField(default=0)


class Likes(models.Model):
    user_id = models.IntegerField(default=0)
    blog_id = models.IntegerField(default=0)
