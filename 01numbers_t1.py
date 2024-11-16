
def function(a,b):
     result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
     rounded_result = round(result,2)
     return rounded_result

a=2
b=3
result = function(a,b)
print(result)