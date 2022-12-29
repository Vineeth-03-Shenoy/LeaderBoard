from django.shortcuts import render
from .models import Board

# Create your views here.
def LBdisplay(request):
    Teams = Board.objects.all().order_by('Points')
    return render(request, "leaderboardpage.html", {"Teams":Teams})

def Insert(request):
    if request.method=='POST':
        TeamNumber = request.POST['TeamNumber']
        Name = request.POST['Name']
        Points = 0
        Credits = 100

        try:
            obj=Board.objects.get(TeamNumber=TeamNumber)
            print("TEAM NUMBER EXISTS")
        except Board.DoesNotExist:
            ins = Board(TeamNumber=TeamNumber, Name=Name, Points=Points, Credits=Credits)
            ins.save()
    return render(request, "Initial_insert.html")