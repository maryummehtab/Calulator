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

        # get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

        # index = get_indexes('.', numbers)

        # newnumbers = []
        # removed = 0
        # num = []

        # for i in index:
        #     n = ''.join(numbers[i-1:i+2])
        #     del newnumbers[i-1-(removed*2):i+2-(removed*2)]
        #     removed += 1
        #     newnumbers.append(float(n))
        #     num.append(float(n))
        #     for x in range(i + 2, len(numbers)):
        #         if not x >= len(numbers):
        #             newnumbers.append(numbers[x])

        # if len(index) > 0:
        #     numbers = newnumbers
        # result = 0
    
        # if(len(num) >= 2):

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