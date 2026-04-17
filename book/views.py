from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser



class AddBookAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        tags=['book'],
        request_body=BookSerializer,
        responses={
            201: BookSerializer,
            400: 'Bad Request'}
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['book'],
        responses={
            200: BookSerializer,
            404: "Bad request"
        }
    )
    def get(self, request):
        book_id = request.query_params.get('pk')

        if book_id:
            books = get_object_or_404(Book, id=book_id)
            serializer = BookSerializer(books)
            return Response(serializer.data, status=status.HTTP_200_OK)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UpdateBookAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['book'],
        request_body=BookSerializer,
        responses={
            200: BookSerializer,
            400: 'Bad Request',
            404: "Not Found"
        }
    )
    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBookAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['book'],
        responses={
            204: "Not content"
        }
    )
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        book.delete()

        return Response({"detail": "No Content"}, status=status.HTTP_204_NO_CONTENT)













