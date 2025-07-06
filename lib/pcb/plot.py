#!/usr/bin/python3
#
# PCB Plotter Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import math

def M (ax, ay, bx, by):
	return ((ax + bx) / 2, (ay + by) / 2)

class Core:
	def __init__ (o, tx = 0.1, ty = 0.1):
		(o.tx, o.ty) = (tx, ty)

		o.move (0, 0)

	def move (o, x, y):
		print (f'M {x} {y}')

		(o.sx, o.sy) = (x, y)
		(o.ex, o.ey) = (x, y)

	def line (o, x, y):
		print (f'L {x} {y}')

		(o.ex, o.ey) = (x, y)

	def close (o):
		o.line (o.sx. o.sy)

	def conic (o, cx, cy, x, y):
		(lx, ly) = M (o.ex, o.ey, cx, cy)
		(rx, ry) = M (   x,    y, cx, cy)
		(mx, my) = M (  lx,   ly, rx, ry)

		if abs (cx - mx) <= o.tx and abs (cy - my) <= o.ty:
			o.line (mx, my)
			o.line ( x,  y)
		else:
			o.conic (lx, ly, mx, my)
			o.conic (rx, ry,  x,  y)

	def cubic (o, lx, ly, rx, ry, x, y):
		(ax, ay) = M (o.ex, o.ey, lx, ly)
		(bx, by) = M (   x,    y, rx, ry)
		(cx, cy) = M (  lx,   ly, rx, ry)

		(dx, dy) = M (  ax,   ay, cx, cy)
		(ex, ey) = M (  bx,   by, cx, cy)
		(mx, my) = M (  dx,   dy, ex, ey)

		if abs (cx - mx) <= o.tx and abs (cy - my) <= o.ty:
			o.line (mx, my)
			o.line ( x,  y)
		else:
			o.cubic (ax, ay, dx, dy, mx, my)
			o.cubic (ex, ey, bx, by,  x,  y)

	def arc (o, ox, oy, x, y):
		(lx, ly, rx, ry) = (o.ex - ox, o.ey - oy, x - ox, y - ox)
		(sx, sy) = (lx + rx, ly + ry)

		D = math.hypot (lx, ly) + math.hypot (rx, ry)
		k = D / (2 * math.hypot (sx, sy))

		(mx, my) = (ox + k * sx, oy + k * sy)
		(cx, cy) = M (o.ex, o.ey, x, y)

		if abs (cx - mx) <= o.tx and abs (cy - my) <= o.ty:
			o.line (mx, my)
			o.line ( x,  y)
		else:
			o.arc (ox, oy, mx, my)
			o.arc (ox, oy,  x,  y)

