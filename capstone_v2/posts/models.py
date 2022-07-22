from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    previewImage = models.CharField(max_length=100)
    ## preview image will store file locations like static/images/image_1.jpg

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    post = models.ManyToManyField(Post, related_name='subjects')

    def __str__(self):
        return self.subject

## if have time create many to many field comment class (not sure why comment class has to be many to many)


########### NOTES ##############

### MAY get rid of general as subject for simplicity and then add subcategories
### if something is really general (and applies to all subjects) then list it under all of the subjects
### add subcategories like food, training etc. (IN FUTURE)
