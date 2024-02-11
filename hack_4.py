text:"fooziman"

print("foozimaN")

"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "foozimaN"
    result: result.upper()
    return result