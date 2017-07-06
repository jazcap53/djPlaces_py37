# File: places/forms.py
# -*- coding: utf-8 -*-

import re
from django import forms

class GetHomeForm(forms.Form):
    SORT_CHOICES = (('1','by Name',), ('2','by Population (asc.)',), ('3','by Population (desc.)',), ('4','by Distance (asc.)',), \
            ('5','by Distance (desc.)',))
    STATE_CHOICES =  ((None,''), ('AL', 'Alabama (AL)'), ('AK', 'Alaska (AK)'), ('AZ', 'Arizona (AZ)'), ('AR', 'Arkansas (AR)'), \
            ('CA', 'California (CA)'), ('CO', 'Colorado (CO)'), ('CT', 'Connecticut (CT)'), ('DE', 'Delaware (DE)'), \
            ('DC', 'District of Columbia (DC)'), ('FL', 'Florida (FL)'), ('GA', 'Georgia (GA)'), ('HI', 'Hawaii (HI)'), \
            ('ID', 'Idaho (ID)'), ('IL', 'Illinois (IL)'), ('IN', 'Indiana (IN)'), ('IA', 'Iowa (IA)'), ('KS', 'Kansas (KS)'), \
            ('KY', 'Kentucky (KY)'), ('LA', 'Louisiana (LA)'), ('ME', 'Maine (ME)'), ('MD', 'Maryland (MD)'), \
            ('MA', 'Massachusetts (MA)'), ('MI', 'Michigan (MI)'), ('MN', 'Minnesota (MN)'), ('MS', 'Mississippi (MS)'), \
            ('MO', 'Missouri (MO)'), ('MT', 'Montana (MT)'), ('NE', 'Nebraska (NE)'), ('NV', 'Nevada (NV)'), \
            ('NH', 'New Hampshire (NH)'), ('NJ', 'New Jersey (NJ)'), ('NM', 'New Mexico (NM)'), ('NY', 'New York (NY)'), \
            ('NC', 'North Carolina (NC)'), ('ND', 'North Dakota (ND)'), ('OH', 'Ohio (OH)'), ('OK', 'Oklahoma (OK)'), \
            ('OR', 'Oregon (OR)'), ('PA', 'Pennsylvania (PA)'), ('PR', 'Puerto Rico (PR)'), ('RI', 'Rhode Island (RI)'), \
            ('SC', 'South Carolina (SC)'), ('SD', 'South Dakota (SD)'), ('TN', 'Tennessee (TN)'), ('TX', 'Texas (TX)'), \
            ('UT', 'Utah (UT)'), ('VT', 'Vermont (VT)'), ('VA', 'Virginia (VA)'), ('WA', 'Washington (WA)'), \
            ('WV', 'West Virginia (WV)'), ('WI', 'Wisconsin (WI)'), ('WY', 'Wyoming (WY)')) 
    homeCityLabel = "Please enter a home town"
    # TODO: change to a max_length counted from data?
    homeCity = forms.CharField(label=homeCityLabel, max_length=100)
    homeStateLabel = "Please select a state, DC, or Puerto Rico" 
    homeState = forms.ChoiceField(label=homeStateLabel, choices=STATE_CHOICES)
    distLabel = "Please enter a distance from the home town in miles"
    dist = forms.CharField(label=distLabel, max_length=6)
    sortLabel = "Please select a sort order for results"
    sorter = forms.ChoiceField(label=sortLabel, widget=forms.RadioSelect, choices=SORT_CHOICES, initial='1') 
    minPopLabel = "Please enter a minimum population, or zero for no minimum"
    minPop = forms.CharField(label=minPopLabel, max_length=11, initial=0)
    maxPopLabel = "Please enter a maximum population, or zero for no maximum"
    maxPop = forms.CharField(label=maxPopLabel, max_length=11, initial=0)

