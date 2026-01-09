from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


# -------------------------------
# API ROUTES (for reference)
# -------------------------------
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all notes'
        },
        {
            'Endpoint': '/notes/<id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'content': 'note text'},
            'description': 'Create a new note'
        },
        {
            'Endpoint': '/notes/<id>/update/',
            'method': 'PUT',
            'body': {'content': 'updated text'},
            'description': 'Update a note'
        },
        {
            'Endpoint': '/notes/<id>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a note'
        },
    ]
    return Response(routes)


# -------------------------------
# GET ALL NOTES
# -------------------------------
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-created')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# -------------------------------
# GET SINGLE NOTE
# -------------------------------
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# -------------------------------
# CREATE NOTE
# -------------------------------
@api_view(['POST'])
def createNote(request):
    data = request.data

    # Frontend sends "content"
    # Database/model uses "body"

