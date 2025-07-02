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

def draw_pads (o, nh, W, s, d):
	o.pad  (0, 0, d, d)
	o.opad (W, 0, d)

	for i in range (1, nh):
		o.opad (0, -s * i, d)
		o.opad (W, -s * i, d)

def draw_power (o, nh, W, s, d, contacts):
	for i in range (0, nh):
		if not (1 + i) in contacts:
			o.hole (0, -s * i, d)

		if not (n - i) in contacts:
			o.hole (W, -s * i, d)

def draw_holes (o, nh, W, s, d):
	for i in range (0, nh):
		o.hole (0, -s * i, d)
		o.hole (W, -s * i, d)

def draw (O, n, w, angle, pins, s = 2.54, d = 1.3, h = 0.7):
	nh = n // 2
	(x, y) = O
	(W, H) = (w * s, (nh - 1) * s)

	vcc = pcb.chip.select_pins (pins, 'VCC')
	gnd = pcb.chip.select_pins (pins, 'GND')

	def fn (o):
		o.view (x, y, angle)

		match o.name:
			case 'top':	draw_pads  (o, nh, W, s, d)
			case 'bottom':	draw_pads  (o, nh, W, s, d)
			case 'power':	draw_power (o, nh, W, s, d, vcc)
			case 'ground':	draw_power (o, nh, W, s, d, gnd)
			case 'drill':	draw_holes (o, nh, W, s, h)

	return fn

def init (o, O, n, w, angle = 0, s = 2.54, d = 1.3, h = 0.7):
	o.anchor = anchor (O, n, w, angle, s)
	o.draw   = draw   (O, n, w, angle, o.pins, s, d, h)

