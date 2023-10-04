from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    class Status(models.TextChoices):
        TO_READ = 'TR', 'ToRead'
        PUBLISHED = 'F', 'Finished'
        READING = 'R', 'Reading'
        ABANDONED = 'A', 'Abandoned'

    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=250)
    reading_status = models.CharField(max_length=2, choices=Status.choices, default=Status.TO_READ)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.title}"

