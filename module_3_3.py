

#def print_params(a=1, b='строка', c=True):
 #   print (a, b, c)
#print_params ()
#print_params (2, b=5, c=4, d='hello') - выводит ошибку по причине различного количества параметров 
#print_params(b=25)
#print_params(c=[1,2,3])

def print_params(a=1, b='строка', c=True):
        print (a, b, c)
values_list = [11, '12', False]
values_dict = {'a':5, 'b':'five', 'c':True}
print_params (*values_list)
print_params (**values_dict)
values_list_2 = ['replace', 7]
print_params(*values_list_2,42)
