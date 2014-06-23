from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, Context, loader, RequestContext
from pprint import pprint
from app.models import CD
from django.db import models
import json
import re
# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        template=Template("""
            <html>
                <head>
                    {% load staticfiles %}
                    <link rel="stylesheet" type="text/css" href="{% static 'app/stylesheet.css' %}"/>
                    <title>Welcome</title>
                </head>
                <body>
                    Welcome to the CD storage. Below you can see our CDs in store<br>
                    If you want to add or delete entries, press the buttons below.
                    <br>
                    <br>
                    <a href="/add">add</a>
                    <a href="/show">show</a>
                    
                </body>
            </html>

        """)
        context = Context(template)
        return HttpResponse(template.render(context))

class input(View):
    def get(self, request, *args, **kwargs):
        band_name=request.GET.get('band_name', 'band_name')
        title=request.GET.get('title', ' ')
        number_tracks=request.GET.get('number_tracks',' ')
        length=request.GET.get('length',' ')
        price=request.GET.get('price',' ')
        template=Template("""
            <html>
                <head>
                    {% load staticfiles %}
                    <link rel="stylesheet" type="text/css" href="{% static 'app/stylesheet.css' %}"/>
                    <title>The input</title>
                </head>
                <body>
                    Here you can add new records to the CDs database. Please fill in
                    every place below:
                    <br>
                    <br>
                    <form>
                        
                        <table style="width:500px">
                            <tr>
                                <td>Name</td>
                                <td><input type="text" name="band_name"></td>     
                            </tr>
                            <tr>
                                <td>Title</td>
                                <td><input type="text" name="title"></td>
                            </tr>
                            <tr>
                                <td>Number of trakcks</td>
                                <td><input type="text" name="number_tracks"></td>
                            </tr>
                            <tr>
                                <td>Total length</td>
                                <td><input type="text" name="length"></td>
                            </tr>
                            <tr>
                                <td>Price</td>
                                <td><input type="text" name="price"></td>
                            </tr>
                        </table>
                        <input type="submit" value="Submit">
                    </form>
                    <a href="/">back</a>
                    <a href="/show">show</a>
                    <br>
                </body>
            </html>
        """)

        if (band_name!="band_name"):
            p = CD(band_name=band_name, title=title, track_number=number_tracks, total_length=length, price=price)
            p.save()
            
        context = Context(template)
        return HttpResponse(template.render(context))

class show(View):

    def get(self, request, *args, **kwargs):
        which_delete_title=request.GET.get('which_delete_title', '0')
        which_delete_band=request.GET.get('which_delete_band', '0')
        i=1;
        template=Template("""
            <html>
                <head>
                    {% load staticfiles %}
                    <link rel="stylesheet" type="text/css" href="{% static 'app/stylesheet.css' %}"/>
                    <title>List of the CDs</title>
                </head>
                <body>
                    Below you can see all the entries in the shop:
                    <br>
                    <br>
                    <table rules="cols">
                        <tr>
                        {% for x in title%}
                            <td>
                                Title: {{x}}
                            </td>
                        {% endfor%}
                        </tr>
                        <tr>
                        {% for x in band_name%}
                            <td>
                                Band name: {{x}}
                            </td>
                        {% endfor%}
                        </tr>
                        <tr>
                        {% for x in price%}
                            <td>
                                Price: {{x}}
                            </td>
                        {% endfor%}
                        </tr>
                        <tr>
                        {% for x in number_tracks%}
                            <td>
                                Number of tracks: {{x}}
                            </td>
                        {% endfor%}
                        </tr>
                        <tr>
                        {% for x in length%}
                            <td>
                                Total length: {{x}}
                            </td>
                    
                        {% endfor%}
                        </tr>
                    </table>
                    <br>
                    <form>
                        Type in the title of the CD you wish to delete:
                        <br>
                        <input type="text" name="which_delete_title">
                        <br>
                        Or the name ofthe band, whose CD you want to delete:
                        <br>
                        <input type="text" name="which_delete_band">
                        <br>
                        <input type="submit" value="Submit">
                        
                    </form>
                    <a href="/add">add</a>
                    <a href="/">back</a>
                </body>
            </html>

        """)
        
        result = CD.objects.all().values()
        
        regx = re.compile('\'band_name\': \'(.*?)\'')
        band_name = regx.findall(str(result))
        
        regx = re.compile('\'title\': \'(.*?)\'')
        title = regx.findall(str(result))
        
        regx = re.compile('\'track_number\': \'(.*?)\'')
        number_tracks = regx.findall(str(result))

        regx = re.compile('\'total_length\': \'(.*?)\'')
        length = regx.findall(str(result))

        regx = re.compile('\'price\': \'(.*?)\'')
        price = regx.findall(str(result))

        datas2 = CD.objects.filter(id=5).values()
        datas = CD.objects.all().values()
        
        if (which_delete_title != 0 ):
            CD.objects.filter(title=which_delete_title).delete()

        if (which_delete_band != 0 ):
            CD.objects.filter(band_name=which_delete_band).delete()

        dictionary={"band_name": band_name, "title": title, "number_tracks": number_tracks, 'length': length, 'price': price}
        context=Context(dictionary)
        return HttpResponse(template.render(context))