def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(2,'число', False)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = (5, 'МИР', True)
values_dict = {'a':1, 'b':'ок', 'c':False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = (6.54, True)
print_params(*values_list_2, 42)
