from alpha import alpha_function1, alpha_function2, alpha_function3


def alpha_function1_test():
    print("\n Inside alpha function 1 test \n")

    param1 = 1
    param2 = 2
    alpha_function1(param1, param2)

    return "return from alpha_function1 test"


def alpha_function2_test():
    print("\n Inside alpha function 2 test \n")

    param1 = 1
    param2 = 2

    alpha_function2(param1, param2)
    return "return from alpha_function2 test"


def alpha_function3_test():
    print("\n Inside alpha function 3 test \n")

    param1 = 1
    param2 = 2

    alpha_function3(param1, param2)
    return "return from alpha_function3 test"


if __name__ == "__main__":
    alpha_function1_test()
    alpha_function2_test()
    alpha_function3_test()
