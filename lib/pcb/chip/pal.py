#!/usr/bin/python3
#
# PCB PAL Chips
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb.package

class P16V8 (pcb.package.DIP20):
	pins = {
		'D0':  2, 'D1':  3, 'D2':  4, 'D3':  5,
		'D4':  6, 'D5':  7, 'D6':  8, 'D7':  9,
		'Q0': 19, 'Q1': 18, 'Q2': 17, 'Q3': 16,
		'Q4': 15, 'Q5': 14, 'Q6': 13, 'Q7': 12,

		'CLK': 1, 'GND': 10, 'OE': 11, 'VCC': 20
	}

class P22V10 (pcb.package.DIP24):
	pins = {
		'D0':  2, 'D1':  3, 'D2':  4, 'D3':  5, 'D4':  6,
		'D5':  7, 'D6':  8, 'D7':  9, 'D8': 10, 'D9': 11,
		'Q0': 23, 'Q1': 22, 'Q2': 21, 'Q3': 20, 'Q4': 19,
		'Q5': 18, 'Q6': 17, 'Q7': 16, 'Q8': 15, 'Q9': 14,

		'CLK': 1, 'GND': 12, 'OE': 13, 'VCC': 24
	}

