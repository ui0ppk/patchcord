"""

Litecord
Copyright (C) 2018-2019  Luna Mendes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

VOICE_SERVER = {
    'hostname': {'type': 'string', 'maxlength': 255, 'required': True}
}

VOICE_REGION = {
    'id': {'type': 'string', 'maxlength': 255, 'required': True},
    'name': {'type': 'string', 'maxlength': 255, 'required': True},

    'vip': {'type': 'boolean', 'default': False},
    'deprecated': {'type': 'boolean', 'default': False},
    'custom': {'type': 'boolean', 'default': False},
}