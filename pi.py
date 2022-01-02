#!/usr/bin/python3

#    PYI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PYI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PYI. If not, see <https://www.gnu.org/licenses/>.

from multiprocessing import Process
from multiprocessing import Queue

num_proc = 10

rectangle_x = 10000
rectangle_y = 10000
area = rectangle_x * rectangle_y

proc_rec_x = rectangle_x / num_proc
proc_rec_y = rectangle_y / num_proc

part = 0
full = 0

circle = 0

if (proc_rec_x % 1 != 0):
    if (proc_rec_y % 1 != 0):
        print("x or y not dividable by", num_proc)
        exit(-1)
    else:
        part = proc_rec_y
        full = rectangle_x
else:
    part = proc_rec_x
    full = rectangle_y

def check_points(start, part, full, q):

    in_circle = 0
    side = (rectangle_x * rectangle_y)**0.5

    for x in range(start, part):
        for y in range(full):
          if ((x*x + y*y)**0.5) <= side:
                in_circle += 1

    q.put(in_circle)

if __name__ == '__main__':
    q = Queue()
    for x in range(num_proc):
        p = Process(target=check_points, args=(int(x * part), int(part * (x+1)), int(full), q))
        p.start()

    for x in range(num_proc):
        circle += q.get()
        p.join()

print(4 * circle/area)
