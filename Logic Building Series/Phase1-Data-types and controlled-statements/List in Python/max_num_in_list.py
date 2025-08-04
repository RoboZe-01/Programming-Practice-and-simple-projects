
# Problem statement : Find max and min number in list 


# Easy and reliable solution 
# First sort the list and then apply indexing 

# def sort_lst (lst):
#     a = lst.sort
     
#     return print(a)


# ex_lst = [2,4,1,5]
# lst_call = sort_lst(ex_lst)
# print(lst_call)

def sort_list(lst):
    lst.sort()
    return lst

a = [9,6,4,8,7]
print(sort_list(a))

sorted_list = sort_list(a)
max_val = sorted_list[-1]
print(max_val)