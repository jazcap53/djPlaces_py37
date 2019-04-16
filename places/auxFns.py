from math import pi, cos


def distPtToPt(lat1, lng1, lat2, lng2):
    latsSq = pow(distLats(lat1, lat2), 2.0)
    avgLat = abs(lat1 + lat2) / 2
    lngsSq = pow(distLngs(lng1, lng2, avgLat), 2.0)
    return int((latsSq + lngsSq) ** 0.5)


def earthRadiusInMi():
    return 3963.1676


def miPerDegLngAtLat(latInDegrees):
    latInRadians = latInDegrees * pi / 180.0  # convert degrees to radians
    # earthCircumferenceInMi = 2 * pi * earthRadiusInMi()
    # oneDegreeInMi = earthCircumferenceInMi * cos(latInRadians) / 360
    #               = 2 * pi * earthRadiusInMi() * cos(latInRadians) / 360
    #               = earthRadiusInMi() * cos(latInRadians) * (pi / 180)
    return earthRadiusInMi() * cos(latInRadians) * (pi / 180.0)


def degLngPerMiAtLat(latInDegrees):
    return 1.0 / miPerDegLngAtLat(latInDegrees)


def miPerDegLat():
    return pi * 2.0 * earthRadiusInMi() / 360.0  # return a constant


def degLatPerMi():
    return 360.0 / (pi * 2.0 * earthRadiusInMi())  # return a constant


def distLats(homeLat, awayLat):
    return miPerDegLat() * abs(homeLat - awayLat)


def distLngs(homeLng, awayLng, avgLat):
    return miPerDegLngAtLat(avgLat) * abs(homeLng - awayLng)
