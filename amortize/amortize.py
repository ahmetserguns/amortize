
def main():
    from amortize.calc import Mortgage,checker,checker_faiz
    import argparse

    parser = argparse.ArgumentParser(
        description="Python Library for Amortization Schedule and Refinance"
    )
    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "-a",
        "--amount",
        dest="amount",
        type=checker,
        required=True,
        help="Mortgage amount",
    )
    required.add_argument(
        "-i",
        "--interest",
        dest="interest",
        type=checker_faiz,
        required=True,
        help="Annual Interest Rate",
    )
    required.add_argument(
        "-m",
        "--months",
        dest="months",
        type=checker,
        required=True,
        help="Term in months",
    )
    required.add_argument(
        "-f",
        "--fees",
        dest="fees",
        type=checker,
        required=True,
        help="Extra Payments",
    )
    parser.add_argument(
        "-s",
        "--schedule",
        dest="schedule",
        default=False,
        action="store_true",
        help="Show Amortization Schedule",
    )
    parser.add_argument(
        "-e",
        "--excel",
        dest="excel",
        default=False,
        action="store_true",
        help="Export to Excel",
    )
    parser.add_argument(
        "-r",
        "--refinance",
        dest="refinance",
        default=False,
        action="store_true",
        help="Refinance Mortgage",
    )
    arguments = parser.parse_args()

    if arguments.schedule:
        _kr=Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.showschedule()
    elif arguments.excel:
        _kr=Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.sendtoexcel()
    elif arguments.refinance:
        _kr =Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.showrefinance()
    else:
        _kr=Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.showsummary()


if __name__=="__main__":
    main()