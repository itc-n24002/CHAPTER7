def test_function():
    try:
        print('try')
        return
    except:
        print('except')
    finally:
        print('finally')

test_function()
