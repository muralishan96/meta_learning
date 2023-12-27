try:
    with open('test.txt','a') as file:
        file.writelines(['\n Chuchu is my world ','\nAkilandeswari my mom'])
except FileNotFoundError as e:
    print('error',e)