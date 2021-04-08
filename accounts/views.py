from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from accounts.models import account

# Create your views here.


class AccountView(View):
    """ list of account """

    def get(self,request):
        """ account list show on admin user dashboard"""
        qs = account.objects.all()
        context = {"account_details":qs}
        return render(request,'accounts/account_list.html',context)

class DepositAndWithdraw(View):
    """ Deposit and Withdraw by User """

    def get(self,request):
        current_user = request.user
        qs = account.objects.filter(user=current_user)
        context={"account_details":qs}
        return render(request,'accounts/deposit.html',context)

    def post(self,request):
        current_user = request.user
        amount = int(request.POST['amount'])
        event = request.POST['event']
        try:

            qs = account.objects.get(user=current_user)
            if event=="Withdraw":
                if amount>=qs.amount:
                    total_amount = qs.amount - amount
                    qs.amount=total_amount
                    qs.save()
                else:
                    message = "Required amount is not your account"
                    return HttpResponse(message)
            elif event=="Deposit":
                total_amount = qs.amount + amount
                qs.amount=total_amount
                qs.save()
                message = "Amount {} deposite in your account".format(total_amount)
                return HttpResponse(message)

            else:
                message = "event not found"
                return HttpResponse(message)
        except Exception as e:
            print("user not found")



class TransectionHistory(View):
    """Transection history"""

    def get(self,request):
        import pdb;pdb.set_trace()
        current_user = request.user
        try:
            qs = account.objects.get(user=current_user)
            context = {"account_details":qs.history}
            return render(request,'accounts/account_history.html',context)
        except Exception as e:
            print("user not found")






    
