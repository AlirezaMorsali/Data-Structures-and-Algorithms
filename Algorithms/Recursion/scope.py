

def inception_run():
    counter = 0

    def inception():
        nonlocal counter
        if counter > 3:
            print("Done")
            # return
        else:
            counter += 1
            inception()

    return inception()


inception_run()

# b = 1


# def func():
#     global a
#     a = 1
#     print(a)
#     print(b)
#     return


# func()
# print(a)
