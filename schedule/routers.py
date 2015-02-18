from haystack import routers


class MasterRouter(routers.BaseRouter):
    def for_write(self, **hints):
        return 'jobcontrol'

    def for_read(self, **hints):
        return 'jobcontrol'