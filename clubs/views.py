from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Club, Member

# Route implementations

def index(request):
    return render(request, 'index.html')

def get_or_create_club(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        quality = request.POST.get("quality")
        time_commitment = request.POST.get("time_commitment")
        fun = request.POST.get("fun")

        parameters = ["name", "description", "quality", "time_commitment"\
            , "fun"]
        for param in parameters:
            if not request.POST.get(param):
                return JsonResponse({
                    "success": False,
                    "error": "Parameter \'" + param + "\' must not be blank!"
                }, status=400)

        if Clubs.objects.filter(name=name).exists():
            return JsonResponse({
                "success": False,
                "error": "Club with this name already exists!"
            }, status=409)

        Club.objects.create(name=name, description=description\
            , quality=quality, time_commitment = time_commitment, fun = fun)

        return JsonResponse({
            "success": True
        })
    else:
        clubSet = Club.objects.all().values('name', 'id', 'quality'\
            , 'time_commitment', 'fun', 'description', 'members', 'comments')
        clubJson = JsonResponse({
            "clubs": list(clubSet)
        })
        return clubJson

def get_or_create_member(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")

        if not name:
            return JsonResponse({
                "success": False,
                "error": "Member name must not be empty!"
            }, status=400)

        if Member.objects.filter(name=name).exists():
            return JsonResponse({
                "success": False,
                "error": "Member with this name already exists!"
            }, status=409)

        Member.objects.create(name=name)
        return JsonResponse({
            "success": True
        })
    else:
        members = list(Member.objects.all().values_list("name", flat=True))
        return JsonResponse({
            "members": members
        })

def update_club_ranking(request):
    if request.method == "POST":
        id = request.POST.get("clubid")

        quality = request.POST.get("quality")
        time_commitment = request.POST.get("time_commitment")
        fun = request.POST.get("fun")

        parameters = ["clubid", "quality", "time_commitment", "fun"]
        for param in parameters:
            if not request.POST.get(param):
                return JsonResponse({
                    "success": False,
                    "error": "Parameter \'" + param + "\' must not be blank!"
                }, status=400)

        if not Club.objects.filter(id=id).exists():
            return JsonResponse({
                "success": False,
                "error": "No club with the given id exists!"
            }, status=404)
    
        clubToUpdate = Club.objects.get(id=id)
        clubToUpdate.quality = quality
        clubToUpdate.time_commitment = time_commitment
        clubToUpdate.fun = fun
        clubToUpdate.save()

        return JsonResponse({
                "success": True
            })

def mystery_function(request):
    #We stray further from god's light everyday
    return average_club_quality(request)

def average_club_quality(request): 
    allClubs = Club.objects.all()

    if allClubs.exists():
        qualitySum = 0
        for club in allClubs:
            qualitySum += club.quality
        json = { "val": qualitySum / allClubs.count() }
    else:
        json = { "val": 0 }
    
    return JsonResponse(json)