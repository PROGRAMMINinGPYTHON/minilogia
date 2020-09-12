# def ile(n):
#     a = 1
#     for i in range(1,n):
#         if i/12 == 0:
#             a = a-10
#         else:
#             if i%2 == 0:
#                 a = a+3
#             else:
#                 a = a-1
#     return a
# print(ile(4))
# print(ile(14))
# print(ile(100))

def ile(n):
    a = 2
    for i in range(n):
        if i%2 == 0:
            a = a-1
        else:
            a = a+3
        if i%12 == 0:
            a = a-9
    a = a+9



    print(a)

ile(5)
