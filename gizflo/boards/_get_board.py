# Copyright (c) 2014 Christopher Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from __future__ import print_function

from xilinx._xula import Xula, Xula2

xbrd = {
    'xula': Xula,
    'xula2': Xula2,
}

def get_board(name):
    """ retrieve a board definition from the name provided.
    """
    brd = None
    if xbrd.has_key(name):
        brd = xbrd[name]()
        brd.path = './xilinx/'
    elif abrd.has_key(name):
        brd = abrd[name]()
        brd.path = './altera/'
    else:
        # @todo: print out a list of boards and descriptions
        raise ValueError("Invalid board %s"%(name,))
    
    return brd