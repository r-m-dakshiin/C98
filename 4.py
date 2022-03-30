from multiprocessing.spawn import old_main_modules


def Square():
    new_value = 4 ** 2
    print(new_value)
Square()

def Add(x, y):
    old_value = x + y
    print(old_value)
Add(2, 4)