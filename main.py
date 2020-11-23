import bpy
import math
import random

print("Hello World")

x = 2

for obj in bpy.data.objects:
    print(obj.name + " " + obj.type)
    obj.location = [x,0,0]
    x = x + 5

def add_cube(name, position, rotation, scale):
    bpy.ops.mesh.primitive_cube_add()
    rtn = bpy.context.selected_objects[0]
    rtn.name = name
    rtn.location = position
    rtn.rotation_euler = [
    math.radians(rotation[0]),
    math.radians(rotation[1]),
    math.radians(rotation[2])
    ]
    rtn.scale = scale
    return rtn
 
add_cube("Stacey", [0,0,0],[0,45,0],[10,10,0.1])


def add_stairs(count):
    pos = [0,0,0]

    for x in range(count):
        pos[2] += 1
        pos[0] += 2
        rx = random.randint(0,25)
        ry = random.randint(0,25)
        rz = random.randint(0,25)
        add_cube("Bob", pos,[rx,ry,rz],[1,1,0.5])
    
add_stairs(50)
