
from tabulate import tabulate
import datetime
from dateutil.relativedelta import relativedelta
import numpy_financial as npf
import pandas as pd     # for export schedule to excel
import argparse
import re

class Mortgage():
    """
    loan        : loan amount\n
    interest    : annual interest rate \n
    term        : loan period in months \n
    fees        : ex:  origination fees, closing costs.
    """
    def __init__(self, loan, interest, term, fees=0):
        self.__loan = loan
        self.__interest = interest
        self.__term = term
        self.__fees=fees
        self.__monint=self.__interest/100/12
        self.__monpayment=npf.pmt(self.__monint,self.__term,-self.__loan)
        self.__totalpayment=self.__monpayment*self.__term
        self.__total_interest = self.__monpayment * self.__term - self.__loan
        # IRR
        self.__IRR = npf.irr(self.__cashflows())
        # APY calculation, fees not included : effective
        self.__effinterest = (((1 + self.__monint) ** 12) - 1) * 100
        # APY calculation, fees included : effective
        self.__annualeffective= (((1 + self.__IRR) ** 12) - 1) * 100

    def __kalanpara(self, kalanay):
        """ Remaining money ... """
        for ele in self.__calc_amortisman():
            if ele[1] == kalanay:
                return ele[5], ele[2]

    def refinance(self):
        """ Show refinance comparison table """

        odenenay=input("\t\tMonths Already Paid?        :\t")
        yenifaiz=input("\t\tRefinance Interest Rate?    :\t")
        if is_int(odenenay) and is_number(yenifaiz):
            odenenay=int(odenenay)
            yenifaiz=float(yenifaiz)
            if odenenay>=self.__term or odenenay<0:
                print("\t\t\t\tCheck already paid value!!")
            elif yenifaiz<0:
                print("\t\t\tInterest rate must be > 0!!")
            else:
                kalanay=int(self.__term - int(odenenay))
                para=self.__kalanpara(odenenay)[0]
                taksit_tutari=para*yenifaiz/12/100*(1+(yenifaiz/12/100))**kalanay/(((1+(yenifaiz/12/100))**kalanay)-1)
                geri_odeme1=self.__kalanpara(odenenay)[1]*kalanay
                geri_odeme2=taksit_tutari*kalanay
                kazanc=(taksit_tutari - self.__kalanpara(odenenay)[1])
                prompt= "Sorry, refinancing will not save your money!" if (geri_odeme2 - geri_odeme1 + self.__fees) >= \
                                                                          0 \
                                        else "Refinancing could save you"

                print("""
                                    REFINANCE CALCULATOR
                              Should I Refinance My Mortgage?
                ==========================================================
                !! Principal Remaining: {:>10,.2f}
                
                                               Remaining          Refinance      Difference
                Interest Rate              {:>10,.2f}          {:>10,.2f}       {:>10,.2f}
                Remaining Term             {:>10}          {:>10}               
                Monthly Payment            {:>10,.2f}      {:>14,.2f}       {:>10,.2f}
                ===========================================================    ============
                Total Payments             {:>10,.2f}      {:>14,.2f}       {:>10,.2f}     
                ===========================================================    ============
                                                                                {:>10,.2f}    
                                                                               ============
                                                                                {:>10,.2f}
                {}
                
                -------------------BREAK EVEN POINT------------------------
                Costs                       : {:>10,.2f}
                Monthly Savings             : {:>10,.2f}
                Break Even Point (Months)   : {:>10,.2f}
                ------------------------------------------------------------
                  
                """.format(self.__kalanpara(odenenay)[0], self.__interest, yenifaiz, (yenifaiz - self.__interest),
                           kalanay, kalanay,
                           self.__kalanpara(odenenay)[1], taksit_tutari, kazanc,
                           geri_odeme1, geri_odeme2, (geri_odeme2-geri_odeme1), self.__fees,
                           ((geri_odeme2 - geri_odeme1) + self.__fees),
                           prompt, self.__fees,
                           kazanc,-1*(self.__fees / kazanc) if self.__fees > 0 and kazanc < 0 else 0))
        else:
            print("\t\t\tMust be a number !! ")


    def __cashflows(self):
        """ Create cashflow table for IRR calculation"""
        _cashflow=[-(self.__loan - self.__fees), ]
        for i in range(self.__term):
            _cashflow.append(self.__monpayment)
        return _cashflow

    def summary(self):
        """ Mortgage Repayment Summary """
        print("")
        print("\t\t\tMORTGAGE REPAYMENT SUMMARY")
        print("")
        print('             Monthly Interest Rate        :{:>20,.4f} %'.format(self.__interest / 12))
        print('             APR                          :{:>20,.4f} %'.format(self.__interest))
        print('             APY                          :{:>20.4f} %'.format(self.__effinterest))
        print("")
        print("             When Extra Payments Included")
        print('             Monthly Interest Rate        :{:>20.4f} %'.format(self.__IRR*100))
        print('             APR                          :{:>20.4f} %'.format(self.__IRR*100*12))
        print('             APY                          :{:>20.4f} %'.format(self.__annualeffective))
        print("")
        print('             Term in Months               :{:>13}'.format(self.__term) + " Months")
        print('             Monthly Payment              :{:>20,.2f}'.format(self.__monpayment))
        print("")
        print('             Mortgage Amount              :{:>20,.2f}'.format(self.__loan))
        print('             Total Interest Paid          :{:>20,.2f}'.format(self.__total_interest))
        print("                                           ====================")
        print('             Total Payments               :{:>20,.2f}'.format(self.__total_interest + self.__loan))
        print('             Extra Payments               :{:>20,.2f}'.format(self.__fees))
        print("                                           ====================")
        print('             All Payments and Fees        :{:>20,.2f}'.format(self.__totalpayment + self.__fees))
        print("                                           ====================")
        print("")

    def __calc_amortisman(self):
        """ Prepare loan amortization table stuff """
        principal_remaining = self.__loan
        totalpayment = 0
        say = 1
        while say <= self.__term:
            interest = principal_remaining * self.__monint
            principal = self.__monpayment - interest
            principal_remaining -= principal-0.000001
            totalpayment += interest + principal
            dates = datetime.date.today() + relativedelta(months=say)
            yield dates, say, self.__monpayment, principal, interest, principal_remaining, \
                totalpayment if principal_remaining > 0 \
                else 0
            say += 1
            
    def excel(self):
        """ Send amortization table to excel """
        df=pd.DataFrame([ele for ele in self.__calc_amortisman()],
        columns =['Payment Date', '#', 'Payment','Principal', 'Interest', 'Principal Remaining', 'Total Paid'])
        df.to_excel(r'.\schedule.xlsx', index = False, header=True)     

    def table(self):
        """ Loan Amortization Table """
        table = [ele for ele in self.__calc_amortisman()]
        print(tabulate(
                table,
                headers=["Payment\nDate", "\n#", "\nPayment", "\nPrincipal",
                "\nInterest", "Principal\nRemaining", "Total\nPaid"],
                floatfmt=",.2f",
                tablefmt='simple',
                numalign="right"
            )
        )
    def afford(self):
        """Use this function to determine how much house you can afford."""
        
        print("")
        annual_income = input("\t\t\t Annual Income        :\t")
        monthly_debts = input("\t\t\t Monthly Debts        :\t")
        if is_int(annual_income) and is_int(monthly_debts):
            annual_income,monthly_debts=int(annual_income),int(monthly_debts)
            if annual_income>0 and monthly_debts>0:
                monthly_income=annual_income/12*0.36
                alinabilecek_ev_kalan_para = monthly_income - monthly_debts
                if monthly_debts<monthly_income:
                    affhouseprice=npf.pv(self.__monint, self.__term, -alinabilecek_ev_kalan_para)
                    aff_monthly_payment=npf.pmt(self.__monint,self.__term,-affhouseprice)
                    print("""
                                    AFFORDABILITY CALCULATOR
                         Monthly Income (36%)         :       {:>10,.2f}
                         Monthly Debts                :       {:>10,.2f}
                         Loan term (months)           :       {:>10}
                         -----------------------------------------------
                         You can afford a house up to :       {:>10,.0f}
                         with Monthly Payment         :       {:>10,.2f}
                         -----------------------------------------------
                         
                         Note: Having a DTI ratio of 36% is considered ideal.
                    """.format(monthly_income,monthly_debts,self.__term,affhouseprice, aff_monthly_payment))
                else:
                    print("\t\t\tInvalid amount of debt !")
            else:
                print("\t\t\tMust be > 0 !")
        else:
            print("\t\t\tMust be a number!")



def checker_1(argument):
    num = int(argument)
    if num <=0: 
        raise argparse.ArgumentTypeError('Must be > 0 !')
    return num

def checker(argument):
    num = int(argument)
    if num <0: 
        raise argparse.ArgumentTypeError('Must be > 0 !')
    return num 

def checker_interest(argument):
    num=float(argument)
    if num<=0:
        raise argparse.ArgumentTypeError("Must be >0 !")
    return num

# CHECK INTERGER, FLOAT
def is_int(amount):
    if isinstance(amount, int):
        return True
    if re.search(r'^-{,1}[0-9]+$', amount):
        return True
    return False

def is_float(amount):
    if isinstance(amount, float):
        return True
    if re.search(r'^-{,1}[0-9]+\.{1}[0-9]+$', amount):
        return True
    return False

def is_number(amount):
    return is_int(amount) or is_float(amount)
