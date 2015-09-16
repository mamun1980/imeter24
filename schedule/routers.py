from haystack import routers


class JobRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'job'

    def for_read(self, **hints):
        return 'job'

class JobControlRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'jobcontrol'

    def for_read(self, **hints):
        return 'jobcontrol'