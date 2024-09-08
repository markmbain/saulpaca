from gamma import gamma_function1, gamma_function2, gamma_function3


def gamma_function1_test():
    print("\n Inside gamma function 1 test \n")

    param1 = 1
    param2 = 2
    gamma_function1(param1, param2)

    return "return from gamma_function1 test"


def gamma_function2_test():
    print("\n Inside gamma function 2 test \n")

    param1 = 1
    param2 = 2

    gamma_function2(param1, param2)
    return "return from gamma_function2 test"


def gamma_function3_test():
    print("\n Inside gamma function 3 test \n")

    param1 = 1
    param2 = 2

    gamma_function3(param1, param2)
    return "return from gamma_function3 test"


if __name__ == "__main__":
    gamma_function1_test()
    gamma_function2_test()
    gamma_function3_test()
