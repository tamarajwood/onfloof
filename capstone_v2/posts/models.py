from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    previewText = models.CharField(max_length=120)
    previewImage = models.CharField(max_length=100)
    id = models.PositiveIntegerField(primary_key = True)
    ## preview image will store file locations like static/images/image_1.jpg

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    post = models.ManyToManyField(Post, related_name='subjects')
## a sub category model can be added later on such as 'food' 'gear' etc. for now subcategories that pertain to multiple subjects
## such as food will be put into multiple subjects so seen on multiple pages

    def __str__(self):
        return self.subject

## if have time create many to many field comment class (not sure why comment class has to be many to many)

class Comment(models.Model):
    comment = models.CharField(max_length = 500)
    post = models.ManyToManyField(Post, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment

########### NOTES ##############

### MAY get rid of general as subject for simplicity and then add subcategories
### if something is really general (and applies to all subjects) then list it under all of the subjects
### add subcategories like food, training etc. (IN FUTURE)
