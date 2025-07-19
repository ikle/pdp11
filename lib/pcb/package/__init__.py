#!/usr/bin/python3
#
# PCB Chip Package Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb.package.dip

class Package:
	def __getattr__ (o, label):
		s = label.split ('_')
		n = s[0]

		return o.anchor (o.pins[n], int (s[1]) if len (s) > 1 else 0)

class DIP20 (Package):
	def __init__ (o, O, angle = 0):
		pcb.package.dip.init (o, O, 20, 3, angle)

class DIP24 (Package):
	def __init__ (o, O, angle = 0):
		pcb.package.dip.init (o, O, 24, 3, angle)

class DIP40 (Package):
	def __init__ (o, O, angle = 0):
		pcb.package.dip.init (o, O, 40, 6, angle)

