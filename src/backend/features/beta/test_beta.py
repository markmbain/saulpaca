from beta import beta_function1, beta_function2, beta_function3


def beta_function1_test():
    print("\n Inside beta function 1 test \n")

    param1 = 1
    param2 = 2
    beta_function1(param1, param2)

    return "return from beta_function1 test"


def beta_function2_test():
    print("\n Inside beta function 2 test \n")

    param1 = 1
    param2 = 2

    beta_function2(param1, param2)
    return "return from beta_function2 test"


def beta_function3_test():
    print("\n Inside beta function 3 test \n")

    param1 = 1
    param2 = 2

    beta_function3(param1, param2)
    return "return from beta_function3 test"


if __name__ == "__main__":
    beta_function1_test()
    beta_function2_test()
    beta_function3_test()
