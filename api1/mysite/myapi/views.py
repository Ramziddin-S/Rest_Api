from rest_framework import viewsets
from .models import Author, Genre, Book
from .serializers import AuthorSerializers, GenreSerializers, BookSerializers
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .services import *
from rest_framework.exceptions import NotFound


class AuthorView(GenericAPIView):
    serializer_class = AuthorSerializers

    def get_object(self, *args, **kwargs):
        try:
            author = Author.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return author

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response({"detail": f"Author with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            author = get_author(author_id=pk)
            if not author:
                raise NotFound("Author not found !")
            return Response(author, status=status.HTTP_200_OK)
        else:
            authors = get_authors()
            return Response(authors, status=status.HTTP_200_OK)


class GenreView(GenericAPIView):
    serializer_class = GenreSerializers

    def get_object(self, *args, **kwargs):
        try:
            genre = Genre.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return genre

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=genre)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response({"detail": f"Genre with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            genre = get_genre(genre_id=pk)
            if not genre:
                raise NotFound("Genre not found !")
            return Response(genre, status=status.HTTP_200_OK)
        else:
            genre = get_genres()
            return Response(genre, status=status.HTTP_200_OK)


class BookView(GenericAPIView):
    serializer_class = BookSerializers

    def get_object(self, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
        except Exception as e:
            book = None
            print(e)
        return book

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = self.get_serializer(data=request.data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({"detail": f"Book with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            book = get_book()
            if not book:
                raise NotFound("Book is not found")
            return Response(book, status=status.HTTP_200_OK)
        else:
            book = Book.objects.all()
            serializer = BookSerializers(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
