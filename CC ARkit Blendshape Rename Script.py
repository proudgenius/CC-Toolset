import bpy

# Define List 1 and List 2
list1 = [
    "A01_Brow_Inner_Up", "A02_Brow_Down_Left", "A03_Brow_Down_Right", "A04_Brow_Outer_Up_Left",
    "A05_Brow_Outer_Up_Right", "A06_Eye_Look_Up_Left", "A07_Eye_Look_Up_Right", "A08_Eye_Look_Down_Left",
    "A09_Eye_Look_Down_Right", "A10_Eye_Look_Out_Left", "A11_Eye_Look_In_Left", "A12_Eye_Look_In_Right",
    "A13_Eye_Look_Out_Right", "A14_Eye_Blink_Left", "A15_Eye_Blink_Right", "A16_Eye_Squint_Left",
    "A17_Eye_Squint_Right", "A18_Eye_Wide_Left", "A19_Eye_Wide_Right", "A20_Cheek_Puff", "A21_Cheek_Squint_Left",
    "A22_Cheek_Squint_Right", "A23_Nose_Sneer_Left", "A24_Nose_Sneer_Right", "A25_Jaw_Open", "A26_Jaw_Forward",
    "A27_Jaw_Left", "A28_Jaw_Right", "A29_Mouth_Funnel", "A30_Mouth_Pucker", "A31_Mouth_Left", "A32_Mouth_Right",
    "A33_Mouth_Roll_Upper", "A34_Mouth_Roll_Lower", "A35_Mouth_Shrug_Upper", "A36_Mouth_Shrug_Lower",
    "A37_Mouth_Close", "A38_Mouth_Smile_Left", "A39_Mouth_Smile_Right", "A40_Mouth_Frown_Left",
    "A41_Mouth_Frown_Right", "A42_Mouth_Dimple_Left", "A43_Mouth_Dimple_Right", "A44_Mouth_Upper_Up_Left",
    "A45_Mouth_Upper_Up_Right", "A46_Mouth_Lower_Down_Left", "A47_Mouth_Lower_Down_Right", "A48_Mouth_Press_Left",
    "A49_Mouth_Press_Right", "A50_Mouth_Stretch_Left", "A51_Mouth_Stretch_Right", "A52_Tongue_Out"
]

list2 = [
    "browInnerUp", "browDownLeft", "browDownRight", "browOuterUpLeft", "browOuterUpRight", "eyeLookUpLeft",
    "eyeLookUpRight", "eyeLookDownLeft", "eyeLookDownRight", "eyeLookOutLeft", "eyeLookInLeft", "eyeLookInRight",
    "eyeLookOutRight", "eyeBlinkLeft", "eyeBlinkRight", "eyeSquintLeft", "eyeSquintRight", "eyeWideLeft",
    "eyeWideRight", "cheekPuff", "cheekSquintLeft", "cheekSquintRight", "noseSneerLeft", "noseSneerRight",
    "jawOpen_OLD", "jawForward", "jawLeft", "jawRight", "mouthFunnel", "mouthPucker", "mouthLeft", "mouthRight",
    "mouthRollUpper", "mouthRollLower", "mouthShrugUpper", "mouthShrugLower", "mouthClose", "mouthSmileLeft",
    "mouthSmileRight", "mouthFrownLeft", "mouthFrownRight", "mouthDimpleLeft", "mouthDimpleRight", "mouthUpperUpLeft",
    "mouthUpperUpRight", "mouthLowerDownLeft", "mouthLowerDownRight", "mouthPressLeft", "mouthPressRight",
    "mouthStretchLeft", "mouthStretchRight", "tongueOut"
]

# Get the active object (assuming the blendshape object is active)
obj = bpy.context.active_object

# Iterate through the blendshape names and rename them
for old_name, new_name in zip(list1, list2):
    if old_name in obj.data.shape_keys.key_blocks:
        key_block = obj.data.shape_keys.key_blocks[old_name]
        key_block.name = new_name

print("Blendshape names have been renamed.")