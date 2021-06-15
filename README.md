# ara-collection

Opinionated collection of Ansible roles available on [Ansible Galaxy](https://galaxy.ansible.com/recordsansible/ara)
for deploying and configuring [ARA Records Ansible](https://github.com/ansible-community/ara).

ARA Records Ansible and makes it easier to understand and troubleshoot.

![ara](https://raw.githubusercontent.com/ansible-community/ara-collection/master/doc/source/_static/ara-with-icon.png)

## ara_api

![ara_api](https://raw.githubusercontent.com/ansible-community/ara-collection/master/doc/source/_static/ansible-role-ara-api.png)

A role to install and run the ARA API server and built-in reporting interface
in various supported configurations.

Documentation: [roles/ara_api/README.md](https://github.com/ansible-community/ara-collection/blob/master/roles/ara_api/README.md)

## ara_web

![ara_web](doc/source/_static/ansible-role-ara-web.png)

Documentation: [roles/ara_web/README.md](https://github.com/ansible-community/ara-collection/blob/master/roles/ara_web/README.md)

## ara_frontend_nginx

A role that sets up a basic nginx reverse proxy for serving the API server as
well as ara-web.

Documentation: [roles/ara_frontend_nginx/README.md](https://github.com/ansible-community/ara-collection/blob/master/roles/ara_frontend_nginx/README.md)

# Community and getting help

- Bugs, issues and enhancements: https://github.com/ansible-community/ara-collection/issues
- IRC: #ara on [Libera](https://libera.chat/)
- Slack: https://arecordsansible.slack.com ([invitation link](https://join.slack.com/t/arecordsansible/shared_invite/enQtMjMxNzI4ODAxMDQxLTU2NTU3YjMwYzRlYmRkZTVjZTFiOWIxNjE5NGRhMDQ3ZTgzZmQyZTY2NzY5YmZmNDA5ZWY4YTY1Y2Y1ODBmNzc))

- Website and blog: https://ara.recordsansible.org
- Twitter: https://twitter.com/recordsansible

# Contributing

Contributions to the project are welcome and appreciated !

Get started with the [contributor's documentation](https://ara.readthedocs.io/en/latest/contributing.html).

# Authors

Contributors to the project can be viewed on [GitHub](https://github.com/ansible-community/ara-collection/graphs/contributors).

# Copyright

```
Copyright (c) 2020 The ARA Records Ansible authors

ARA Records Ansible is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ARA Records Ansible is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ARA Records Ansible. If not, see <http://www.gnu.org/licenses/>.
```
