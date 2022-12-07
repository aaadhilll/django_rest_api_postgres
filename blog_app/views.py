from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def blog_list(request):
    all_blogs = Blog.objects.filter(is_public=True)
    serializer = BlogSerializer(all_blogs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def blog_detail(request, pk):
    all_blogs = Blog.objects.get(is_public=True, pk=pk)
    serializer = BlogSerializer(all_blogs)
    return Response(serializer.data)
