def jwt_usuario_response(token, user=None, request=None):
    return {
        'token': token,
        'user': 'Respuesta personalizada',
    }
