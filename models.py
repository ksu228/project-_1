from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=255)
    User = models.ForeignKey(User, on_delete=models.CASCADE)



class category(models.Model):
    category = models.CharField(max_length=200, unique = True)

class Post(models.Model):
    news_or = models.BooleanField(default = False)
    Post = models.ManyToManyField(category, through='postcategory')
    time = models.DateTimeField()
    Zagolovok = models.CharField(max_length=100)
    text = models.TextField()
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)




class postcategory(models.Model):
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(category, on_delete = models.CASCADE)

class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text_com = models.TextField()
    time_com = models.DateTimeField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)



