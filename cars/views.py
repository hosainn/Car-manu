from django.shortcuts import render
from django.views.generic import CreateView
from .models import CarParts,CarModel
from .forms import CarsForm,PartsForm
from django.shortcuts import (get_object_or_404, render_to_response)
from django.db.models import Max
import numpy as np
import pandas as pd
from django.shortcuts import (get_object_or_404, render_to_response)
import json
# Create your views here.


class ModelCreate(CreateView):
    model = CarModel
    form_class = CarsForm




class PartsCreate(CreateView):
    model = CarParts
    form_class = PartsForm



def homepage(request):
    return render_to_response('cars/homepage.html')




def ViewTable(request):
    T = True
    for car in CarModel.objects.all():
        ld = car.carparts_set.all().aggregate(Max('level'))
        lc = ld['level__max']
        l = lc+2
        if (T==True):
             pm = CarParts.objects.all().aggregate(Max('parts'))
             pc = pm['parts__max']
             p = pc+2

             na = np.chararray((l, p), unicode=True, itemsize=50)
             na[0][0]=car.model

             col_name = ['car']

             for i in range(p-1):
                 j = str(i+1)
                 j = 'parts '+j
                 col_name.append(j)
        else:
            nb = np.chararray((l,p),unicode=True,itemsize=50)
            nb[0][0]=car.model

        for part in car.carparts_set.all():
            x = part.level - 1
            y = part.parts
            if (T==True):
                na[x][y]=part.name
            else:
                nb[x][y]=part.name
        if (T==False):
            na = np.concatenate((na,nb),axis=0)
        T=False

        pf = pd.DataFrame(na,columns = col_name)
        html = pf.to_html(index = False)
        b = na.tolist()
        a = json.dumps(b)


    return render_to_response('cars/tableview.html', {'html': html,})
    #return render_to_response('cars/graphview_test.html',{'a':a})

def GraphView(request):
    T = True
    for car in CarModel.objects.all():
        ld = car.carparts_set.all().aggregate(Max('level'))
        lc = ld['level__max']
        l = lc + 2
        if (T == True):
            pm = CarParts.objects.all().aggregate(Max('parts'))
            pc = pm['parts__max']
            p = pc + 2

            na = np.chararray((l, p), unicode=True, itemsize=50)
            na[0][0] = car.model

            col_name = ['car']

            for i in range(p - 1):
                j = str(i + 1)
                j = 'parts ' + j
                col_name.append(j)
        else:
            nb = np.chararray((l, p), unicode=True, itemsize=50)
            nb[0][0] = car.model

        for part in car.carparts_set.all():
            x = part.level - 1
            y = part.parts
            if (T == True):
                na[x][y] = part.name
            else:
                nb[x][y] = part.name
        if (T == False):
            na = np.concatenate((na, nb), axis=0)
        T = False

        #pf = pd.DataFrame(na, columns=col_name)
        #html = pf.to_html(index=False)
        b = na.tolist()
        a = json.dumps(b)

    return render_to_response('cars/graphview_test.html',{'a':a})


