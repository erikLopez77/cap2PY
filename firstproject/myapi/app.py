import strawberry, typer
import strawberry_django
from .models import Book
from graphene_django import DjangoObjectType
import graphene

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "publisher", "price")

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())

    def resolve_all_books(self, info):
        return Book.objects.all()

    def resolve_book(self, info, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return None


class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        publisher = graphene.String(required=True)
        price = graphene.Int(required=True)

    def mutate(self, info, title, author, publisher, price):
        #we saved a book in db and we return it
        book = Book.objects.create( title=title, author=author, publisher=publisher, price=price )
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
