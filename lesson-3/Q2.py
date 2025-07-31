# WAP to fill letter template given below with name and date

letter="""
dear <|name|>
you are selected!
<|date|>
"""
user=input("enter you name:")
edit = (letter.replace("<|name|>" , user).replace("<|date|>","7/31")) #chaining the replace value
print(edit)

