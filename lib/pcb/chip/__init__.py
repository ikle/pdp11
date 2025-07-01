#!/usr/bin/python3
#
# PCB Chip Series
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

def select_pins (pins, prefix):
	names = filter (lambda n: n.startswith (prefix), pins.keys())

	return set (map (lambda n: pins[n], names))

