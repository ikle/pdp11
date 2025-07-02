#!/usr/bin/python3
#
# PCB DIP Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb, pcb.chip, pcb.grid

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

def init (o, O, n, w, angle = 0, s = 2.54, d = 1.3, h = 0.7):
	(nh, wd, sh, W) = (n // 2, w * 2, s / 2, w * s)
	(Lx, Ly) = O
	(Rx, Ry) = (Lx + W, Ly - (nh - 1) * s)

	AL = pcb.rotate (O, Lx, Ly - s , angle)
	BL = pcb.rotate (O, Rx, Ly - sh, angle)

	R  = pcb.rotate (O, Rx, Ry     , angle)
	AR = pcb.rotate (O, Rx, Ry + s , angle)
	BR = pcb.rotate (O, Lx, Ry + sh, angle)

	def anchor (i, j = 0):
		if i <= nh:
			return pcb.grid.anchor (O, AL, BL, wd, i - 1, j)

		return pcb.grid.anchor (R, AR, BR, wd, i - nh - 1, j)

	vcc = pcb.chip.select_pins (o.pins, 'VCC')
	gnd = pcb.chip.select_pins (o.pins, 'GND')

	def draw (o, layer):
		o.view (Lx, Ly, angle)

		match layer:
			case 'top':	draw_pads  (o, nh, W, s, d)
			case 'bottom':	draw_pads  (o, nh, W, s, d)
			case 'power':	draw_power (o, nh, W, s, d, vcc)
			case 'ground':	draw_power (o, nh, W, s, d, gnd)
			case 'drill':	draw_holes (o, nh, W, s, h)

	o.anchor = anchor
	o.draw   = draw

