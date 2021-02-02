# __amortize__
### **Easy-to-use Python Library for Amortization Schedule and Refinance**

<p align=left>
    <a target="_blank" ><img src="https://img.shields.io/pypi/pyversions/amortize?style=flat-square"></a>
    <a target="_blank" ><img src="https://img.shields.io/pypi/v/amortize"></a>
    <a href="https://www.codefactor.io/repository/github/ahmetserguns/amortize/overview/main"></a>
    <a target="_blank" ><img src="https://www.codefactor.io/repository/github/ahmetserguns/amortize/badge/main" alt="CodeFactor" /></a>
    <a target="_blank" ><img alt="Travis (.com) branch" src="https://img.shields.io/travis/com/ahmetserguns/amortize/main?logo=Travis"></a>
    <a target="_blank" ><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/amortize"></a>
   <a target="_blank" ><img src="https://img.shields.io/static/v1?label=status&message=stable&color=<Green>"></a>
</p>


### __Inspiration__

The loan cost rate, contrary to the interest rate, represents the total cost of the loan.
This is what should be used to repay loans provided by banks. However, the borrower will see this figure after
the approval and signing of the contract.

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

    >> from amortize.calc import Mortgage    
    >> m=Mortgage(300000,6,12,6000)
  
    >> m.showpayment()          : Monthly Payment
    >> m.showsummary()          : Summary Table
    >> m.showschedule()         : Amortization Schedule
    >> m.showrefinance()        : Refinance Mortgage
    >> m.sendtoexcel()          : Send Amortization Schedule to Excel

### __CLI__

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
Thanks for checking out the package.
