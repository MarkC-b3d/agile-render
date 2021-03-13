# agile-render
Agile Render add-on

Agile Render Handbook
First I would like to say thank you for your purchase of Agile render from Blendermarket. If you 
have any questions that are not covered in this handbook please feel free to send me a message via 
Blendermarket I’m based in Scotland and operate on GMT timezones so please be understanding if 
I cannot respond to you right away.
------------------------------------------------------------------------------------------------------------------------
Installation:
Agile render installs like most other 3rd party community add-ons but I must stress to you.
DO NOT UNDER ANY CIRCUMSTANCES EXTRACT THE .ZIP ARCHIVE OR ALLOW 
YOUR FILE MANAGER TO PERFORM A SIMILAR OPERATION!
To install Agile render:
Launch Blender > Edit > Preferences > Addons > Install > Navigate to the agilerender zip archive 
and press install add-on with the archive selected.
This is why you don’t extract the archive before installation. Blender extracts the archive for you in 
the correct location.
Agile Render Panel:
The agile render panel can be found in the render properties in blender to the right:Agile Render Config
 Disable auto tile size
This add-on is not required when used with Agile render and in benchmarking I actually 
found it can lead to slower render times.
 Enable / Download SID 
The config will look for the SID add-on. (Super Image Denoiser) if available it will make 
sure it is enabled. If the config cannot find SID it will take you to the gumroad page where it 
can be downloaded for free or for a donation.
 Detect Best Compute Device
This will check if you can use Optix, CUDA or OpenCL for rendering. This operator favours 
Optix for its render speed, if Optix is not possible it will check if CUDA is available. If 
neither is available it will check for OpenCL and if none of these are present the operator 
will determine the best (or only device left rather) to render on is the CPU.
Agile Cycles:
This is a base preset used to get a fast render. It will not touch the sample count so whatever the 
samples are are what it will render with and it does not use any denoising.
Full list of changes:
 Check devices and assign tile sizes
 Enable experimental cycles
 Toggle adaptive sampling
 Set bounces to 16
 Disables clamping and caustics
 Sets volume step rate to 3.5 (for fast nebula rendering)
 Enables simplify camera cull margin to 0.1 and sets the ambient occlusion bounces to 4Agile Render Helper:
This is the preferred way to use the Agile render add-on as it offers greater flexibility than Agile and 
Turbo.
Allows user to decide:
 Which denoiser, if any is used.
 Samples.
 Volume step rate.
 Light paths.
 Toggle on / off caustics and clamping (Caustics can lead to better illumination for interiors).
 Toggle on / off Adaptive Sampling and the Simplify optimisations.
Agile Viewport:
This is an optimised viewport denoising preset. Mostly the same as the agile preset except for the 
following:
 Viewport texture limit set to 1024.
 Tile size set to 32. Cycles is able to render the viewport faster even on GPU with a smaller 
tile size, it is recommended to enable the agile preset AFTER you’re finished with this 
preset.
Turbo Cycles:
This is a preset that is very similar to the agile preset except:
 Samples set to 300 (could actually be more than required but the denoiser needs a decent 
amount in order to produce a clean image)
 Sets the AO bounces in simplify to 1 which is rather quite low. Might need tweaked 
manually for some scenes
