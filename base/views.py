from asyncio.windows_events import NULL
from django.shortcuts import render
from datetime import datetime
from base.models import player,evening

# Create your views here.
def index(request):
    player1 = player.objects.filter(time="1").order_by('slotId')
    player2 = player.objects.filter(time="2").order_by('slotId')
    player3 = player.objects.filter(time="3").order_by('slotId')
    player4 = player.objects.filter(time="4").order_by('slotId')
    player5 = player.objects.filter(time="5").order_by('slotId')
    player6 = player.objects.filter(time="6").order_by('slotId')
    if request.method == "POST":
        slotId = request.POST.get('slotId')
        playerChoose = request.POST.get('playerChoose')
        uniqueKey = request.POST.get('uniqueKey')
        name = request.POST.get('name')
        time = request.POST.get('time')
        if player.objects.filter(slotId=slotId , playerChoose=playerChoose).count()==0:
            Player = player(slotId=slotId,playerChoose=playerChoose,uniqueKey=uniqueKey,name=name,time=time,dateAdded = datetime.today())
            Player.save()
        else:
            return render(request,"index.html" , {'data1':player1,'data2':player2,'data3':player3,'data4':player4,'data5':player5,'data6':player6})
    return render(request,"index.html" , {'data1':player1,'data2':player2,'data3':player3,'data4':player4,'data5':player5,'data6':player6})

def eveningPlayers(request):
    player1 = evening.objects.filter(time="1").order_by('slotId')
    player2 = evening.objects.filter(time="2").order_by('slotId')
    player3 = evening.objects.filter(time="3").order_by('slotId')
    player4 = evening.objects.filter(time="4").order_by('slotId')
    player5 = evening.objects.filter(time="5").order_by('slotId')
    player6 = evening.objects.filter(time="6").order_by('slotId')
    if request.method == "POST":
        slotId = request.POST.get('slotId')
        playerChoose = request.POST.get('playerChoose')
        uniqueKey = request.POST.get('uniqueKey')
        name = request.POST.get('name')
        time = request.POST.get('time')
        if evening.objects.filter(slotId=slotId , playerChoose=playerChoose).count()==0:
            Player = evening(slotId=slotId,playerChoose=playerChoose,uniqueKey=uniqueKey,name=name,time=time,dateAdded = datetime.today())
            Player.save()
        else:
            return render(request,"index1.html" , {'data1':player1,'data2':player2,'data3':player3,'data4':player4,'data5':player5,'data6':player6})
    return render(request,"index1.html" , {'data1':player1,'data2':player2,'data3':player3,'data4':player4,'data5':player5,'data6':player6})
