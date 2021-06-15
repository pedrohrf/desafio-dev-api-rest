
class BaseHttpResponseException(Exception):
    """ Base HTTP Response to treat specific exceptions """

    def __init__(self, status: int, body):
        super(BaseException, self).__init__()
        self.status = status
        self.body = body


class BadRequestException(BaseHttpResponseException):
    def __init__(self, body):
        super(BadRequestException, self).__init__(400, body)


class NotFoundException(BaseHttpResponseException):
    def __init__(self, body):
        super(NotFoundException, self).__init__(404, body)
