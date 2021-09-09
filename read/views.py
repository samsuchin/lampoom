from django.shortcuts import render

def detect(request):
    return render(request, "read/smile_detect.html")