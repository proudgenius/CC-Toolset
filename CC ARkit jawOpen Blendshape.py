import bpy

# Get the active object (assuming the object with shape keys is active)
obj = bpy.context.active_object

# Define the names of the source blendshapes
source_shape1 = "jawOpen_OLD"
source_shape2 = "Merged_Open_Mouth"

# Define the name of the new blendshape
new_shape_name = "jawOpen"

# Check if the source blendshapes exist
if source_shape1 in obj.data.shape_keys.key_blocks and source_shape2 in obj.data.shape_keys.key_blocks:
    # Set the source blendshapes to their maximum values
    obj.data.shape_keys.key_blocks[source_shape1].value = 1.0
    obj.data.shape_keys.key_blocks[source_shape2].value = 1.0

    # Create a new shape key based on the mix
    new_shape_key = obj.shape_key_add(name=new_shape_name, from_mix=True)

    # Reset the source blendshapes to their original values
    obj.data.shape_keys.key_blocks[source_shape1].value = 0.0
    obj.data.shape_keys.key_blocks[source_shape2].value = 0.0

    print(f"Created '{new_shape_name}' from the maximum values of '{source_shape1}' and '{source_shape2}'.")
else:
    print("One or both of the source blendshapes do not exist.")
