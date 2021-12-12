from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin ,CreateModelMixin

from rest_framework import generics

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

from rest_framework.exceptions import ValidationError

from books.api.permissions import IsAdminOrReadOnly , IsCommentOwnerOrReadOnly

from books.api.serializers import Book, BookSerializer , Comment, CommentSerializer
from books.models import Book

from books.api.pagination import SmallPagination,LargePaagination



class BookListCreateAPIView (generics.ListCreateAPIView):
    # queryset = Book.objects.all().order_by("-created_date")
    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer   
    
    permission_classes= [IsAdminOrReadOnly]
    # permission_classes=[IsAdminUser]
    pagination_class= SmallPagination
    # pagination_class= LargePaagination

    


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializer
   
    permission_classes= [IsAdminOrReadOnly]


class CommentCreatAPIView(generics.CreateAPIView):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializer

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book_pk=self.kwargs.get("book_pk")
        book = generics.get_object_or_404(Book,pk=book_pk)
        commenter= self.request.user
        is_Comment= Comment.objects.filter(commenter=commenter,book=book)
        if is_Comment.exists():
            raise ValidationError("you can make one comment for each book")
        serializer.save(book=book,commenter=commenter)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializer

    # permission_classes=[permissions.IsAuthenticated]
    permission_classes=[IsCommentOwnerOrReadOnly]







# class BookListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


#     #listelemek
#     def get(self,request ,*args, **kwargs):
#         return self.list(request,*args, **kwargs)

#     #yaratmak
#     def post( self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)







