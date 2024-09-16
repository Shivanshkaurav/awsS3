from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    stud_image = models.ImageField(upload_to="images")
    student_resume = models.FileField(upload_to="files", default="")
    
    def __str__(self):
        return self.name