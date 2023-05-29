#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            divresult = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            divresult = 0
            print("Wrong type")
        except ZeroDivisionError:
            divresult = 0
            print("division by 0")
        except IndexError:
            divresult = 0
            print("out of range")
        finally:
            result.append(divresult)
    return (result)

