import bpy
import addon_utils
import webbrowser

class Agile_Cycles(bpy.types.Operator):
    bl_idname = "render.agile_cycles"
    bl_label = "Agile Cycles"

    def execute(self, context):
        preferences = bpy.context.preferences.addons['cycles'].preferences
        for device_type in preferences.get_device_types(bpy.context):
            preferences.get_devices_for_type(device_type[0])
        for device in preferences.devices:
            print('Device {} of type {} found'.format(device.name, device.type))
        if device.type:
            'OPTIX'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CUDA'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'OPENCL'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CPU'
            bpy.context.scene.render.tile_x = 32
            bpy.context.scene.render.tile_y = 32
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
        bpy.context.scene.cycles.use_adaptive_sampling = True
        bpy.context.scene.cycles.max_bounces = 16
        bpy.context.scene.cycles.diffuse_bounces = 16
        bpy.context.scene.cycles.glossy_bounces = 16
        bpy.context.scene.cycles.transparent_max_bounces = 16
        bpy.context.scene.cycles.transmission_bounces = 16
        bpy.context.scene.cycles.sample_clamp_indirect = 0
        bpy.context.scene.cycles.sample_clamp_direct = 0
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.cycles.volume_preview_step_rate = 3.5
        bpy.context.scene.cycles.volume_step_rate = 3.5
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.cycles.camera_cull_margin = 0.1
        bpy.context.scene.cycles.ao_bounces_render = 4
        self.report({'INFO'}, "Agile Cycles preset applied.")

        return {'FINISHED'}
#Remember to turn off debug mode for release!
# class Debug_Mode(bpy.types.Operator):
#     bl_idname = "render.debug_mode"
#     bl_label = "Debug Mode"
#     def execute(self, context):

# #Cheap hack to make sure only thing on metadata stamp is rendertime.
#         bpy.context.scene.render.use_stamp_date = False
#         bpy.context.scene.render.use_stamp_frame = False
#         bpy.context.scene.render.use_stamp_frame_range = False
#         bpy.context.scene.render.use_stamp_memory = False
#         bpy.context.scene.render.use_stamp_hostname = False
#         bpy.context.scene.render.use_stamp_lens = False
#         bpy.context.scene.render.use_stamp_scene = False
#         bpy.context.scene.render.use_stamp_marker = False
#         bpy.context.scene.render.use_stamp_filename = False
#         bpy.context.scene.render.use_stamp = True
#         bpy.context.scene.render.use_stamp_render_time = True
#         self.report({'INFO'}, "Debug Mode Activated.")

#         return {'FINISHED'}

class Init_Config(bpy.types.Operator):
        bl_idname = "initalise.cycles_config"
        bl_label = "Agile Render Config"

        dats: bpy.props.BoolProperty(name="Disable Auto Tilesize", default=True)
        esid: bpy.props.BoolProperty(name="Enable / Download SID", default=True)
        dcomd: bpy.props.BoolProperty(name="Detect Best Compute Device", default=True)

        def execute(self, context):
            #Disable Auto Tile Size - Not required with Agile
            if self.dats:
                if 'render_auto_tile_size' in bpy.context.preferences.addons:
                    print('Auto Tile Size Enabled')
                    print('Disabling Auto Tile Size...')
                    addon_utils.disable('render_auto_tile_size', default_set=True)
                else:
                    print('Auto Tile Size Disabled')
            if self.esid:
                if 'SuperImageDenoiser' in bpy.context.preferences.addons:
                    print('Detected SID')
                    addon_utils.enable('SuperImageDenoiser', default_set=True)
                else:
                    print('Sid not detected opening download link')
                    webbrowser.open('https://gumroad.com/l/superimagedenoiser', new=2)
            if self.dcomd:
                preferences = bpy.context.preferences.addons['cycles'].preferences
                for device_type in preferences.get_device_types(bpy.context):
                    preferences.get_devices_for_type(device_type[0])
                for device in preferences.devices:
                    print('Device {} of type {} found'.format(device.name, device.type))
                    if device.type:
                        'OPTIX'
                        bpy.context.preferences.addons[
                    "cycles"
                ].preferences.compute_device_type = "OPTIX"
                    elif device.type:
                        'CUDA'
                        bpy.context.preferences.addons[
                    "cycles"
                ].preferences.compute_device_type = "CUDA"
                    elif device.type:
                        'OPENCL'
                        bpy.context.preferences.addons[
                    "cycles"
                ].preferences.compute_device_type = "OPENCL"

            return {'FINISHED'}

        def invoke(self, context, event):
            wm = context.window_manager
            return wm.invoke_props_dialog(self)

class Agile_Helper(bpy.types.Operator):
    bl_idname = "agile.render_helper"
    bl_label = "Agile Render Helper"



    denoise_enum : bpy.props.EnumProperty(

        name="Denoiser",
        description="Select a denoiser",
        items = [
            ('ID1', "OPTIX", "Enable OPTIX"),
            ('ID2', "OIDN", "Enable OIDN"),
            ('ID3', "NLM", "Enable NLM"),
            ('ID4', "No Denoiser", "Disable Denoising"),
            ('ID5', "Sid Standard", "Sid Standard"),
            ('ID6', "Sid High", "Sid High"),
            ('ID7', "Sid Super", "Sid Super")
        ]
    )

    samples_enum : bpy.props.EnumProperty(

        name="Samples",
        description="Set sample count",
        items = [
            ('SC1', "Fastest - 64", "64 Samples"),
            ('SC2', "Faster - 128", "256 Samples"),
            ('SC3', "Fast - 256", "256 Samples"),
            ('SC4', "Normal - 512", "512 Samples"),
            ('SC5', "High - 768", "768 Samples"),
            ('SC6', "Higher - 1024", "1024 Samples"),
            ('SC7', "Ultra - 1200", "1200 Samples")
        ]
    )


    volume_enum : bpy.props.EnumProperty(

            name="Volumes",
            description="Set step rate",
            items = [
                ('V1', "Fastest Volume - 10 Step Rate", "10 Step Rate"),
                ('V2', "Faster Volume - 8.5 Step Rate", "8.5 Step Rate"),
                ('V3', "Fast Volume - 6.5 Step Rate", "6.5 Step Rate"),
                ('V4', "Medium Volume - 5 Step Rate", "5 Step Rate"),
                ('V5', "High Volume - 3.5 Step Rate", "3.5 Step Rate"),
                ('V6', "Higher Volume - 2.0 Step Rate", "2.0 Step Rate"),
                ('V7', "Ultra Volume - 1.0 Step Rate", "1.0 Step Rate"),
                ('V8', "Ultra High Volume - 0.5 Step Rate", "0.5 Step Rate")
            ]
        )

    bounces_enum: bpy.props.EnumProperty(

        name="Light Paths",
        description="Set light bounces",
        items=[
            ('B1', "No Bounces", "0 Light Path Bounces"),
            ('B2', "2 Bounces", "2 Light Path Bounces"),
            ('B3', "4 Bounces", "4 Light Path Bounces"),
            ('B4', "6 Bounces", "6 Light Path Bounces"),
            ('B5', "8 Bounces", "8 Light Path Bounces"),
            ('B6', "12 Bounces", "12 Light Path Bounces"),
            ('B7', "16 Bounces", "16 Light Path Bounces"),
            ('B8', "20 Bounces", "20 Light Path Bounces"),
            ('B9', "24 Bounces", "24 Light Path Bounces"),
            ('B10', "28 Bounces", "28 Light Path Bounces"),
            ('B11', "32 Bounces", "32 Light Path Bounces")
        ]
    )

#itrue = Interior true toggle.
    itrue: bpy.props.BoolProperty(name="Caustics & Clamping")
#asamp = use_adaptive_sampling
    asamp: bpy.props.BoolProperty(name="Adaptive Sampling", default=True)
#esimp = enable simplify
    esimp: bpy.props.BoolProperty(name="Simplify Optimizations", default=True)

    def execute(self, context):
        preferences = bpy.context.preferences.addons['cycles'].preferences
        for device_type in preferences.get_device_types(bpy.context):
            preferences.get_devices_for_type(device_type[0])
        for device in preferences.devices:
            print('Device {} of type {} found'.format(device.name, device.type))
        if device.type:
            'OPTIX'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CUDA'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'OPENCL'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CPU'
            bpy.context.scene.render.tile_x = 32
            bpy.context.scene.render.tile_y = 32

        if self.denoise_enum == 'ID1':
            bpy.context.scene.cycles.use_denoising = True
            bpy.context.scene.cycles.denoiser = 'OPTIX'
        if self.denoise_enum == 'ID2':
            bpy.context.scene.cycles.use_denoising = True
            bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
        if self.denoise_enum == 'ID3':
            bpy.context.scene.cycles.use_denoising = True
            bpy.context.scene.cycles.denoiser = 'NLM'
        if self.denoise_enum == 'ID4':
            bpy.context.scene.cycles.use_denoising = False
        if self.denoise_enum == 'ID5':
            #Quick sanity check to make sure sid is installed and enabled
            if 'SuperImageDenoiser' in bpy.context.preferences.addons:
                print('Detected SID')
                bpy.context.scene.render.use_compositing = True # make sure compositing is enabled
                addon_utils.enable('SuperImageDenoiser', default_set=True)
                bpy.context.scene.sid_settings.quality = 'STANDARD'
                bpy.ops.object.superimagedenoise()
                # if we're using sid we don't need denoising here
                bpy.context.scene.cycles.use_denoising = False
            else:
                print('Sid not detected opening download link')
                webbrowser.open('https://gumroad.com/l/superimagedenoiser', new=2)
        if self.denoise_enum == 'ID6':
            #Quick sanity check to make sure sid is installed and enabled
            if 'SuperImageDenoiser' in bpy.context.preferences.addons:
                print('Detected SID')
                bpy.context.scene.render.use_compositing = True # make sure compositing is enabled
                addon_utils.enable('SuperImageDenoiser', default_set=True)
                bpy.context.scene.sid_settings.quality = 'HIGH'
                bpy.ops.object.superimagedenoise()
                # if we're using sid we don't need denoising here
                bpy.context.scene.cycles.use_denoising = False
            else:
                print('Sid not detected opening download link')
                webbrowser.open('https://gumroad.com/l/superimagedenoiser', new=2)
        if self.denoise_enum == 'ID7':
            #Quick sanity check to make sure sid is installed and enabled
            if 'SuperImageDenoiser' in bpy.context.preferences.addons:
                print('Detected SID')
                bpy.context.scene.render.use_compositing = True # make sure compositing is enabled
                addon_utils.enable('SuperImageDenoiser', default_set=True)
                bpy.context.scene.sid_settings.quality = 'SUPER'
                bpy.ops.object.superimagedenoise()
                bpy.context.scene.cycles.use_denoising = False # if we're using sid we don't need denoising here
            else:
                print('Sid not detected opening download link')
                webbrowser.open('https://gumroad.com/l/superimagedenoiser', new=2)

        if self.samples_enum == 'SC1':
            bpy.context.scene.cycles.samples = 64
        if self.samples_enum == 'SC2':
            bpy.context.scene.cycles.samples = 128
        if self.samples_enum == 'SC3':
            bpy.context.scene.cycles.samples = 256
        if self.samples_enum == 'SC4':
            bpy.context.scene.cycles.samples = 512
        if self.samples_enum == 'SC5':
            bpy.context.scene.cycles.samples = 768
        if self.samples_enum == 'SC6':
            bpy.context.scene.cycles.samples = 1024
        if self.samples_enum == 'SC7':
            bpy.context.scene.cycles.samples = 1200
        bpy.context.scene.cycles.use_square_samples = False

        if self.itrue:
            bpy.context.scene.cycles.caustics_reflective = True
            bpy.context.scene.cycles.caustics_refractive = True
            bpy.context.scene.cycles.sample_clamp_indirect = 10
            bpy.context.scene.cycles.sample_clamp_direct = 0

        if self.asamp:
            bpy.context.scene.cycles.use_adaptive_sampling = True

        if self.volume_enum == 'V1':
            bpy.context.scene.cycles.volume_preview_step_rate = 10
            bpy.context.scene.cycles.volume_step_rate = 10

        if self.volume_enum == 'V2':
            bpy.context.scene.cycles.volume_preview_step_rate = 8.5
            bpy.context.scene.cycles.volume_step_rate = 8.5

        if self.volume_enum == 'V3':
            bpy.context.scene.cycles.volume_preview_step_rate = 6.5
            bpy.context.scene.cycles.volume_step_rate = 6.5

        if self.volume_enum == 'V4':
            bpy.context.scene.cycles.volume_preview_step_rate = 5
            bpy.context.scene.cycles.volume_step_rate = 5

        if self.volume_enum == 'V5':
            bpy.context.scene.cycles.volume_preview_step_rate = 3.5
            bpy.context.scene.cycles.volume_step_rate = 3.5

        if self.volume_enum == 'V6':
            bpy.context.scene.cycles.volume_preview_step_rate = 2.0
            bpy.context.scene.cycles.volume_step_rate = 2.0

        if self.volume_enum == 'V7':
            bpy.context.scene.cycles.volume_preview_step_rate = 1.0
            bpy.context.scene.cycles.volume_step_rate = 1.0

        if self.volume_enum == 'V8':
            bpy.context.scene.cycles.volume_preview_step_rate = 0.5
            bpy.context.scene.cycles.volume_step_rate = 0.5
        
        if self.bounces_enum == 'B1':
            bpy.context.scene.cycles.max_bounces = 0
            bpy.context.scene.cycles.diffuse_bounces = 0
            bpy.context.scene.cycles.glossy_bounces = 0
            bpy.context.scene.cycles.transparent_max_bounces = 0
            bpy.context.scene.cycles.transmission_bounces = 0
 
        if self.bounces_enum == 'B2':
            bpy.context.scene.cycles.max_bounces = 2
            bpy.context.scene.cycles.diffuse_bounces = 2
            bpy.context.scene.cycles.glossy_bounces = 2
            bpy.context.scene.cycles.transparent_max_bounces = 2
            bpy.context.scene.cycles.transmission_bounces = 2

        if self.bounces_enum == 'B3':
            bpy.context.scene.cycles.max_bounces = 4
            bpy.context.scene.cycles.diffuse_bounces = 4
            bpy.context.scene.cycles.glossy_bounces = 4
            bpy.context.scene.cycles.transparent_max_bounces = 4
            bpy.context.scene.cycles.transmission_bounces = 4

        if self.bounces_enum == 'B4':
            bpy.context.scene.cycles.max_bounces = 6
            bpy.context.scene.cycles.diffuse_bounces = 6
            bpy.context.scene.cycles.glossy_bounces = 6
            bpy.context.scene.cycles.transparent_max_bounces = 6
            bpy.context.scene.cycles.transmission_bounces = 6
  
        if self.bounces_enum == 'B5':
            bpy.context.scene.cycles.max_bounces = 8
            bpy.context.scene.cycles.diffuse_bounces = 8
            bpy.context.scene.cycles.glossy_bounces = 8
            bpy.context.scene.cycles.transparent_max_bounces = 8
            bpy.context.scene.cycles.transmission_bounces = 8
  
        if self.bounces_enum == 'B6':
            bpy.context.scene.cycles.max_bounces = 12
            bpy.context.scene.cycles.diffuse_bounces = 12
            bpy.context.scene.cycles.glossy_bounces = 12
            bpy.context.scene.cycles.transparent_max_bounces = 12
            bpy.context.scene.cycles.transmission_bounces = 12
  
        if self.bounces_enum == 'B7':
            bpy.context.scene.cycles.max_bounces = 16
            bpy.context.scene.cycles.diffuse_bounces = 16
            bpy.context.scene.cycles.glossy_bounces = 16
            bpy.context.scene.cycles.transparent_max_bounces = 16
            bpy.context.scene.cycles.transmission_bounces = 16
  
        if self.bounces_enum == 'B8':
            bpy.context.scene.cycles.max_bounces = 20
            bpy.context.scene.cycles.diffuse_bounces = 20
            bpy.context.scene.cycles.glossy_bounces = 20
            bpy.context.scene.cycles.transparent_max_bounces = 20
            bpy.context.scene.cycles.transmission_bounces = 20
  
        if self.bounces_enum == 'B9':
            bpy.context.scene.cycles.max_bounces = 24
            bpy.context.scene.cycles.diffuse_bounces = 24
            bpy.context.scene.cycles.glossy_bounces = 24
            bpy.context.scene.cycles.transparent_max_bounces = 24
            bpy.context.scene.cycles.transmission_bounces = 24
  
        if self.bounces_enum == 'B10':
            bpy.context.scene.cycles.max_bounces = 28
            bpy.context.scene.cycles.diffuse_bounces = 28
            bpy.context.scene.cycles.glossy_bounces = 28
            bpy.context.scene.cycles.transparent_max_bounces = 28
            bpy.context.scene.cycles.transmission_bounces = 28
  
        if self.bounces_enum == 'B11':
            bpy.context.scene.cycles.max_bounces = 32
            bpy.context.scene.cycles.diffuse_bounces = 32
            bpy.context.scene.cycles.glossy_bounces = 32
            bpy.context.scene.cycles.transparent_max_bounces = 32
            bpy.context.scene.cycles.transmission_bounces = 32
        
        if self.esimp:

            bpy.context.scene.render.use_simplify = True
            bpy.context.scene.cycles.camera_cull_margin = 0.1
            bpy.context.scene.cycles.ao_bounces_render = 2



#quick sanity check to make sure cycles and experimental is enabled
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
        self.report({'INFO'}, "Preset Applied.")

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class Agile_Viewport(bpy.types.Operator):
    bl_idname = "render.agile_viewport"
    bl_label = "Agile Viewport"
    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
        bpy.context.scene.cycles.use_square_samples = False
        bpy.context.scene.cycles.use_adaptive_sampling = True
        bpy.context.scene.cycles.use_preview_denoising = True
        bpy.context.scene.cycles.preview_denoiser = 'AUTO'
        bpy.context.scene.cycles.max_bounces = 16
        bpy.context.scene.cycles.diffuse_bounces = 16
        bpy.context.scene.cycles.glossy_bounces = 16
        bpy.context.scene.cycles.transparent_max_bounces = 16
        bpy.context.scene.cycles.transmission_bounces = 16
        bpy.context.scene.cycles.sample_clamp_indirect = 0
        bpy.context.scene.cycles.sample_clamp_direct = 0
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.cycles.volume_preview_step_rate = 3.5
        bpy.context.scene.cycles.volume_step_rate = 3.5
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.cycles.camera_cull_margin = 0.1
        bpy.context.scene.cycles.texture_limit = '1024'
        bpy.context.scene.render.tile_x = 32
        bpy.context.scene.render.tile_y = 32

        self.report({'INFO'}, "DO NOT ENABLE FOR FINAL RENDER!")

        return {'FINISHED'}

class Turbo_Cycles(bpy.types.Operator):
    bl_idname = "render.turbo_cycles"
    bl_label = "Turbo Cycles"

    def execute(self, context):
        preferences = bpy.context.preferences.addons['cycles'].preferences
        for device_type in preferences.get_device_types(bpy.context):
            preferences.get_devices_for_type(device_type[0])
        for device in preferences.devices:
            print('Device {} of type {} found'.format(device.name, device.type))
        if device.type:
            'OPTIX'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CUDA'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'OPENCL'
            bpy.context.scene.render.tile_x = 256
            bpy.context.scene.render.tile_y = 256
        elif device.type:
            'CPU'
            bpy.context.scene.render.tile_x = 32
            bpy.context.scene.render.tile_y = 32
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
        bpy.context.scene.cycles.use_adaptive_sampling = True
        bpy.context.scene.cycles.use_square_samples = False #toggles to false because next command for 300 samples is ok in most cases.
        bpy.context.scene.cycles.samples = 300
        preferences = bpy.context.preferences.addons['cycles'].preferences
        for device_type in preferences.get_device_types(bpy.context):
            preferences.get_devices_for_type(device_type[0])
        for device in preferences.devices:
            print('Device {} of type {} found'.format(device.name, device.type))
            if device.type:
                'OPTIX'
                bpy.context.scene.cycles.denoiser = 'OPTIX'
            elif device.type:
                'CUDA'
                bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
            elif device.type:
                'OPENCL'
                bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
        bpy.context.scene.cycles.use_denoising = True
        bpy.context.scene.cycles.max_bounces = 16
        bpy.context.scene.cycles.diffuse_bounces = 16
        bpy.context.scene.cycles.glossy_bounces = 16
        bpy.context.scene.cycles.transparent_max_bounces = 16
        bpy.context.scene.cycles.transmission_bounces = 16
        bpy.context.scene.cycles.sample_clamp_indirect = 0
        bpy.context.scene.cycles.sample_clamp_direct = 0
        bpy.context.scene.cycles.caustics_reflective = False
        bpy.context.scene.cycles.caustics_refractive = False
        bpy.context.scene.cycles.volume_preview_step_rate = 3.5
        bpy.context.scene.cycles.volume_step_rate = 3.5
        bpy.context.scene.render.use_simplify = True
        bpy.context.scene.cycles.camera_cull_margin = 0.1
        bpy.context.scene.cycles.ao_bounces_render = 1
        self.report({'INFO'}, "Turbo Cycles preset applied.")

        return {'FINISHED'}
