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

import pytest

pytestmark = pytest.mark.asyncio


async def test_message_listing(test_cli_user):
    guild = await test_cli_user.create_guild()
    channel = await test_cli_user.create_guild_channel(guild_id=guild.id)
    messages = []
    for _ in range(10):
        messages.append(
            await test_cli_user.create_message(guild_id=guild.id, channel_id=channel.id)
        )

    # assert all messages we just created can be refetched if we give the
    # middle message to the 'around' parameter
    middle_message_id = messages[5].id

    resp = await test_cli_user.get(
        f"/api/v6/channels/{channel.id}/messages",
        query_string={"around": middle_message_id},
    )
    assert resp.status_code == 200
    rjson = await resp.json

    fetched_ids = [m["id"] for m in rjson]
    for message in messages:
        assert str(message.id) in fetched_ids
