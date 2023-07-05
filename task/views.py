from rest_framework.response import Response
from rest_framework import pagination,status
from .models import Task
from .serializers import TaskSerializer, TaskValidateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Paginator(pagination.PageNumberPagination):
    page_size = 10


class TaksListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = Paginator

    def post(self, request, *args, **kwargs):
        serializer = TaskValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        completed = serializer.validated_data['completed']
        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed
        )
        return Response(data=TaskSerializer(task).data, status=status.HTTP_201_CREATED)


class TaksDeteilAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id_task'

    def put(self, request, *args, **kwargs):
        try:
            item = Task.objects.get(id_task=kwargs['id_task'])
        except Task.DoesNotExist:
            return Response(data={'error': 'Tasks not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskValidateSerializer(instance=item, data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data['title']
        description = serializer.validated_data['description']
        completed = serializer.validated_data['completed']
        item.title = title
        item.description = description
        item.completed = completed
        item.save()
        return Response(data=TaskSerializer(item).data, status=status.HTTP_200_OK)