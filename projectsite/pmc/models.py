from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return self.title

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    headquarters_location = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill, related_name='contractors')
    hire_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    contractors = models.ManyToManyField(Contractor, related_name='projects')

    def __str__(self):
        return self.title
