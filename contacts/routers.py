from haystack import routers


class ContactRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'default'

    def for_read(self, **hints):
        return 'default'