#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import oslo_messaging

from varroa.common import rpc

# Current API version
API_VERSION = '1.0'


class WorkerAPI:
    """Worker api

    Version history:

    1.0 - Add process_security_risk
    """

    def __init__(self):
        target = oslo_messaging.Target(
            topic='varroa-worker', version=API_VERSION
        )
        self._client = oslo_messaging.RPCClient(rpc.TRANSPORT, target)

    def process_security_risk(self, ctxt, security_risk_id):
        cctxt = self._client.prepare(version='1.0')
        cctxt.cast(
            ctxt, 'process_security_risk', security_risk_id=security_risk_id
        )
