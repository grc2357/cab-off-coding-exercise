from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# The endpoint hello_world/ is handled by the function hello_world.
# It receives a GET request and returns Hello World.

@api_view(['GET'])
def hello_world(request):
    return Response({'greeting': 'Hello World'})

# The endpoint add_numbers is handled by the function add_numbers.
# It receives a POST request with two numbers and returns their sum;
# otherwise it returns a 400 with an explanation.

@api_view(['POST'])
def add_numbers(request):
    try:
        num1 = float(request.data['numbers'][0])
        num2 = float(request.data['numbers'][1])
        if num1 == int(num1) and num2 == int(num2):
            return Response({'result': int(num1+num2)})
        else:
            return Response({'result': num1+num2})
    except:
        return Response({'detail': ['The input must be an array of two numbers!']}, 
                        status.HTTP_400_BAD_REQUEST)

# The endpoint link_strings is handled by the function link_strings.
# It receives a POST request with two strings and returns the strings joined 
# with a dash; otherwise it returns a 400 with an explanation.

@api_view(['POST'])
def link_strings(request):
    try:
        str1 = request.data['strings'][0]
        str2 = request.data['strings'][1]
        if isinstance(str1, str) and isinstance(str2, str):
            return Response({'string': '{}-{}'.format(str1, str2)})
        else:
            raise
    except:
        return Response({'detail': ['The input must be an array of two strings!']}, 
                        status.HTTP_400_BAD_REQUEST)