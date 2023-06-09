x=lambda y:y+15
print(x(10))

z=lambda x,y:x*y
print(z(6,8))

# nums=[1,2,3,4,5,6,7,8,9,10]
# print("Orignal List",nums)
# even_nums=list(filter(lambda x: x%2==0,nums))
# print("Even list:",even_nums)

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def sorted_array_to_bst(nums):
    
#     if not nums:
#         return None
#     mid_val = len(nums)//2
#     node = TreeNode(nums[mid_val])
    
#     node.left = sorted_array_to_bst(nums[:mid_val])
#     node.right = sorted_array_to_bst(nums[mid_val+1:])
#     return node

# def preOrder(node): 
#     if not node: 
#         return      
#     print(node.val)
#     preOrder(node.left) 
#     preOrder(node.right)   
    
# result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
# preOrder(result)
# def binary_search(item_list,item):
# 	first = 0
# 	last = len(item_list)-1
# 	found = False
# 	while( first<=last and not found):
# 		mid = (first + last)//2
# 		if item_list[mid] == item :
# 			found = True
# 		else:
# 			if item < item_list[mid]:
# 				last = mid - 1
# 			else:
# 				first = mid + 1	
# 	return found

# item_list=[]
# size=int(input("Enter size:"))
# for i in range(size):
#     val=(int(input("Enter elements:")))
#     item_list.append(val)
# item=int(input("Enter elements to be search:"))
# call=binary_search(item_list,item)
# print(call)

