# Copyright 2013 BrewPi
# This file is part of BrewPi.

# BrewPi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BrewPi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BrewPi.  If not, see <http://www.gnu.org/licenses/>.

import simplejson as json


def getPinList(arduinoType, shieldType):
    if arduinoType == "leonardo" and shieldType == "revC":
        pinList = [{'val': 6, 'text': ' 6 (Act 1)', 'type': 'act'},
                   {'val': 5, 'text': ' 5 (Act 2)', 'type': 'act'},
                   {'val': 2, 'text': ' 2 (Act 3)', 'type': 'act'},
                   {'val': 23, 'text': 'A5 (Act 4)', 'type': 'act'},
                   {'val': 4, 'text': ' 4 (Door)', 'type': 'door'},
                   {'val': 22, 'text': 'A4 (OneWire)', 'type': 'onewire'},
                   {'val': 3, 'text': ' 3', 'type': 'beep'},
                   {'val': 7, 'text': ' 7', 'type': 'rotary'},
                   {'val': 8, 'text': ' 8', 'type': 'rotary'},
                   {'val': 9, 'text': ' 9', 'type': 'rotary'},
                   {'val': 10, ' text': '10', 'type': 'spi'},
                   {'val': 0, 'text': ' 0', 'type': 'free'},
                   {'val': 1, 'text': ' 1', 'type': 'free'},
                   {'val': 11, ' text': '11', 'type': 'free'},
                   {'val': 12, ' text': '12', 'type': 'free'},
                   {'val': 13, ' text': '13', 'type': 'free'},
                   {'val': 18, 'text': 'A0', 'type': 'free'},
                   {'val': 19, 'text': 'A1', 'type': 'free'},
                   {'val': 20, 'text': 'A2', 'type': 'free'},
                   {'val': 21, 'text': 'A3', 'type': 'free'}]
    elif arduinoType == "standard" and shieldType == "revC":
        pinList = [{'val': 6, 'text': ' 6 (Act 1)', 'type': 'act'},
                   {'val': 5, 'text': ' 5 (Act 2)', 'type': 'act'},
                   {'val': 2, 'text': ' 2 (Act 3)', 'type': 'act'},
                   {'val': 19, 'text': 'A5 (Act 4)', 'type': 'act'},
                   {'val': 4, 'text': ' 4 (Door)', 'type': 'door'},
                   {'val': 18, 'text': 'A4 (OneWire)', 'type': 'onewire'},
                   {'val': 3, 'text': ' 3', 'type': 'beep'},
                   {'val': 7, 'text': ' 7', 'type': 'rotary'},
                   {'val': 8, 'text': ' 8', 'type': 'rotary'},
                   {'val': 9, 'text': ' 9', 'type': 'rotary'},
                   {'val': 10, ' text': '10', 'type': 'spi'},
                   {'val': 11, ' text': '11', 'type': 'spi'},
                   {'val': 12, ' text': '12', 'type': 'spi'},
                   {'val': 13, ' text': '13', 'type': 'spi'},
                   {'val': 0, 'text': ' 0', 'type': 'serial'},
                   {'val': 1, 'text': ' 1', 'type': 'serial'},
                   {'val': 14, 'text': 'A0', 'type': 'free'},
                   {'val': 15, 'text': 'A1', 'type': 'free'},
                   {'val': 16, 'text': 'A2', 'type': 'free'},
                   {'val': 17, 'text': 'A3', 'type': 'free'}]
    elif arduinoType == "leonardo" and shieldType == "revA":
        pinList = [{'val': 6, 'text': '  6 (Cool)', 'type': 'act'},
                   {'val': 5, 'text': '  5 (Heat)', 'type': 'act'},
                   {'val': 4, 'text': ' 4 (Door)', 'type': 'door'},
                   {'val': 22, 'text': 'A4 (OneWire)', 'type': 'onewire'},
                   {'val': 23, 'text': 'A5 (OneWire1)', 'type': 'onewire'},
                   {'val': 3, 'text': ' 3', 'type': 'beep'},
                   {'val': 7, 'text': ' 7', 'type': 'rotary'},
                   {'val': 8, 'text': ' 8', 'type': 'rotary'},
                   {'val': 9, 'text': ' 9', 'type': 'rotary'},
                   {'val': 10, ' text': '10', 'type': 'spi'},
                   {'val': 0, 'text': ' 0', 'type': 'free'},
                   {'val': 1, 'text': ' 1', 'type': 'free'},
                   {'val': 2, 'text': '  2', 'type': 'free'},
                   {'val': 11, ' text': '11', 'type': 'free'},
                   {'val': 12, ' text': '12', 'type': 'free'},
                   {'val': 13, ' text': '13', 'type': 'free'},
                   {'val': 18, 'text': 'A0', 'type': 'free'},
                   {'val': 19, 'text': 'A1', 'type': 'free'},
                   {'val': 20, 'text': 'A2', 'type': 'free'},
                   {'val': 21, 'text': 'A3', 'type': 'free'}]
    elif arduinoType == "standard" and shieldType == "revA":
        pinList = [{'val': 6, 'text': '  6 (Cool)', 'type': 'act'},
                   {'val': 5, 'text': '  5 (Heat)', 'type': 'act'},
                   {'val': 4, 'text': ' 4 (Door)', 'type': 'door'},
                   {'val': 18, 'text': 'A4 (OneWire)', 'type': 'onewire'},
                   {'val': 19, 'text': 'A5 (OneWire1)', 'type': 'onewire'},
                   {'val': 3, 'text': ' 3', 'type': 'beep'},
                   {'val': 7, 'text': ' 7', 'type': 'rotary'},
                   {'val': 8, 'text': ' 8', 'type': 'rotary'},
                   {'val': 9, 'text': ' 9', 'type': 'rotary'},
                   {'val': 10, ' text': '10', 'type': 'spi'},
                   {'val': 11, ' text': '11', 'type': 'spi'},
                   {'val': 12, ' text': '12', 'type': 'spi'},
                   {'val': 13, ' text': '13', 'type': 'spi'},
                   {'val': 0, 'text': ' 0', 'type': 'serial'},
                   {'val': 1, 'text': ' 1', 'type': 'serial'},
                   {'val': 2, 'text': '  2', 'type': 'free'},
                   {'val': 14, 'text': 'A0', 'type': 'free'},
                   {'val': 15, 'text': 'A1', 'type': 'free'},
                   {'val': 16, 'text': 'A2', 'type': 'free'},
                   {'val': 17, 'text': 'A3', 'type': 'free'}]
    elif arduinoType == "leonardo" and shieldType == "diy":
        pinList = [{'val': 12, 'text': '  12 (Cool)', 'type': 'act'},
                   {'val': 13, 'text': '  13 (Heat)', 'type': 'act'},
                   {'val': 23, 'text': ' A5 (Door)', 'type': 'door'},
                   {'val': 10, 'text': '10 (OneWire)', 'type': 'onewire'},
                   {'val': 11, 'text': '11 (OneWire1)', 'type': 'onewire'},
                   {'val': 0, 'text': ' 0', 'type': 'rotary'},
                   {'val': 1, 'text': ' 1', 'type': 'rotary'},
                   {'val': 2, 'text': ' 2', 'type': 'rotary'},
                   {'val': 3, 'text': ' 3', 'type': 'display'},
                   {'val': 4, ' text': '4', 'type': 'display'},
                   {'val': 5, ' text': '5', 'type': 'display'},
                   {'val': 6, ' text': '6', 'type': 'display'},
                   {'val': 7, ' text': '7', 'type': 'display'},
                   {'val': 8, ' text': '8', 'type': 'display'},
                   {'val': 9, ' text': '9', 'type': 'display'},
                   {'val': 18, 'text': 'A0', 'type': 'free'},
                   {'val': 19, 'text': 'A1', 'type': 'free'},
                   {'val': 20, 'text': 'A2', 'type': 'free'},
                   {'val': 21, 'text': 'A3', 'type': 'free'},
                   {'val': 22, 'text': 'A4', 'type': 'free'}]
    else:
        print 'Unknown Arduino or board type'
        pinList = {}
    return pinList


def getPinListJson(arduinoType, shieldType):
    try:
        pinList = getPinList(arduinoType, shieldType)
        return json.dumps(pinList)
    except json.JSONDecodeError:
        print "Cannot process pin list JSON"
        return 0

def pinListTest():
    print getPinListJson("leonardo", "revC")
    print getPinListJson("standard", "revC")
    print getPinListJson("leonardo", "revA")
    print getPinListJson("standard", "revA")

# pinListTest()
