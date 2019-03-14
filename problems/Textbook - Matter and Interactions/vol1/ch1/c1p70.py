
## Matter & Interactions, Fourth Edition; Computational Problem Sets
## Chapter 1, Problem #70
## Implementation by: Alexander Ahmann, alexander.ahmann@live.lagcc.cuny.edu

## PROBLEM:
## Write a VPython program that represents the x, y, and z
## axes by three cylinders of different colors. The display from one
## possible solution is shown in Figure 1.63
 
## SOLUTION:
## Figure 1.63 is shown on page 43 of the textbook and the reader is to create 

from visual import *

def render_this(thing_name, position, ax, colour):
	print("Rendering the", thing_name, "thing...")
	thing_rendered = cylinder(pos=position, axis=ax, radius=.1)
	thing_rendered.color = colour

parameters = [
	["x axis", vector(-1,0,0), vector(+2,0,0), vector(255,0,0)],
	["y axis", vector(0,-1,0), vector(0,+2,0), vector(0,255,0)],
	["z axis", vector(0,0,-1), vector(0,0,+2), vector(0,0,255)]
]

for n, k in enumerate(parameters):
	render_this(k[0], k[1], k[2], k[3])

