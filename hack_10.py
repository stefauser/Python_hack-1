

"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
def fn_hack_10():
    result = "fooziman"
    new_result=[]

    for i in  result:
        new_result.append(i)
        new_result.append("F")
        new_result.append("0")
        new_result.append("0")
        new_result.append("Z")
        new_result.append("I")
        new_result.append("M")
        new_result.append("@")
        new_result.append("N")

    return new_result

r= fn_hack_10
print(r)


   



    


    