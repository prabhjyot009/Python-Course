x=lambda y:y+15
print(x(10))

z=lambda x,y:x*y
print(z(6,8))

nums=[1,2,3,4,5,6,7,8,9,10]
print("Orignal List",nums)
even_nums=list(filter(lambda x: x%2==0,nums))
odd_nums=list(filter(lambda x: x%2!=0,nums))
print("Even list:",even_nums)
print("Odd list:",odd_nums)
