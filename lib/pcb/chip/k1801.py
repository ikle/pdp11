#!/usr/bin/python3
#
# PCB K1801-Series Chips
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import pcb.package

class VM2 (pcb.package.DIP40):  # 1801VM2
	pins = {
		'AD0':   9, 'AD1':   8, 'AD2':   7, 'AD3':   6,
		'AD4':   5, 'AD5':   4, 'AD6':   3, 'AD7':   2,
		'AD8':  39, 'AD9':  38, 'AD10': 37, 'AD11': 36,
		'AD12': 35, 'AD13': 34, 'AD14': 33, 'AD15': 32,

		'CLCI': 16, 'VIRQ': 28, 'EVNT': 30, 'HALT': 29,
		'ACLO': 25, 'DCLO': 26, 'AR':   23, 'DMR':  12,
		'SACK': 13, 'RPLY': 17, 'SP2':  11, 'WAKI': 11,

		'SP1':  10, 'WRQ':  10, 'DMGO': 14, 'SYNC': 21,
		'DIN':  22, 'DOUT': 18, 'WTBT': 19, 'IAKO': 24,
		'INIT': 27, 'SEL':  31, 'CLCO': 15,

		'GND2': 1, 'GND1': 20, 'VCC': 40
	}

