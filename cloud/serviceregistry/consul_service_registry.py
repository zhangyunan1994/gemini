import consul

from cloud.service_instance import ServiceInstance
from cloud.serviceregistry.service_registry import ServiceRegistry


class ConsulServiceRegistry(ServiceRegistry):
    _consul = None
    _instance_id = None

    def __init__(self, host: str, port: int, token: str = None):
        self.host = host
        self.port = port
        self.token = token
        self._consul = consul.Consul(host, port, token=token)

    def register(self, service_instance: ServiceInstance):
        schema = "http"
        if service_instance.secure:
            schema = "https"
        check = consul.Check.http(f'{schema}:{service_instance.host}:{service_instance.port}/actuator/health', "1s",
                                  "3s", "10s")
        self._consul.agent.service.register(service_instance.service_id,
                                            service_id=service_instance.instance_id,
                                            address=service_instance.host,
                                            port=service_instance.port,
                                            check=check)
        self._instance_id = service_instance.instance_id

    def deregister(self):
        if self._instance_id:
            self._consul.agent.service.deregister(service_id=self._instance_id)
            self._instance_id = None

