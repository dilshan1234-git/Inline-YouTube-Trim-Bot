#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("API_ID", '14631157'))
    API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5927429053:AAGNa4VeQEOM5_Fj_mmq-21OqB6qr308DDU")     
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1002106332206'))
