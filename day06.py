#데코레이터 만들기
def test(func):
    def new_function():
        print('start')
        func()
        print('end')
    return new_function

@test
def tmp():
    print("functioning~~")

tmp()
