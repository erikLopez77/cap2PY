import strawberry, typer

@strawberry.type
class Book:
    title: str
    author: str
    price: int

@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return Book(title="Numerical Python",author="Johansan", price= 750)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, price: int)-> Book:
        print(f"Adding new book: {title}")
        return Book(title=title, author=author, price=price)

schema = strawberry.Schema(query=Query, mutation=Mutation)
