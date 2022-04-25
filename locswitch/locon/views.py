from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import RPi.GPIO as GPIO
import time

# Create your views here.

from django.http import HttpResponse
global uptime
uptime  = time.time() - 60
@csrf_exempt
def index(request):
    global uptime
    if request.method == 'GET':
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.OUT)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        GPIO.cleanup()
       '''
        if uptime != None:# and time.time() - uptime > 10:
            if time.time() - uptime > 60:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(18,GPIO.OUT)
                GPIO.output(18,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18,GPIO.LOW)
                GPIO.cleanup()
                uptime = time.time() 
                return HttpResponse('run')
            return HttpResponse("time."+ str(uptime))
        return HttpResponse("Hello PC.")
