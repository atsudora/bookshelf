from django.db  import models

class BookModel(models.Model):
    bookname = models.CharField(max_length=255)
    summary = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.bookname