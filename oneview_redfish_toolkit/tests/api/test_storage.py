# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

from oneview_redfish_toolkit.api.storage import Storage
from oneview_redfish_toolkit.tests.base_test import BaseTest


class TestStorage(BaseTest):
    """Tests for Storage class"""

    def setUp(self):
        """Tests preparation"""

        # Loading Storage mockup result
        with open(
            'oneview_redfish_toolkit/mockups/redfish/Storage.json'
        ) as f:
            self.storage_mockup = json.load(f)

        # Loading ServerHardwareTypes mockup value
        with open(
            'oneview_redfish_toolkit/mockups/oneview/ServerHardwareTypes.json'
        ) as f:
            self.server_hardware_types = json.load(f)

    def test_class_instantiation(self):
        # Tests if class is correctly instantiated and validated

        try:
            storage = Storage('30303437-3034-4D32-3230-313133364752',
                              self.server_hardware_types)
        except Exception as e:
            self.fail("Failed to instantiate Storage class."
                      " Error: {}".format(e))
        self.assertIsInstance(storage, Storage)

    def test_serialize(self):
        # Tests the serialize function result against known result

        try:
            storage = Storage('30303437-3034-4D32-3230-313133364752',
                              self.server_hardware_types)
        except Exception as e:
            self.fail("Failed to instantiate Storage class."
                      " Error: {}".format(e))

        try:
            result = json.loads(storage.serialize())
        except Exception as e:
            self.fail("Failed to serialize. Error: ".format(e))

        self.assertEqual(self.storage_mockup, result)
