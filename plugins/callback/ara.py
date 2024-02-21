# Copyright (c) 2022 The ARA Records Ansible authors
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
name: ara
callback_type: notification
requirements:
  - ara
short_description: Sends playbook execution data to the ARA API internally or over HTTP
description:
  - Sends playbook execution data to the ARA API internally or over HTTP
version_added: 0.1.0
author:
    - David Moreau-Simard (@dmsimard)
    - Christoph Hille (@hille721)
options:
  api_client:
    description: The client to use for communicating with the API
    default: offline
    env:
      - name: ARA_API_CLIENT
    ini:
      - section: ara
        key: api_client
    choices: ['offline', 'http']
  api_server:
    description: When using the HTTP client, the base URL to the ARA API server
    default: http://127.0.0.1:8000
    env:
      - name: ARA_API_SERVER
    ini:
      - section: ara
        key: api_server
  api_username:
    description: If authentication is required, the username to authenticate with
    default: null
    env:
      - name: ARA_API_USERNAME
    ini:
      - section: ara
        key: api_username
  api_password:
    description: If authentication is required, the password to authenticate with
    default: null
    env:
      - name: ARA_API_PASSWORD
    ini:
      - section: ara
        key: api_password
  api_cert:
    description: If a client certificate is required, the path to the certificate to use.
    default: null
    env:
      - name: ARA_API_CERT
    ini:
      - section: ara
        key: api_cert
  api_key:
    description: If a client certificate is required, the path to the private key to use.
    default: null
    env:
      - name: ARA_API_KEY
    ini:
      - section: ara
        key: api_key
  api_ca:
    description: The path to a CA bundle.
    default: null
    env:
      - name: ARA_API_CA
    ini:
      - section: ara
        key: api_ca
  api_insecure:
    description: Can be enabled to ignore SSL certification of the API server
    type: bool
    default: false
    env:
      - name: ARA_API_INSECURE
    ini:
      - section: ara
        key: api_insecure
  api_timeout:
    description: Timeout, in seconds, before giving up on HTTP requests
    type: integer
    default: 30
    env:
      - name: ARA_API_TIMEOUT
    ini:
      - section: ara
        key: api_timeout
  argument_labels:
    description: |
        A list of CLI arguments that, if set, will be automatically applied to playbooks as labels.
        Note that CLI arguments are not always named the same as how they are represented by Ansible.
        For example, --limit is "subset", --user is "remote_user" but --check is "check".
    type: list
    default:
      - remote_user
      - check
      - tags
      - skip_tags
      - subset
    env:
      - name: ARA_ARGUMENT_LABELS
    ini:
      - section: ara
        key: argument_labels
  callback_threads:
    description:
      - The number of threads to use in API client thread pools (maximum 4)
      - When set to 0, no threading will be used (default) which is appropriate for usage with sqlite
      - Using threads is recommended when the server is using MySQL or PostgreSQL
    type: integer
    default: 0
    env:
      - name: ARA_CALLBACK_THREADS
    ini:
      - section: ara
        key: callback_threads
  default_labels:
    description: A list of default labels that will be applied to playbooks
    type: list
    default: []
    env:
      - name: ARA_DEFAULT_LABELS
    ini:
      - section: ara
        key: default_labels
  ignored_facts:
    description: List of host facts that will not be saved by ARA
    type: list
    default: ["ansible_env"]
    env:
      - name: ARA_IGNORED_FACTS
    ini:
      - section: ara
        key: ignored_facts
  ignored_arguments:
    description: List of Ansible arguments that will not be saved by ARA
    type: list
    default: ["extra_vars"]
    env:
      - name: ARA_IGNORED_ARGUMENTS
    ini:
      - section: ara
        key: ignored_arguments
  ignored_files:
    description:
      - List of file path patterns that will not be saved by ARA
      - Note that the default pattern ('.ansible/tmp') gets dynamically set to the value of ANSIBLE_LOCAL_TEMP
      - The configuration for ANSIBLE_LOCAL_TEMP is typically ~/.ansible/tmp unless it is changed.
    type: list
    default: [".ansible/tmp"]
    env:
      - name: ARA_IGNORED_FILES
    ini:
      - section: ara
        key: ignored_files
  localhost_as_hostname:
    description:
        - Associates results to the hostname (or fqdn) instead of localhost when the inventory name is localhost
        - Defaults to false for backwards compatibility, set to true to enable
        - This can be useful when targetting localhost, using ansible-pull or ansible-playbook -i 'localhost,'
        - This helps differentiating results between hosts, otherwise everything would be recorded under localhost.
    type: boolean
    default: false
    env:
      - name: ARA_LOCALHOST_AS_HOSTNAME
    ini:
      - section: ara
        key: localhost_as_hostname
  localhost_as_hostname_format:
    description:
      - The format to use when recording the hostname for localhost
      - This is used when recording the controller hostname or when ARA_LOCALHOST_TO_HOSTNAME is true
      - There are different formats to choose from based on the full (or short) configured hostname and fqdn
      - Defaults to 'fqdn' (i.e, server.example.org) but can be set to 'fqdn_short' (server)
      - Other options include 'hostname' and 'hostname_short' which may be suitable depending on server configuration
    default: fqdn
    env:
      - name: ARA_LOCALHOST_AS_HOSTNAME_FORMAT
    ini:
      - section: ara
        key: localhost_as_hostname_format
    choices: ['fqdn', 'fqdn_short', 'hostname', 'hostname_short']
  record_controller:
    description:
      - Whether ara should record the controller hostname on which the playbook ran
      - Defaults to true but may be optionally set to false for privacy or other use cases
    type: boolean
    default: true
    env:
      - name: ARA_RECORD_CONTROLLER
    ini:
      - section: ara
        key: record_controller
  record_controller_name:
    description:
      - The name to use when recording the controller hostname.
      - Defaults to the system hostname.
    type: string
    env:
      - name: ARA_RECORD_CONTROLLER_NAME
    ini:
      - section: ara
        key: record_controller_name
  record_user:
    description:
      - Whether ara should record the user that ran a playbook
      - Defaults to true but may be optionally set to false for privacy or other use cases
    type: boolean
    default: true
    env:
      - name: ARA_RECORD_USER
    ini:
      - section: ara
        key: record_user
  record_user_name:
    description:
      - The name to use when recording the user that ran a playbook.
      - Defaults to the OS user which ran the playbook.
    type: string
    env:
      - name: ARA_RECORD_USER_NAME
    ini:
      - section: ara
        key: record_user_name
  record_task_content:
    description:
      - Whether ara should record the content of a task
      - Defaults to true, set to false for privacy or other use cases
    type: boolean
    default: true
    env:
      - name: ARA_RECORD_TASK_CONTENT
    ini:
      - section: ara
        key: record_task_content
"""
from ansible.plugins import AnsibleError

try:
    from ara.plugins.callback.ara_default import CallbackModule as CallbackBase

    HAS_ARA = True
except ImportError:
    HAS_ARA = False

    from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    CALLBACK_NAME = "recordsansible.ara.ara"

    def __init__(self):
        if not HAS_ARA:
            raise AnsibleError(
                """The ara callback plugin needs ara installed
                (https://ara.readthedocs.io/en/latest/)
                """
            )
        super().__init__()
