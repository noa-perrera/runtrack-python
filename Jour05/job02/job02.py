def rectangle(width, height):
    print('-' * width)
    for i in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    print('-' * width)
rectangle(10, 3)