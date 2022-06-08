def selection_sort(arr_list):

    for i in range(len(arr_list)):
        min_index = i


    # nested for loop -->
        for j in range(i + 1, len(arr_list)):
            if arr_list[j] < arr_list[min_index]:
                min_index = j

        arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]

    return arr_list


arr_list = [21,56,2, 6, 9, 33, 3]

print("The sorted list is: ", selection_sort(arr_list))