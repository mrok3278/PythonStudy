'''
placelist.txt 에서 하나씩 꺼내오기
'''

f = open('placelist.txt', 'r', encoding='utf-8')
place_list = f.readlines()
f.close()

# print(place_list)
for place in place_list:
    print(place)
