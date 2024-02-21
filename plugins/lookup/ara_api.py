# Copyright (c) 2022 The ARA Records Ansible authors
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    lookup: ara_api
    author:
        - David Moreau-Simard (@dmsimard)
        - Christoph Hille (@hille721)
    version_added: "0.1.0"
    short_description: Queries the ARA API for data
    description:
        - Queries the ARA API for data
    options:
        _terms:
            description:
                - The endpoint to query
            type: list
            elements: string
            required: True
"""

EXAMPLES = """
    - debug: msg="{{ lookup('ara_api','/api/v1/playbooks/1') }}"
"""

RETURN = """
    _raw:
        description: response from query
"""

from ansible.plugins import AnsibleError

try:
    from ara.plugins.lookup.ara_api import LookupModule as LookupBase
    HAS_ARA = True
except ImportError:
    from ansible.plugins.lookup import LookupBase
    HAS_ARA = False


class LookupModule(LookupBase):

    def __init__(self):
        if not HAS_ARA:
            raise AnsibleError(
                """The ara_api lookup plugin needs ara installed
                (https://ara.readthedocs.io/en/latest/)
                """
            )
        super().__init__()
