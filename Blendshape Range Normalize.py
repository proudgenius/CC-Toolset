import bpy

# Get the active object (assuming the object with shape keys is active)
obj = bpy.context.active_object

# Check if the object has shape keys
if obj.data.shape_keys:
    # Iterate through each shape key
    for key_block in obj.data.shape_keys.key_blocks:
        # Set the range minimum value to zero
        key_block.slider_min = 0.0
        
        # Set the range maximum value to 1
        key_block.slider_max = 1.0
        
    print("Set the range minimum to 0 and the range maximum to 1 for all shape keys.")
else:
    print("The object does not have shape keys.")
