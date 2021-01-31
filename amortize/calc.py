

from tabulate import tabulate
import datetime
from dateutil.relativedelta import relativedelta
import numpy_financial as npf # for irr calculation
import pandas as pd     # for export schedule to excel
import argparse, re

class Mortgage():
    def __init__(self, kreditutari, faiz, vade, masraf=0):
        self.__kreditutari = kreditutari
        self.__faiz = faiz
        self.__vade = vade
        self.__masraf=masraf
        # effective interest rate %
        self.__Yillikefective=(1+self.__IRR())**12-1

    def __showcalc(self):
        for ele in self.__calc_amortisman():
            return ele

    def __extractdetails(self):
        sfaiz=0
        for ele in self.__calc_amortisman():
            sfaiz+=ele[4]
        return sfaiz

    def __kalanpara(self,kalanay):
        for ele in self.__calc_amortisman():
            if ele[1]==kalanay:
                return ele[5],ele[2]


    def showrefinance(self):
        odenenay=input("            Months Already Paid?      :\t")
        yenifaiz=input("          Refinance Interest Rate?    :\t")
        if is_int(odenenay) and is_number(yenifaiz):
            odenenay=int(odenenay)
            yenifaiz=float(yenifaiz)
            if odenenay>=self.__vade or odenenay<0:
                print("             Invalid Input!!")
            elif yenifaiz<0:
                print("             Invalid Input!!")
            else:
                kalanay=int(self.__vade-int(odenenay))
                para=self.__kalanpara(odenenay)[0]
                taksit_tutari=para*yenifaiz/12/100*(1+(yenifaiz/12/100))**kalanay/(((1+(yenifaiz/12/100))**kalanay)-1)
                geri_odeme1=self.__kalanpara(odenenay)[1]*kalanay
                geri_odeme2=taksit_tutari*kalanay
                kazanc=(taksit_tutari - self.__kalanpara(odenenay)[1])
                prompt= "Sorry, refinancing will not save your money!" if (geri_odeme2 - geri_odeme1+self.__masraf) >=\
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
                  
                """.format(self.__kalanpara(odenenay)[0],self.__faiz, yenifaiz,(yenifaiz-self.__faiz) ,kalanay, kalanay,
                self.__kalanpara(odenenay)[1],taksit_tutari,kazanc,
                geri_odeme1,geri_odeme2, (geri_odeme2-geri_odeme1),self.__masraf,((geri_odeme2-geri_odeme1)+self.__masraf),
                prompt,self.__masraf,
                           kazanc,-1*(self.__masraf/ kazanc) if self.__masraf >0 and kazanc <0 else 0))
        else:
            print("             Must be number !! ")



    def __cashflows(self):
        _cashflow=[-(self.__kreditutari-self.__masraf),]
        data=self.__showcalc()[2]
        for i in range(self.__vade):
            _cashflow.append(data)
        return _cashflow

    def __IRR(self):
        return npf.irr(self.__cashflows())

    def showsummary(self):
        monthly_payment = self.__showcalc()[2]
        total_interest = self.__showcalc()[2]*self.__vade-self.__kreditutari
        total_payment = monthly_payment*self.__vade
        effinterest=(((1+self.__faiz/12/100)**12)-1)*100
        print("")
        print('             Monthly Interest Rate        :{:>20,.4f} %'.format(self.__faiz/12))
        print('             APR                          :{:>20,.4f} %'.format(self.__faiz))
        print('             APY                          :{:>20.4f} %'.format(effinterest))
        print("")
        print("             When Extra Payments Included")
        print('             Monthly Interest Rate        :{:>20.4f} %'.format(self.__IRR()*100))
        print('             APR                          :{:>20.4f} %'.format(self.__IRR()*100*12))
        print('             APY                          :{:>20.4f} %'.format(self.__Yillikefective*100))
        print("")
        print('             Term in Months               :{:>13}'.format(self.__vade) + " Months")
        print('             Monthly Payments             :{:>20,.2f}'.format(monthly_payment))
        print("")
        print('             Mortgage Amount              :{:>20,.2f}'.format(self.__kreditutari))
        print('             Total Interest Paid          :{:>20,.2f}'.format(self.__extractdetails()))
        print("                                           ====================")
        print('             Total Payments               :{:>20,.2f}'.format(total_interest+self.__kreditutari))
        print('             Extra Payments               :{:>20,.2f}'.format(self.__masraf))
        print("                                           ====================")
        print('             All Payments and Fees        :{:>20,.2f}'.format(total_payment+self.__masraf))
        print("                                           ====================")
        print("")


    def showpayment(self):
        new_intrate = self.__faiz / 12 / 100
        a = new_intrate * (1 + new_intrate) ** self.__vade
        b = ((1 + new_intrate) ** self.__vade) - 1
        taksit_tutari = self.__kreditutari * (a / b)
        return taksit_tutari

    def __calc_amortisman(self):  
        new_intrate = self.__faiz/12/100
        a=new_intrate*(1+new_intrate)**self.__vade
        b=((1+new_intrate)**self.__vade)-1
        taksit_tutari=self.__kreditutari*(a/b)
        bakiye = self.__kreditutari
        totalpayment = 0
        say = 1
        while say <= self.__vade:
            interest = bakiye * self.__faiz/12/100
            anapara = taksit_tutari - interest
            bakiye -= anapara-0.0001
            totalpayment += interest + anapara
            dates = datetime.date.today() + relativedelta(months=say)
            yield dates, say, taksit_tutari, anapara, interest, bakiye, \
                totalpayment if bakiye > 0 \
                else 0
            say += 1
            
    def sendtoexcel(self):
        df=pd.DataFrame([ele for ele in self.__calc_amortisman()],
        columns =['Payment Date', 'Taksit No', 'Payment','Principal', 'Interest', 'Principal Remaining', 'Total Paid'])
        df.to_excel(r'.\odemeplani.xlsx', index = False, header=True)     

    def showschedule(self):
        #self.showsummary()
        table = [ele for ele in self.__calc_amortisman()]
        print(
            tabulate(
                table,
                headers=["Payment\nDate", "\n#", "\nPayment", "\nPrincipal",
                "\nInterest", "Principal\nRemaining", "Total\nPaid"],
                floatfmt=",.2f",
                tablefmt='simple',
                numalign="right"
            )
        )

    def cashflow(self):
        return self.__cashflows()

def checker(argumnt): 
    num = int(argumnt)
    if num <0: 
        raise argparse.ArgumentTypeError('Must be > 0')
    return num 

def checker_faiz(argumnt):
    num=float(argumnt)
    if num==0:
        raise argparse.ArgumentTypeError("Must be >0 ")
    return num

# CHECK INTERGER, FLOAT, INT
def is_int(amount):
    if isinstance(amount, int): return True
    if re.search(r'^-{,1}[0-9]+$', amount): return True
    return False

def is_float(amount):
    if isinstance(amount, float): return True
    if re.search(r'^-{,1}[0-9]+\.{1}[0-9]+$', amount): return True
    return False

def is_number(amount):
    return is_int(amount) or is_float(amount)

# References:
# https://exceltable.com/en/analyses-reports/calculation-effective-interest-rate
# https://www.investopedia.com/personal-finance/apr-apy-bank-hopes-cant-tell-difference/
#APR = Periodic Rate x Number of Periods in a Year
#APY = (1 + Periodic Rate)**Number of periods – 1

#a=Mortgage(300000,6,12,6000)
#a.showsummary()
#print(a.calc_monthlypayment())
#a.showrefinance()
#a.showschedule()
#a.sendtoexcel()
#a.cashflow()


