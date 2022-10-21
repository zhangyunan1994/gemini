import unittest
from random import random

from cloud.discovery.consul_service_discovery import ConsulServiceDiscovery
from cloud.service_instance import ServiceInstance
from cloud.serviceregistry.consul_service_registry import ConsulServiceRegistry


class MyTestCase(unittest.TestCase):
    def test_consul_register(self):
        instance = ServiceInstance("abc", "127.0.0.1", 8000, instance_id=f'abc_{random()}')
        registry = ConsulServiceRegistry("127.0.0.1", 8500)
        registry.register(instance)
        self.assertEqual(True, True)

    def test_consul_discovery(self):
        discovery = ConsulServiceDiscovery("127.0.0.1", 8500)
        print(discovery.get_services())
        print(discovery.get_instances("abc"))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
