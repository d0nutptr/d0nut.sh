from pyramid.httpexceptions import HTTPUnauthorized


class AuthorizationLevel:
    def __init__(self, value: int) -> None:
        self.value = value

    def __and__(self, other) -> int:
        return self.value & other.value


class Authorization:
    Guest: AuthorizationLevel = AuthorizationLevel(1)
    User: AuthorizationLevel = AuthorizationLevel(2)
    Admin: AuthorizationLevel = AuthorizationLevel(4)

    @classmethod
    def is_authorized(cls,
                      expected_authorization: AuthorizationLevel,
                      presented_authorization: AuthorizationLevel) -> bool:
        return expected_authorization & presented_authorization != 0


class AuthorizationException(HTTPUnauthorized):
    def __init__(self) -> None:
        super().__init__()
        self.explanation = "You do not have permission to access this resource."
