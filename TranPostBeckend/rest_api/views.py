from django.shortcuts import render
from django.views import View
from .serializers import EmployeeSerializer, NEWEmployeeSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
import json
import random
import copy
from .data import Employee
# Create your views here.
NEWEmployee_list = []

class GetEmployeeView(View):
    def get(self, request):
        employee_serialized = NEWEmployeeSerializer(Employee, many=True).data
        return JsonResponse(employee_serialized, safe=False, status=200)


class GetEmployeeByPostView(View):
    def get(self, request):
        query = request.GET.get('query')
        print(query)
        Employee_list = []
        for val in Employee:
            if val["Designation"] == query:
                Employee_list.append(val)
        employee_serialized = NEWEmployeeSerializer(
            Employee_list, many=True).data
        # return JsonResponse(employee_serialized ,safe=False,status=200)
        if (Employee_list):
            return JsonResponse(employee_serialized, safe=False, status=200)
        else:
            query = ""
            return HttpResponseBadRequest("Error", status=401)

# Method to put employee as per no block requirements

# class GetNewOfficeWithBlock(View):
#     def get(self, request):
#         del NEWEmployee_list[:]
#         query = request.GET.get('query')
#         # print(query)
#         Employee_list = []
#         # NEWEmployee_list = []
#         FinalEmployee_list = []
#         for val in Employee:
#             if val["Designation"] == query:
#                 Employee_list.append(val)
#         # print(Employee_list)
        
#         block = ["Nala", "Kundahit", "Jamtara","DHQ", "Karmatar", "Narayanpur", "Fathehpur", "DHQ"]
#         for val in Employee_list:
#             val["Alloted_office"] = ""
#             secure_random = random.SystemRandom()
#             Block = secure_random.choice(block)
#             # print(Block)
#             if (
#                 val["Curr_block"] != Block and
#                 val["First_post_office_block"] != Block and
#                 val["Second_post_office_block"] != Block and
#                 val["Dept_block"] != Block
#             ):
#                 val["Alloted_Block"] = Block
#             NEWEmployee_list.append(val)
#         employee_serialized = NEWEmployeeSerializer(NEWEmployee_list, many=True).data
#         return JsonResponse(employee_serialized, safe=False, status=200)


# Method to put employee as per block requirements

class GetNewOfficeWithBlock(View):
    def get(self, request):
        del NEWEmployee_list[:]
        for val in NEWEmployee_list:
            val["Alloted_office"] =""
            val["Alloted_Block"] =""
        employees_assigned=0
        available_employees=[]
        query = request.GET.get('query')
        Employee_list = [val for val in Employee if val["Designation"] == query]
        print(NEWEmployee_list)
        for val in Employee_list:
            val["Alloted_office"] =""
            val["Alloted_Block"] =""
        block_requirements = {
            "Nala": 1,
            "Kundahit": 0,
            "Jamtara": 0,
            "Karmatar": 1,
            "Narayanpur": 1,
            "Fathehpur": 0,
            "DHQ": 3
        }
        blocks_available = ["Nala", "Kundahit", "Jamtara","DHQ", "Karmatar", "Narayanpur", "Fathehpur", "DHQ"]
        for block, required_count in block_requirements.items():
            employees_assigned = 0
            while employees_assigned < required_count:
                available_employees = [val for val in Employee_list if val["Alloted_Block"] == "" ]
                if not available_employees:
                    break
                employee = random.choice(available_employees)
                if (
                employee["Curr_block"] != block and
                employee["First_post_office_block"] != block and
                employee["Second_post_office_block"] != block and
                employee["Dept_block"] != block
                ):
                    employee["Alloted_Block"] = block
                    NEWEmployee_list.append(employee)
                employees_assigned += 1
       
        employee_serialized = NEWEmployeeSerializer(NEWEmployee_list, many=True).data       
        return JsonResponse(NEWEmployee_list, safe=False, status=200)



class CleanArray(View):
     def get(self,request):
          query=request.GET.get('query')
          if query=="clean":  
            del NEWEmployee_list[:]
            print(NEWEmployee_list)
          return JsonResponse(NEWEmployee_list,safe=False, status=200)

class GetNewOffice(View):
    def get(self, request):
        block_office=["BDO Office", "CO Office"]
        district_office = ["Election", "General", "PDS", "DTO", "Samajik", "Kalyan", "Revenue"]
        FinalEmployee_list = []
        for val in NEWEmployee_list:
            secure_random = random.SystemRandom()
            if(val["Alloted_Block"]!="DHQ"):
                 OfficeName = secure_random.choice(block_office)
                 if (
                val["Curr_office"] != OfficeName and
                val["First_post_office"] != OfficeName and
                val["Second_post_office"] != OfficeName and
                val["Dept_office"] != OfficeName
                ):
                   val["Alloted_office"] = OfficeName
            else:
                OfficeName = secure_random.choice(district_office)
                if (
                val["Curr_office"] != OfficeName and
                val["First_post_office"] != OfficeName and
                val["Second_post_office"] != OfficeName and
                val["Dept_office"] != OfficeName
                ):
                    val["Alloted_office"] = OfficeName
            FinalEmployee_list.append(val)
        employee_serialized = NEWEmployeeSerializer(FinalEmployee_list, many=True).data
        return JsonResponse(employee_serialized, safe=False, status=200)

