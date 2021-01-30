# __amortize__
### **Easy-to-use Python Library for Amortization Schedule and Refinance**

<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/amortize?style=for-the-badge">
<img alt="PyPI" src="https://img.shields.io/pypi/v/amortize?style=for-the-badge">
<img alt="Travis (.com) branch" src="https://img.shields.io/travis/com/ahmetserguns/amortize/main?label=Travis%20CI&style=for-the-badge">

### __Inspiration__

The loan cost rate, contrary to the interest rate, represents the total cost of the loan.
This is what should be used to repay loans provided by banks. However, the borrower will see this figure after the approval and signing of the contract.

This Python library can, according to the credit information entered, detail the prepayment and the subsequent cost 
of the loan on a monthly and annual, nominal and effective basis, create a payment plan and transfer to excel.
It allows the side-by-side comparison of the existing or refinanced loan.


### __Installation__
    pip install amortize
---
### __Dependencies__

* numpy-financial = 1.0.0
* tabulate = 0.8.7
* pandas = "1.2.1
---

### __Usage__
    
    Mortgage(amount,interest,months,fees=0)

    = Monthly Payment =
    >> from amortize.calc import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
    >> m.showpayment()    

    = Show Summary =
    >> from amortize.calc import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
    >> m.showsummary()

    = Show Amortization Schedule =
    >> from amortize.clac import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
    >> m.showschedule()

    = Refinance Mortgage =
    >> from amortize.calc import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
    >> m.showrefinance()

    = Export Amortization Schedule to Excel =
    >> from amortize.calc import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
    >> m.sendtoexcel()

### __CLI__
---
    usage: amortize [-h] -a AMOUNT -i INTEREST -m MONTHS -f FEES [-s] [-e] [-r]

    Python Library for Amortization Schedule and Refinance

    optional arguments:
    -h, --help            show this help message and exit
    -s, --schedule        Show Amortization Schedule
    -e, --excel           Export to Excel
    -r, --refinance       Refinance Mortgage

    required arguments:
    -a AMOUNT, --amount AMOUNT    Mortgage amount
    -i INTEREST, --interest INTEREST  Annual Interest Rate
    -m MONTHS, --months MONTHS    Term in months
    -f FEES, --fees FEES  Extra Payments




---
### __Screenshots__

    usage: amortize -a 300000 -i 6 -m 12 -f 6000

![](https://github.com/ahmetserguns/amortize/raw/main/images/summary.png)
    
    usage: amortize -a 300000 -i 6 -m 12 -f 6000 -s
![](https://github.com/ahmetserguns/amortize/raw/main/images/schedule.png)
    
    usage: amortize -a 300000 -i 6 -m 12 -f 6000 -r
![](https://github.com/ahmetserguns/amortize/raw/main/images/refinance.png)


### __Thank You__
Thanks for checking out the package! I hope you find it useful.
