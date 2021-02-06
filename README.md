## __amortize__
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

## __Inspiration__

 The bank with the lowest rate is not always the best choice. APR is important because the interest rate that gets quoted by the lender, isn't always the interest rate that you will pay. The APR includes interest rate and fees charged by the lender, and lets you compare mortgage offers. __APR, reflects the true cost of borrowing.__ However, the borrower will see this figure after the approval and signing of the contract!

If you want something that is straight to the point, this python library can be a good reference.

- You can estimate the mortgage amount that works with your budget.
- See true cost of borrowing.
- If you wish, you can see a payment breakdown for every single month of the loan duration.
- It allows the side-by-side comparison of the existing or refinanced loan.
- The break-even point shows how long it'll take for the savings to outweigh the cost.
- You can export amortization schedule to excel.
- It doesn’t show you graphs, pie charts, or amortization charts!


## __Installation__

Install with `pip` or your favorite PyPi package manager.

    pip install amortize

## __Dependencies__

* numpy-financial = 1.0.0
* tabulate = 0.8.7
* pandas = "1.2.1


## __Usage__
    
    Mortgage(
        loan amount,
        annual interest rate,
        loan period in months,
        fees)

```python
from amortize.calc import Mortgage    
m=Mortgage(300000,6,12,0)
```

    >> m.afford()           : Determine how much house you can afford
    >> m.summary()          : Repayment summary
    >> m.table()            : Amortization table
    >> m.refinance()        : Refinance
    >> m.excel()            : Send amortization table to excel
   

## __CLI__
    usage: amortize [-h] -a AMOUNT -i INTEREST -m MONTHS -f FEES [-s] [-t] [-r] [-c] [-e] [-info]

    Easy-to-use Python Library for Amortization Schedule and Refinance

    optional arguments:
    -h, --help            show this help message and exit
    -s, --summary         Repayment summary
    -t, --table           Amortization table
    -r, --refinance       Refinance
    -c, --afcalc          Affordability calculator
    -e, --excel           Export to excel
    -info, --info         Brief info about Mortgage

    required arguments:
    -a AMOUNT, --amount AMOUNT  Loan amount
    -i INTEREST, --interest INTEREST Annual interest rate
    -m MONTHS, --months MONTHS Loan period in months
    -f FEES, --fees FEES  Extra payments



## __Screenshots__
   
    Repayment Summary:
    amortize -a300000 -i6 -m12 -f6000 -s
![](https://github.com/ahmetserguns/amortize/raw/main/images/summary.png) 


    Amortization Table:
    amortize -a300000 -i6 -m12 -f0 -t
![](https://github.com/ahmetserguns/amortize/raw/main/images/table.png) 

    Refinance:
    amortize -a300000 -i6 -m12 -f9000 -r
![](https://github.com/ahmetserguns/amortize/raw/main/images/refinance.png) 


    Affordability:
    amortize -a0 -i6 -m360 -f0 -c
![](https://github.com/ahmetserguns/amortize/raw/main/images/afford.png) 




## __Thank You__
Thanks for checking out the package.    
