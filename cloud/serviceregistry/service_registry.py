from cloud.service_instance import ServiceInstance
import abc


class ServiceRegistry(abc.ABC):

    @abc.abstractmethod
    def register(self, service_instance: ServiceInstance):
        pass

    @abc.abstractmethod
    def deregister(self):
        pass

