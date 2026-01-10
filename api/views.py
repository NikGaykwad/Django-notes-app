from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'Endpoint': '/notes/', 'method': 'GET'},
        {'Endpoint': '/notes/<id>/', 'method': 'GET'},
        {'Endpoint': '/notes/create/', 'method': 'POST'},
        {'Endpoint': '/notes/<id>/update/', 'method': 'PUT'},
        {'Endpoint': '/notes/<id>/delete/', 'method': 'DELETE'},
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-created')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# ✅ FIXED
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data.get('body', "")
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# ✅ FIXED
@api_view(['PUT'])
def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted successfully")

