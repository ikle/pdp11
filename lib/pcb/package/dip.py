#!/usr/bin/python3
#
# PCB DIP Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb, pcb.chip, pcb.grid

def anchor (O, n, w, angle = 0, s = 2.54):
	(nh, wd, sh) = (n // 2, w * 2, s / 2)
	(Lx, Ly) = O
	(Rx, Ry) = (Lx + w * s, Ly - (nh - 1) * s)

	AL = pcb.rotate (O, Lx, Ly - s , angle)
	BL = pcb.rotate (O, Rx, Ly - sh, angle)

	R  = pcb.rotate (O, Rx, Ry     , angle)
	AR = pcb.rotate (O, Rx, Ry + s , angle)
	BR = pcb.rotate (O, Lx, Ry + sh, angle)

	def fn (i, j = 0):
		if i <= nh:
			return pcb.grid.anchor (O, AL, BL, wd, i - 1, j)

		return pcb.grid.anchor (R, AR, BR, wd, i - nh - 1, j)

	return fn

def draw (O, n, w, angle, pins, s = 2.54, d = 1.3, h = 0.7):
	nh = n // 2
	(x, y) = O
	(W, H) = (w * s, (nh - 1) * s)

	vcc = pcb.chip.select_pins (pins, 'VCC')
	gnd = pcb.chip.select_pins (pins, 'GND')

	def fn (o):
		o.view (x, y, angle)

		if o.name == 'top' or o.name == 'bottom':
			o.square (0, 0, d)
			o.disc   (W, 0, d)

			for i in range (1, nh):
				o.disc (0, -s * i, d)
				o.disc (W, -s * i, d)

		elif o.name == 'power':
			for i in range (0, nh):
				if not (1 + i) in vcc:
					o.hole (0, -s * i, d)

				if not (n - i) in vcc:
					o.hole (W, -s * i, d)

		elif o.name == 'ground':
			for i in range (0, nh):
				if not (1 + i) in gnd:
					o.hole (0, -s * i, d)

				if not (n - i) in gnd:
					o.hole (W, -s * i, d)

		elif o.name == 'drill':
			for i in range (0, nh):
				o.hole (0, -s * i, h)
				o.hole (W, -s * i, h)

	return fn

def init (o, O, n, w, angle = 0, s = 2.54, d = 1.3, h = 0.7):
	o.anchor = anchor (O, n, w, angle, s)
	o.draw   = draw   (O, n, w, angle, o.pins, s, d, h)

