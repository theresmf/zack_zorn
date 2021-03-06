from django.db import models
from django.urls import reverse


class Artist(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    artist_name = models.CharField(max_length=45, null=False, blank=True, default='')
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'.strip()

    def get_absolute_url(self):
        return reverse('zackzorn:artist-detail', kwargs={'pk': self.id})


class MusicGenre(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('zackzorn:musicgenre-detail', kwargs={'pk': self.id})


class Band(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    members = models.ManyToManyField(to=Artist, blank=True)
    genre = models.ManyToManyField(to=MusicGenre, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('zackzorn:band-detail', kwargs={'pk': self.id})


class Album(models.Model):
    title = models.CharField(max_length=45)
    band = models.ForeignKey(to=Band, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(to=MusicGenre, blank=True)

    featuring = models.ManyToManyField(to=Artist, blank=True)
    release_date = models.DateField()
    producer = models.CharField(max_length=45, null=True, blank=True)
    cover_designer = models.CharField(max_length=45, null=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('zackzorn:album-detail', kwargs={'pk': self.id})


class Track(models.Model):
    title = models.CharField(max_length=45)
    featuring = models.ManyToManyField(to=Artist)
    length = models.IntegerField()  # seconds

    album = models.ForeignKey(to=Album, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title


class BookGenre(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    pseudonym = models.CharField(max_length=45)
    publisher = models.CharField(max_length=45)
    genre = models.ManyToManyField(to=BookGenre)
    description = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    isbn = models.IntegerField()
    img_url = models.CharField(max_length=45)

    pages_total = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=45)
    event_type = models.CharField(max_length=45)
    date = models.DateField()
    venue = models.CharField(max_length=45)
    ticket_price = models.IntegerField()
    description = models.TextField()
    band = models.ForeignKey(Band, null=True, blank=True, on_delete=models.SET_NULL)
    interviewee = models.CharField(max_length=45)
    completed = models.BooleanField()
    cancelled = models.BooleanField()

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=45)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
