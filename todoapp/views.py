import json
from os import link
from re import A
from bs4 import BeautifulSoup
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from models import LotteryData, LotteryNew
from .serializers import LotterySerializer, TodoSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # todos = Todo.objects.filter(user = request.user.id)
        # serializer = TodoSerializer(todos, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        lotteries = LotteryData.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(lotteries, 10)

        try:
            lotteries_list = paginator.page(page)
        except PageNotAnInteger:
            lotteries_list = paginator.page(1)
        except EmptyPage:
            lotteries_list = paginator.page(paginator.num_pages)

        serializer = TodoSerializer(lotteries_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScrapperApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        r = requests.get('http://103.251.43.52/lottery/weblotteryresult.php')
        # new_lotteries = LotteryNew.objects.all()
 
        soup = BeautifulSoup(r.content, 'html.parser')
        # s = soup.findAll('table', class_='stats')
        data = []
        list = []
        new_items= []
        # table = soup.find('table', attrs={'class':'stats','width':'500','align':'center','cellspacing':'0'})
        table = soup.find('table', attrs={'align':'center','border':'0'})
        # table_body = table.find('tbody')

        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
        
            for element in row.find_all('a'):
                href = element['href'] 
            cols = [ele.text.strip() for ele in cols]
            cols[2]=href
            # for ele in cols:
            #     lottery_new=LotteryNew(ele[0],ele[1])
            # data.append(lottery_new.toJSON())
            data.append([ele for ele in cols if ele and (cols[0]!="Lottery/DrawNo" and cols[1]!="Lottery/DrawNo")])

        for lottery in data :
            if len(lottery) != 0:
                data = {'name':lottery[0],'date': lottery[1],'link':lottery[2]}
                list.append(data)
                serializer = LotterySerializer(data=data)
                if serializer.is_valid():
                    if LotteryNew.objects.filter(link = lottery[2]).exists():
                        print("aleady present")
                    else:
                        new_items.append(data)
                        serializer.save()
                

        # print(list)
        print(new_items)
        return Response(list, status=status.HTTP_200_OK)


# class LotteryNew: 
#     def __init__(self, name, date, link): 
#         self.name = name 
#         self.date = date
#         self.link = link
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True)

# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)