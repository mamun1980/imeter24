from haystack import routers


class SLRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'sl'

    def for_read(self, **hints):
        return 'sl'


class PLRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'pl'

    def for_read(self, **hints):
        return 'pl'