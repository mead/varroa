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

from oslo_config import cfg
from oslo_policy import policy


CONF = cfg.CONF
_POLICY_PATH = '/etc/varroa/policy.yaml'


enforcer = policy.Enforcer(CONF, policy_file=_POLICY_PATH)

READER_OR_OWNER = 'reader_or_owner'

base_rules = [
    policy.RuleDefault(
        name='admin_required',
        check_str='role:admin or is_admin:1'),
    policy.RuleDefault(
        name='owner',
        check_str='project_id:%(project_id)s'),
    policy.RuleDefault(
        name=READER_OR_OWNER,
        check_str='role:reader or (role:reader and rule:owner)'),
]

IP_USAGE_PREFIX = "varroa:ip_usage:%s"

ip_usage_rules = [
    policy.DocumentedRuleDefault(
        name=IP_USAGE_PREFIX % 'list',
        check_str='',
        scope_types=['system', 'project'],
        description='List ip usage.',
        operations=[{'path': '/v1/ip-usage/',
                     'method': 'GET'},
                    {'path': '/v1/ip-usage/',
                     'method': 'HEAD'}]),
    policy.DocumentedRuleDefault(
        name=IP_USAGE_PREFIX % 'list:all',
        check_str='role:reader',
        scope_types=['system'],
        description='List all ip usage.',
        operations=[{'path': '/v1/ip-usage/',
                     'method': 'GET'}]),
]

enforcer.register_defaults(base_rules)
enforcer.register_defaults(ip_usage_rules)


def list_rules():
    return base_rules + ip_usage_rules
