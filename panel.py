import bpy
import addon_utils
import webbrowser

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Agile Cycles"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        # Big render button
        layout.label(text="DEBUG MODE", icon='ERROR')
        row = layout.row()
        row.scale_y = 1.0
        row.operator("render.debug_mode")
        # Create a simple row.
        # Big render button
        layout.label(text="Init Config", icon='ERROR')
        row = layout.row()
        row.scale_y = 1.0
        row.operator("initalise.cycles_config")

        layout.label(text="Agile Cycles:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("render.speedy_cycles")

        # Different sizes in a row
        layout.label(text="Render Helper:")
        row = layout.row(align=True)
        row.operator("agile.render_helper")

        layout.label(text="Speedy Viewport:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("render.agile_viewport")

        layout.label(text="Turbo Cycles:")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("render.turbo_cycles")
