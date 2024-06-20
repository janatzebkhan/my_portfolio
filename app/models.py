from django.db import models

# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    proficiency_percentage = models.IntegerField(default=0)

    def _str_(self):
        return self.skill_name
    




class Facts(models.Model):
    emoji = models.CharField(max_length=100 , blank=True)  # Emoji Unicode or icon class (e.g., "😊" or "bi bi-emoji-smile")
    count = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def _str_(self):
        return self.title
    
    
    
    
class Summery(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    list_1 = models.CharField( max_length=50)
    list_2 = models.CharField( max_length=50)
    list_3 = models.CharField( max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    
    
    
class Professional_skill(models.Model):
    title = models.CharField( max_length=100)
    time = models.CharField( max_length=50)
    detail_title = models.CharField( max_length=200)
    detail_1 = models.TextField(blank=True)
    detail_2 = models.TextField(blank=True)
    detail_3 = models.TextField(blank=True)
    detail_4 = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    



class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    lightbox_link = models.URLField(max_length=200, blank=True)
    details_link = models.URLField(max_length=200, blank=True)
    
    def _str_(self):
        return  self.title
    
        
    
    
    
class Services(models.Model):
    emoji = models.CharField(max_length=100 , blank=True)  # Emoji Unicode or icon class (e.g., "😊" or "bi bi-emoji-smile")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def _str_(self):
        return self.title
    
    
class Partners(models.Model):
    name = models.CharField( max_length=50)
    image = models.ImageField( upload_to='partners_images/',)
    category = models.CharField(max_length=50)
    category_1 = models.CharField( max_length=50)
    quets = models.TextField()
    
    
    def __str__(self) -> str:
        return self.name
    
    
    
    


class PortfolioItem(models.Model):
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    project_date = models.DateField()
    project_url = models.CharField( max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    subject = models.CharField( max_length=250)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name