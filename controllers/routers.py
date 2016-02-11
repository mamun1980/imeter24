from haystack import routers


class ControllerRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'controller'

    def for_read(self, **hints):
        return 'controller'
