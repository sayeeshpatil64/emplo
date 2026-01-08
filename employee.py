import sys

def calculate_salary(basic):
    hra = 0.20 * basic
    da = 0.50 * basic
    pf = 0.11 * basic
    net_salary = (basic + hra + da) - pf
    return hra, da, pf, net_salary


def main():
    name = sys.argv[1]
    emp_id = sys.argv[2]
    designation = sys.argv[3]
    basic_salary = float(sys.argv[4])

    hra, da, pf, net = calculate_salary(basic_salary)

    print("\n----- PAY SLIP -----")
    print("Name        :", name)
    print("Employee ID :", emp_id)
    print("Designation :", designation)
    print("Basic Salary:", basic_salary)
    print("HRA (20%)   :", hra)
    print("DA (50%)    :", da)
    print("PF (11%)    :", pf)
    print("--------------------")
    print("Net Salary  :", net)


if __name__ == "__main__":
    main()
