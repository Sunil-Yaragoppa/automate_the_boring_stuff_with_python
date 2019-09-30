# Comma Code
# input : ['apples','bananas','tofu','cats']
# output : apples, bananas, tofu, and, cats
def comma_code(mylist):
    mylist.insert(-1,'and')
    print(mylist)
    s= ', '
    s=s.join(mylist)
    my_string = s.replace('and,' , 'and')
    return my_string    

spam = ['apples','bananas','tofu','cats']
new_string = comma_code(spam)
print(new_string)
