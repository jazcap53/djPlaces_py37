# places/views.py
# -*- coding: utf-8 -*-

import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import GetHomeForm
from .models import Place
from .auxFns import distPtToPt


def index(request):
    ps = Place.objects.filter(st='NY', city='New York')
    context = { 'place_names': ps }
    return render(request, 'places/index.html', context)


def getHome(request):
    errMsg = ''
    if request.method == 'POST':
        form = GetHomeForm(request.POST)
        if form.is_valid():
            homeCity = form.cleaned_data['homeCity']
            homeCity = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ, -]', '', homeCity)
            homeState = form.cleaned_data['homeState']
            homeState = re.sub(r'[^a-zA-Z]', '', homeState)
            cleanDist = form.cleaned_data['dist']
            cleanSorter = form.cleaned_data['sorter']
            cleanMinPop = form.cleaned_data['minPop']
            cleanMaxPop = form.cleaned_data['maxPop']
            # redirect after POST
            redirectString = '/places/showHome/' + homeCity + '/' + homeState + '/' + \
                    cleanDist + '/' + cleanSorter + '/' + \
                    cleanMinPop + '/' + cleanMaxPop + '/'
            return HttpResponseRedirect(redirectString)
    else:
        form = GetHomeForm()  # an unbound form
    context = { 'form': form, 'errMsg': errMsg }
    return render(request, 'places/getHome.html', context)


def showHome(request, homeTown, homeState, dist, sorter, minP, maxP):
    # TODO: rename some variables
    # TODO: reduce number of params (?)
    town = homeTown
    state = homeState
    dist = dist.replace(',', '')
    minP = int(minP.replace(',', ''))
    maxP = int(maxP.replace(',', ''))
    if maxP == 0:
        maxP = 999999999
    p = Place.objects.get(st=state, city=town)
    p.popn = '{:,}'.format(p.popn)
    d = int(dist)

    pLat = p.lat
    pLng = p.lng

    # TODO: see https://docs.djangoproject.com/en/2.2/topics/db/sql/  replace raw SQL
    # length of a degree of longitude = (PI / 180) * radius of earth * latitude in degrees  <from: wikipedia>
    # 3963.1676 is radius of earth in miles
    # cos(lat * PI() / 180.0) is cosine of (lat in radians)
    # cos(((lat + pLat) / 2) * PI() / 180.0) is cosine of (avg of lat and pLat in radians)
    # cos((lat + pLat) * PI() / 360.0)       is ditto
    # (3963.1676 * cos((lat + pLat) * PI() / 360.0) * PI() / 180.0) is miles per degree lng at avg lat
    # (dist / (3963.1676 * cos((lat + pLat) * PI() / 360.0) * PI() / 180.0)) is
    #     distance divided by miles per degree lng at avg lat is
    #     distance times degrees lng per mile at avg lat
    r = Place.objects.raw('SELECT id, st, city, lng, lat, popn, 0 as distance '
                          'FROM places_place '
                          'WHERE lng <= %s + (%s / (3963.1676 * cos((lat + %s) * PI() / 360.0) * PI() / 180.0)) '
                          'AND lng >= %s - (%s / (3963.1676 * cos((lat + %s) * PI() / 360.0) * PI() / 180.0)) '
                          'AND lat <= %s + (%s * (360.0 / (PI() * 2.0 * 3963.1676))) '
                          'AND lat >= %s - (%s * (360.0 / (PI() * 2.0 * 3963.1676)))',
                          [pLng, dist, pLat, pLng, dist, pLat, pLat, dist, pLat, dist])

    r = list(r)
    s = []

    for dataline in r:
        dataline.distance = distPtToPt(float(pLng), float(pLat),
                                       float(dataline.lng),
                                       float(dataline.lat))
        if dataline.distance <= d and \
                not (dataline.st == state and dataline.city == town) and \
                minP <= int(dataline.popn) <= maxP:
            dataline.distance = '{:,}'.format(dataline.distance)
            dataline.popn = '{:,}'.format(int(dataline.popn))
            s.append(dataline)

    L = lambda x: x.city
    rev = False

    # TODO: improve
    if sorter == '2':
        L = lambda x: int(x.popn.replace(',',''))
        rev = False
    elif sorter == '3':
        L = lambda x: int(x.popn.replace(',',''))
        rev = True
    elif sorter == '4':
        L = lambda x: int(x.distance.replace(',',''))
        rev = False
    elif sorter == '5':
        L = lambda x: int(x.distance.replace(',',''))
        rev = True

    s.sort(key=L, reverse=rev)

    context = { 'p': p, 's': s }
    return render(request, 'places/showHome.html', context)
