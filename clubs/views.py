import base64  # lol

from django.shortcuts import render
from django.http import JsonResponse

from .models import Club, Member


def get_or_create_member(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if not name:
            return JsonResponse({
                "success": False,
                "error": "Member name must not be empty!"
            })

        Member.objects.create(name=name)

        return JsonResponse({
            "success": True
        })
    else:
        return JsonResponse({
            "members": Member.objects.all().values_list("name", flat=True)
        })


def mystery_function(request):
    whee = Club
    abc = 10
    hhh = 0
    huh = '\x6f\x62\x6a\x65\x63\x74\x73'

    for ghi in getattr(whee, huh).all():
        abc = abc + ghi.__getattr__("".join(reversed("y\x74ilau\x71")))
        hhh += 1

    hhh += whee.objects.all().count()
    lav = base64.b64decode(b"dmFs").decode("utf-8")

    try:
        wow = {}
        wow.__setitem__(lav, abc / hhh * 2 - 20 / hhh)
    except ZeroDivisionError:
        wow = {lav: 0}

    return JsonResponse(wow)
