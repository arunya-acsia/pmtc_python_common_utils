from custom_decorators.response import Response
from custom_decorators.status_constants import HttpStatusCode

from exceptions import PermissionDenied


def register_error_handlers(api):
    @api.errorhandler(PermissionDenied)
    def handle_permission_denied_exception(error):
        return Response.error(
            {"exception": str(error)},
            HttpStatusCode.FORBIDDEN,
            business_error=None,
            message=str(error)
        )