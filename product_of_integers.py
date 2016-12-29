def get_products_of_all_ints_except_at_index(list):
    
    forward_list = [1,]
    backward_list = [1,]

    forward_product = 1
    backward_product = 1

    for n in xrange(0, len(list)-1):
        forward_product = forward_product * list[n]
        forward_list.append(forward_product)

    for n in xrange(len(list)-1, 0, -1):
        backward_product = backward_product * list[n]
        backward_list.append(backward_product)

    combined_list = []
    for n in range(len(list)):
        combined_list.append(forward_list[n]*backward_list[len(list)-(n+1)])

    return combined_list


#optimized time O(n), space O(n)

def get_products_of_all_ints_except_at_index(list):
     
    new_list = [None] * len(list)
    forward_product = 1
    backward_product = 1


    for n in xrange(0, len(list)):

        new_list[n] = forward_product
        forward_product = forward_product * list[n]
        

    for n in xrange(len(list)-1, 0, -1):
        backward_product = backward_product * list[n]
        new_list[n-1] = new_list[n-1]*backward_product

    return new_list

test_list = [1, 7, 3, 4]
print get_products_of_all_ints_except_at_index(test_list)

