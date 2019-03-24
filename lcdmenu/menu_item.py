# This file is part of lcdmenu.
# 
# DragonPi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# DragonPi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with DragonPi.  If not, see <https://www.gnu.org/licenses/>.

"""Framework for using the Adafruit character LCD plate for a menu.

A series of ``MenuItem`` instances are to be added to an LCDMenu()
instance, building up the menu in pieces.

"""

class MenuItem():
    name = "Menu Item:"
    def select(self):
        """Action to take if the select button is pressed."""
        raise NotImplementedError()
    
    def move_right(self):
        """Action to take when the "right" button is pressed."""
        raise NotImplementedError()
    
    def move_left(self):
        """Action to take when the "left" button is pressed."""
        raise NotImplementedError()
    
    def active_text(self):
        """Text based on the current active item."""
        return f"[{self.name} text]"
