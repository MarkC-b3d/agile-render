bl_info = {
    "name": "Agile Render",
    "description": "Agile Render Presets",
    "author": "Mark C",
    "version": (0, 0, 2),
    "blender": (2, 92, 0),
    "location": "Render Panel",
    "warning": "",
    "wiki_url": "https://github.com/MarkC-b3d/agile-render/issues",
    "category": "Render" }

import bpy
import addon_utils
import webbrowser
from . panel import AgilePanel
from . operators import *

def register():
    bpy.utils.register_class(AgilePanel)
    # bpy.utils.register_class(Debug_Mode) # To be enabled in dev builds and for benchmarking
    bpy.utils.register_class(Agile_Cycles)
    bpy.utils.register_class(Agile_Viewport)
    bpy.utils.register_class(Agile_Helper)
    bpy.utils.register_class(Init_Config)
    bpy.utils.register_class(Turbo_Cycles)


def unregister():
    bpy.utils.unregister_class(AgilePanel)
    # bpy.utils.unregister_class(Debug_Mode) # To be enabled in dev builds and for benchmarking
    bpy.utils.unregister_class(Agile_Cycles)
    bpy.utils.unregister_class(Agile_Viewport)
    bpy.utils.unregister_class(Agile_Helper)
    bpy.utils.unregister_class(Init_Config)
    bpy.utils.unregister_class(Turbo_Cycles)


if __name__ == "__main__":
    register()
