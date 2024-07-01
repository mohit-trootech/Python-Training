import ast

exp = "7 * 5 + 6"
c = ast.parse(exp, mode="eval")
print(eval(compile(c, "", mode="eval")))
print(ast.dump(c))

multiline_ast = ast.parse(
    """  
flowers = ['rose', 'sunflower', 'lavender', 'daisy', 'lily', 'daffodil', 'tulip', 'jasmine', 'rose', 'orchid', 'lavender', 'daffodil', 'daisy', 'lily', 'rose', 'panzy', 'marigold', 'lotus', 'lavender', 'tulip', 'jasmine', 'marigold', 'daffodil']  
bouquet={}
for flower in flowers:  
    if flower not in bouquet:
        bouquet[flower]=0
    bouquet[flower]+=1
print(bouquet) 
"""
)
print(ast.dump(multiline_ast))
