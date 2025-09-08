from django.http import Http404
from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        status_code = response.status_code
        if status_code == status.HTTP_404_NOT_FOUND or isinstance(exc, Http404):
            code = 'not_found'
            message = 'Recurso no encontrado.'
        elif status_code == status.HTTP_403_FORBIDDEN:
            code = 'forbidden'
            message = 'Operación no permitida.'
        elif status_code == status.HTTP_401_UNAUTHORIZED:
            code = 'unauthorized'
            message = 'No autenticado.'
        elif status_code >= 500:
            code = 'server_error'
            message = 'Error interno del servidor.'
        else:
            code = 'bad_request'
            message = 'Solicitud inválida.'

        details = response.data
        response.data = {'code': code, 'message': message, 'details': details}
        return response

    # Excepción no manejada por DRF → 500
    return Response(
        {'code': 'server_error', 'message': 'Error interno del servidor.', 'details': str(exc)},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
