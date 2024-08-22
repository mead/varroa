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

from varroa.extensions import db


class IPUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(64), nullable=False)
    project_id = db.Column(db.String(64), nullable=False)
    port_id = db.Column(db.String(64), nullable=False, unique=True)
    resource_id = db.Column(db.String(64), nullable=True)
    resource_type = db.Column(db.String(64), nullable=True)
    start = db.Column(db.DateTime(), nullable=False)
    end = db.Column(db.DateTime(), nullable=True)

    def __init__(self, ip, project_id, port_id, resource_id, resource_type,
                 start, end=None):
        self.ip = ip
        self.project_id = project_id
        self.port_id = port_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.start = start
        self.end = end
