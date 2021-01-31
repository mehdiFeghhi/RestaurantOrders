import collections

'''
-1 = Impossible
-2 = Ambiguous
0 = UnAmbiguous 
'''


def find_solution(menu, money_you_have, size_menu):
    list_result = [[-1] for j in range(money_you_have + 1)]
    list_result[0] = [0]
    sale = 0

    for i in range(money_you_have+1):

        item_see = False
        # print(sale)
        for f in range(size_menu):

            k = menu[f][1]
            if sale >= k:

                if list_result[sale - k][0] == -2:

                    list_result[i][0] = -2
                    break

                elif list_result[sale - k][0] == 0:


                    heap = list_result[sale - k] + [menu[f][0]]

                    if not item_see:

                        list_result[i] = list_result[sale - k] + [menu[f][0]]

                        # i[1] = 1

                        item_see = True

                    else:

                        if collections.Counter(heap) != collections.Counter(list_result[i]):

                            list_result[i][0] = -2

                            break
            else:
                break

        sale += 1
    return list_result


# def print_heap(heap):
#     heap.sort()
#     st = ""
#     for i in heap:
#         st += str(i) + " "
#     print(st.rstrip())


def main():
    number_item = int(input())

    menu = list(enumerate(list(map(int, input().split())), 1))
    # menu = list(map(int, input().split()))
    menu.sort(key=lambda x: x[1])

    input()
    money_you_have = list(map(int, input().split()))
    maxim = max(money_you_have)

    what_is_situation = find_solution(menu, maxim, number_item)

    for money in money_you_have:

        if what_is_situation[money][0] == 0:

            what_is_situation[money].sort()
            st = ""
            for i in what_is_situation[money]:
                if i == 0:
                    continue
                st += str(i) + " "
            print(st.rstrip())


        elif what_is_situation[money][0] == -2:
            print("Ambiguous")



        else:
            print("Impossible")


if __name__ == '__main__':
    main()
