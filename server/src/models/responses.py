class BaseResponse:
    def __init__(self, status):
        self.status = status

    def as_dict(self):
        return str(vars(self))


class SuccessResponse(BaseResponse):
    def __init__(self, status="Success", data="{}"):
        super().__init__(status)
        self.data = data


class FailResponse(BaseResponse):
    def __init__(self, status="Fail", message=""):
        super().__init__(status)
        self.message = message


class ErrorResponse(BaseResponse):
    def __init__(self, status="Error", message="Unknown error occurred"):
        super().__init__(status)
        self.message = message
