from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    # Use DRF's default handler first to get standard error responses
    response = exception_handler(exc, context)
    if response is not None:
        # Wrap in a consistent structure
        return Response({
            'success': False,
            'error': response.status_code,
            'message': response.data,
        }, status=response.status_code)

    # Unhandled exceptions
    return Response({
        'success': False,
        'error': 'server_error',
        'message': 'An internal error occurred.'
    }, status=500)

