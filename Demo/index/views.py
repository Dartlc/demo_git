from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def index_api(request):
    """
        Index Api
    :param request: request
    :return: Response
    """

    return Response({'data': 'Hello World'}, status=status.HTTP_200_OK)
