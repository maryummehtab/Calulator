from django.shortcuts import render
from django.http import HttpResponse
import re
import logging
import sys

logger = logging.getLogger(__name__)

def App(request):
    #return HttpResponse("<h1>Hi, this is the calc app.</h1>")
    name = 'Calculator'
    return render(request, 'CalcApp/index.html', {'name': name})
def about(request):
    val1 = request.GET.get("input")
    neg = request.GET.get("negate")
    
    result = ""
    val = []
    
    if(not val1 == None):
        numbers = re.split(r'([+*/\-%])', val1)
        val = numbers

        if(len(numbers) > 2):
            num1=float(numbers[0])
            num2=float(numbers[2])

            result = operation(num1, num2, numbers[1])  
            if(neg == 'true'):
                result = -1 * result  

    return render(request, 'CalcApp/about.html',{'result': result, 'query': ''.join(val)})


def operation(n1, n2, op):
    if(op == '+'):
        result=n1+n2     
    elif(op == '-'):
        result=n1-n2
    elif(op == '/'):
        result=n1/n2
    elif(op == '*'):
        result=n1*n2
    elif(op == '%'):
        result=n1%n2 
    else:
        return 0

    return result   
  
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += str(ele)
 
    return str1 