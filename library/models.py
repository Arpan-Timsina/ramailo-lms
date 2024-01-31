
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



def validate_isbn(value):
    """
    Validate that the ISBN provided follows a valid format.
    """
    if not value.isdigit() or len(value) not in [10, 13]:
        raise ValidationError('ISBN must be either 10 or 13 digits long.')

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    

class User(TimestampedModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.full_name

    




class Book(models.Model):
    
    GENRE_CHOICES = (("fantasy","fantasy"),("historical","historical"),("journal","journal"))
    ISBN_REGEX = r'^\d{10,13}$'

    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13,unique=True,validators=[validate_isbn,RegexValidator(regex=ISBN_REGEX)])
    published_date = models.DateField()
    genre = models.CharField(max_length=50,choices=GENRE_CHOICES)



    def __str__(self):
        return self.title

class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

    
    def __str__(self):
        return self.book.title

class BorrowedBook(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_by')
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} borrowed by {self.user.full_name}'

