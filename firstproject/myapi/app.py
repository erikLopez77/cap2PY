import strawberry, typer
import strawberry_django
from .models import Book

@strawberry_django.type(Book)
class BookType:
    id: strawberry.ID
    title: str
    author: str
    price: int
    publisher: str

@strawberry.input
class BookFilterInput:
    id: strawberry.ID

@strawberry.type
class Query:
    all_books: list[BookType] = strawberry_django.field()
    book_by_id: BookType | None = strawberry_django.field(filters=BookFilterInput)

@strawberry.type
class Mutation:
    @strawberry_django.mutation
    def create_book(self,title: str, author: str, price: int, publisher: str) -> BookType:
        # Aquí deberías crear el libro en la DB de Django de verdad
        nuevo_libro = Book.objects.create( title=title, author=author, price=price, publisher=publisher)
        return nuevo_libro

schema = strawberry.Schema(query=Query, mutation=Mutation)
