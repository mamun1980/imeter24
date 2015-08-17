from haystack import routers


class EventsRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'events'

    def for_read(self, **hints):
        return 'events'