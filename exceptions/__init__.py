class PermissionDenied(Exception):

    def __init__(self, message="Permission Denied"):
        self.message = message
        super().__init__(self.message)