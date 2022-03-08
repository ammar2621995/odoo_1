#
# def check(fun):
#     def inside(x,y):
#         if y == 0:
#             print("can't be divsion by zero")
#             return
#         return fun(x,y)
#
#     return inside
#
# @check
# def a(x,y):
#     return x/y
#
# print(a(1,0))

#
# def mydec(fun):
#     def inside():
#         return fun()
#     return inside
#
# @mydec
# def my():
#     print("hello")
#
# my()


#
# def mydec(fun):
#     def inside(x):
#         return fun(x)
#     return inside
#
# @mydec
# def my(name):
#     print(f"hello {name}")
#
# my("ammar")



def mydec(*args, **kwargs):
    def inside(*args, **kwargs):
         print("I like", kwargs['like'])
    return inside

@mydec(like='asdfghjk')
def my():
    print(f"hello")

my()

