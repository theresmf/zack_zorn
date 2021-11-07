from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    artist_name = models.CharField(max_length=45, null=False, blank=True, default='')
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'.strip()


class MusicGenre(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    members = models.ManyToManyField(to=Artist)
    genre = models.ManyToManyField(to=MusicGenre)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=45)
    band = models.ForeignKey(to=Band, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(to=MusicGenre)

    featuring = models.ManyToManyField(to=Artist)
    release_date = models.DateField()
    producer = models.CharField(max_length=45)
    cover_designer = models.CharField(max_length=45)
    price = models.IntegerField()  # seconds
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


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
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=45)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
