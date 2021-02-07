
def main():
    from amortize.calc import Mortgage,checker,checker_interest,checker_1
    import argparse

    parser = argparse.ArgumentParser(
        description="Easy-to-use Python Library for Amortization Schedule and Refinance"
    )
    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "-a",
        "--amount",
        dest="amount",
        type=checker,
        required=True,
        help="Loan amount",
    )
    required.add_argument(
        "-i",
        "--interest",
        dest="interest",
        type=checker_interest,
        required=True,
        help="Annual interest rate",
    )
    required.add_argument(
        "-m",
        "--months",
        dest="months",
        type=checker_1,
        required=True,
        help="Loan period in months",
    )
    required.add_argument(
        "-f",
        "--fees",
        dest="fees",
        type=checker,
        required=True,
        help="Extra payments",
    )
    parser.add_argument(
        "-s",
        "--summary",
        dest="summary",
        default=False,
        action="store_true",
        help="Repayment summary",
    )
    parser.add_argument(
        "-t",
        "--table",
        dest="table",
        default=False,
        action="store_true",
        help="Amortization table",
    )
    parser.add_argument(
        "-r",
        "--refinance",
        dest="refinance",
        default=False,
        action="store_true",
        help="Refinance",
    )
    parser.add_argument(
        "-c",
        "--afcalc",
        dest="afcalc",
        default=False,
        action="store_true",
        help="Affordability calculator",
    )
    parser.add_argument(
        "-e",
        "--excel",
        dest="excel",
        default=False,
        action="store_true",
        help="Export to excel",
    )

    arguments = parser.parse_args()

    if arguments.table:
        _kr=Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.table()
    elif arguments.summary:
        _kr = Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.summary()
    elif arguments.excel:
        _kr=Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.excel()
    elif arguments.refinance:
        _kr =Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.refinance()
    elif arguments.afcalc:
        _kr = Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.afford()
    else :
        _kr = Mortgage(arguments.amount, arguments.interest, arguments.months, arguments.fees)
        _kr.summary()    

if __name__=="__main__":
    main()
