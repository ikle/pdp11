#!/usr/bin/python3
#
# PCB 7400-Series Chips
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb.package

class T244 (pcb.package.DIP20):  # AP5
	pins = {
		'AD0':  2, 'AD1':  4, 'AD2':  6, 'AD3':  8, 'AOE':  1,
		'AQ0': 18, 'AQ1': 16, 'AQ2': 14, 'AQ3': 12,
		'BD0': 11, 'BD1': 13, 'BD2': 15, 'BD3': 17, 'BOE': 19
		'BQ0':  9, 'BQ1':  7, 'BQ2':  5, 'BQ3':  3,

		'GND': 10, 'VCC': 20
	}

class T245 (pcb.package.DIP20):  # AP6
	pins = {
		'A0':  2, 'A1':  3, 'A2':  4, 'A3':  5,
		'A4':  6, 'A5':  7, 'A6':  8, 'A7':  9,
		'B0': 18, 'B1': 17, 'B2': 16, 'B3': 15,
		'B4': 14, 'B5': 13, 'B6': 12, 'B7': 11,

		'DIR': 1, 'GND': 10, 'OE': 19, 'VCC': 20
	}

class T374 (pcb.package.DIP20):  # IR23
	pins = {
		'D0':  3, 'D1':  4, 'D2':  7, 'D3':  8,
		'D4': 13, 'D5': 14, 'D6': 17, 'D7': 18,
		'Q0':  2, 'Q1':  5, 'Q2':  6, 'Q3':  9,
		'Q4': 12, 'Q5': 15, 'Q6': 16, 'Q7': 19,

		'OE': 1, 'GND': 10, 'CLK': 11, 'VCC': 20
	}

class T574 (pcb.package.DIP20):  # IR37
	pins = {
		'D0':  2, 'D1':  3, 'D2':  4, 'D3':  5,
		'D4':  6, 'D5':  7, 'D6':  8, 'D7':  9,
		'Q0': 19, 'Q1': 18, 'Q2': 17, 'Q3': 16,
		'Q4': 15, 'Q5': 14, 'Q6': 13, 'Q7': 12,

		'OE': 1, 'GND': 10, 'CLK': 11, 'VCC': 20
	}

