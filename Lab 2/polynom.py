# for user input
global p_,q_,x 

# for test
p = [2, 0, 1] 
q = [-2, 1, 0, 0, 1] 
p0 = [2, 0, 1, 0] 
q0 = [0, 0, 0] 


def polynomial_to_string(polynom: list) -> str:
    if not polynom:
        # print("Empty list polynomial_to_string")
        return "0"
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    degree = 0
    str_polynomial = ""
    # First collect a list of terms
    for coeff in polynom:
        # if the coefficient is zero then skip the whole term and jump to next degree
        if is_zero(polynom[degree]):
            degree += 1
            continue
        # the first term is special case without any x
        if degree == 0:
            str_polynomial += str(coeff)
        # the first degree is also special without any power (^)
        elif degree == 1:
            str_polynomial += " + " + \
                (str(coeff) if (not str(coeff) in [
                 "1", "-1"]) else "-" if (str(coeff) == "-1") else "") + "x"
        # all terms after first degree have x to the power of degree
        elif degree > 1:
            str_polynomial += " + " + \
                (str(coeff) if (not str(coeff) in ["1","-1"])
                 else "-" if (str(coeff) == "-1") else "") + 'x^' + str(degree)
        degree += 1
    
    # will return the polynomial_string if it's not empty, else will return "0"
    return str_polynomial if (str_polynomial != "") else "0"


def get_polynomial(polynom_name: str) -> list:
    result = []
    try:
        # takes a list of coefficients as an input separated by a space
        result = [int(coeff) for coeff in input(
            f"Enter all coefficients for polynomial ({polynom_name}): ").strip().split(' ')]
    except ValueError as e:
        print("Empty list detected! returning 0")
    return result


def is_zero(coeff: int) -> bool:
    # checks if coefficient is zero and return a bool
    if coeff == 0:
        return True
    return False


def drop_zeroes(polynom: list) -> list:
    result = []
    amount_zeros = 0
    # loop from the end of the list
    for coeff in reversed(polynom):
        # count how many zeros are there at the end of the list 
        # and store amount zeros in amount_zeros variable
        if coeff == 0:
            amount_zeros += 1
            continue
        # stop counting once there is some value greater or less than 0
        else:
            break
    # copy the original list to the result list
    # while ignoring the last (amount_zeros) indexes
    # which are stored in our variable
    # e.g. list_length = 8 (9 items) , amount_zeros = 3 
    # 8 - 3 = 5 , this will add first 6 items in the list
    for i in range(len(polynom)-amount_zeros):
        result.append(polynom[i])
    return result


def eq_poly(p_polynom: list, q_polynom: list) -> bool:
    # drop all zeros from the lists
    p_polynom = drop_zeroes(p_polynom)
    q_polynom = drop_zeroes(q_polynom)
    # by comparing the lists' length as a first check
    # this can easily detect if the lists can be equal or not
    if len(p_polynom) == len(q_polynom):
        length = len(p_polynom)
        # checking equality of each item in the lists
        for i in range(length):
            if p_polynom[i] == q_polynom[i]:
                continue
            # if any items of a certain index in the lists
            # are not equal we return False 
            else:
                return False
        return True
    return False


def eval_poly(polynom: list, x: int) -> int:
    grade = 0
    result = 0
    for coeff in polynom:
        # for first term, add the coefficient only
        if coeff == 0:
            result += coeff
            grade += 1
        else:
            # calculation of the term by replacing the x value
            result += ((coeff) * ((x) ** grade))
            grade += 1
    return result


def neg_poly(polynom: list) -> list:
    result = []
    for coeff in polynom:
        # multiplying the term with -1 will change its sign, then add it to list
        result.append(coeff*-1)
    return result


def add_poly(p_polynom: list, q_polynom: list) -> list:
    # compare the lists and get longest length
    length = get_longest_list_length(p_polynom, q_polynom)
    result = []
    # loop from 0 to the highest possible index
    for i in range(length):
        # if both lists have the index 
        # add the sum of the coefficients to the reuslt list
        if i < len(p_polynom) and i < len(q_polynom):
            result.append(p_polynom[i]+q_polynom[i])
        # if only p_polynom list have the index
        # add p_polynom's coefficient to the result list
        elif i < len(p_polynom):
            result.append(p_polynom[i])
        # otherwise add q_polynom's coefficient to the reuslt list
        else:
            result.append(q_polynom[i])
    return result


def sub_poly(p_polynom: list, q_polynom: list) -> list:
    # compare the lists and get longest length
    length = get_longest_list_length(p_polynom, q_polynom)
    result = []
    # loop from 0 to the highest index
    for i in range(length):
        # if both lists have the index
        # add the subtraction of the coefficients to the reuslt list
        if i < len(p_polynom) and i < len(q_polynom):
            result.append(p_polynom[i]-q_polynom[i])
        # if only p_polynom list have the index (i)
        # add (0 - p_polynom's coefficient) to the result list
        elif i < len(p_polynom):
            result.append(0-p_polynom[i])
        # otherwise add (0 - q_polynom's coefficient) to the reuslt list
        else:
            result.append(0-q_polynom[i])
    return result


def get_longest_list_length(p_polynom: list, q_polynom: list) -> int:
    p_length = len(p_polynom)
    q_length = len(q_polynom)
    result = 0
    # compare the length of the lists and return the longest
    if p_length > q_length:
        result = p_length
    elif q_length > p_length:
        result = q_length
    else:
        result = p_length # or result = q_length, because both lists are the same
    return result

# Tests ?
def run_tests():
    # T1
    print("\n[Task 1]")
    print("polynomial_to_string(p) :", polynomial_to_string(p))
    print("polynomial_to_string(q) :", polynomial_to_string(q))

    # T2
    print("\n[Task 2]")
    print("polynomial_to_string(p) :", polynomial_to_string(p))
    print("polynomial_to_string(q) :", polynomial_to_string(q))
    print("polynomial_to_string([]) :", polynomial_to_string([]))
    print("polynomial_to_string([0, 0, 0]) :", polynomial_to_string([0, 0, 0]))
    print("polynomial_to_string([1, 2, 3]) :", polynomial_to_string([1, 2, 3]))
    print("polynomial_to_string([-1, 2, -3]) :",polynomial_to_string([-1, 2, -3]))
    print("polynomial_to_string([1, 1, -1]) :", polynomial_to_string([1, 1, -1]))

    # T3
    print("\n[Task 3]")
    print("drop_zeroes(p0) :", drop_zeroes(p0))
    print("drop_zeroes(q0) :", drop_zeroes(q0))
    print("eq_poly(p, p0) :", eq_poly(p, p0))
    print("eq_poly(q, p0) :", eq_poly(q, p0))
    print("eq_poly(q0, []) :", eq_poly(q0, []))

    # T4
    print("\n[Task 4]")
    print("eval_poly(p, 0) :", eval_poly(p, 0))
    print("eval_poly(p, 1) :", eval_poly(p, 1))
    print("eval_poly(p, 2) :", eval_poly(p, 2))
    print("eval_poly(q, 2) :", eval_poly(q, 2))
    print("eval_poly(q, -2) :", eval_poly(q, -2))

    # T5
    print("\n[Task 5]")
    print("eq_poly(add_poly(p, q), add_poly(q, p)) :",
          eq_poly(add_poly(p, q), add_poly(q, p)))
    print("eq_poly(sub_poly(p, p), []) :",
          eq_poly(sub_poly(p, p), []))
    print("eq_poly(sub_poly(p, neg_poly(q)), add_poly(p, q)) :",
          eq_poly(sub_poly(p, neg_poly(q)), add_poly(p, q)))
    print("eq_poly(add_poly(p, p), []) :",
          eq_poly(add_poly(p, p), []))
    print("eq_poly(sub_poly(p, q), [4, -1, 1, 0, -1]) :",
          eq_poly(sub_poly(p, q), [4, -1, 1, 0, -1]))
    print("eval_poly(add_poly(p, q), 12) == eval_poly(p, 12) + eval_poly(q, 12) :", eval_poly(add_poly(p, q), 12) ==
          eval_poly(p, 12) + eval_poly(q, 12))


def options(user_input: str):
    match user_input:
        case "1":
            print("Terms list: ", p_)
            print("Terms list: ", q_)
        case "2":
            print("Polynomial string: ", polynomial_to_string(p_))
            print("Polynomial string: ", polynomial_to_string(q_))
        case "3":
            print("Dropping zeros from list: ", drop_zeroes(p_))
            print("Dropping zeros from list: ", drop_zeroes(q_))
        case "4":
            print("Polyonomials are " + ("not " if not (eq_poly(p_, q_)) else "" ) + "equal")
        case "5":
            print("Polynomial p = ", eval_poly(p_, x))
            print("Polynomial q = ", eval_poly(q_, x))
        case "6":
            print("Changing sign of p: ", polynomial_to_string(neg_poly(p_)))
            print("Changing sign of q: ", polynomial_to_string(neg_poly(q_)))
        case "7":
            print("Result of addition p + q =", polynomial_to_string(add_poly(p_, q_)))
        case "8":
            print("Result of subtraction p - q =", polynomial_to_string(sub_poly(p_, q_)))
        case "9":
            run_tests()
        case _:
            print("\nInvalid option!")


if __name__ == "__main__":
    run_test = input("Do you want to run the tests ? (y/n) ")
    if run_test.lower() == "n" : on = True 
    elif run_test.lower()=="y":
        run_tests()
        on = False 
        
    else : on =False
    while on:
        running = True

        print("""\nLet's start with inserting two cool polynomials of your choice!
Please enter the coefficients from lowest to highest grade, separate the coefficients with a space. 
and make sure to enter integers only, no decimal numbers (float)
Both positive and negative numbers are accepted e.g. (3 or -3)\n""")
        p_ = get_polynomial("p")
        q_ = get_polynomial("q")
        try:
            x = int(input("Value of (x): "))
        except ValueError:
            print("Please enter a valid x value.")
            running = False
        while running:
            if q_ and p_:
                print("""\nWhat do you want to do next?
1) Print all terms
2) Print polynomial equation
3) Drop zeros from polynomials
4) Compare polynomials
5) Calculate polynomial with (x) value
6) Change sign of all terms
7) Add two polynomials
8) Subtract two polynomials
9) Run all tests
n) Insert new polynomials
q) Quit""")
                user_input = str(input("\nChoose option: "))
                print("")
                if user_input.lower() == "n":
                    running = False
                elif user_input.lower() == "q":
                    running = False
                    on = False
                else:
                    options(user_input)
            else:
                print("\nPlease enter valid coefficients.")
                running = False
    print("\nQuitting..")
