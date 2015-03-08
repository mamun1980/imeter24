from haystack import routers


class MasterRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'purchase'

    def for_read(self, **hints):
        return 'purchase'