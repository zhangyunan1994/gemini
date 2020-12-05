import unittest
from random import random

from cloud.service_instance import ServiceInstance
from cloud.serviceregistry.consul_service_registry import ConsulServiceRegistry


class MyTestCase(unittest.TestCase):
    def test_consul_register(self):
        instance = ServiceInstance("abc", "127.0.0.1", 8000, instance_id=f'abc_{random()}')

        consulServiceRegistry = ConsulServiceRegistry("127.0.0.1", 8500)
        consulServiceRegistry.register(instance)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
