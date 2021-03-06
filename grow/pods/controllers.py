from . import messages


class BaseController(object):

    def __init__(self, _pod):
        self.pod = _pod

    @property
    def locale(self):
        return None

    def validate(self, params):
        pass

    def get_http_headers(self, params):
        headers = {}
        mimetype = self.get_mimetype(params)
        if mimetype:
            headers['Content-Type'] = mimetype
        return headers

    def to_route_messages(self):
        route_messages = []
        for path in self.list_concrete_paths():
            message = messages.RouteMessage()
            message.path = path
            message.kind = self.KIND
            route_messages.append(message)
        return route_messages
