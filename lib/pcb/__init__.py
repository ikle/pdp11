#!/usr/bin/python3
#
# PCB Generic Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

import math

def rotate (O, Ax, Ay, angle):
	(Ox, Oy) = O
	(ax, ay) = (Ax - Ox, Ay - Oy)

	a = math.pi * angle / 180
	(s, c) = (math.sin (a), math.cos (a))

	return (Ox + ax * c - ay * s, Oy + ax * s + ay * c)

