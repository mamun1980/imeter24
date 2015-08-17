from haystack import routers


class UserRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'user'

    def for_read(self, **hints):
        return 'user'