#!/usr/bin/python3
#
# PCB Grid Helpers
#
# Copyright (c) 2025 Alexei A. Smekalkine <ikle@ikle.ru>
#
# SPDX-License-Identifier: BSD-2-Clause
#

#
# Grid Calculator
#
# The grid cell is a parallelogram with sides OA and OB/m. The coordinates on
# the grid are specified by a pair of numbers (i, j), the origin of
# coordinates is at point O.
#
def anchor (O, A, B, m, i, j):
	(Ox, Oy) = O
	(Ax, Ay) = A
	(Bx, By) = B
	(ax, ay) = (Ax - Ox, Ay - Oy)
	(bx, by) = (Bx - Ox, By - Oy)
	(dx, dy) = (bx /  m, by /  m)

	return (Ox + ax * i + dx * j, Oy + ay * i + dy * j)

