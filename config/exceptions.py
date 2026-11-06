from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return None

    if isinstance(response.data, dict) and "detail" in response.data:
        message, errors = response.data["detail"], None
    else:
        message, errors = "Validation failed.", response.data

    response.data = {
        "status_code": response.status_code,
        "message": message,
        "errors": errors,
    }
    return response


