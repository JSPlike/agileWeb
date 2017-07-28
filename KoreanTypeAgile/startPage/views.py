from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
from .models import User, Todo


def index(request): 

    return render(request, 'startPages/index.html')  
def cssBootstrap(request):
    return render(request, 'startPages/css/bootstrap.min.css')
def loginPage(request):
    return render(request, 'startPages/loginPage.html')
def signUpPage(request):
    return render(request, 'startPages/signUpPage.html')
def planMainPage(request):
    todos = Todo.objects.all()
    context = {'todos' : todos}
    return render(request, 'startPages/left_navi/planMainPage.html', context)
def todoPopUp(request):
    return render(request, 'startPages/todoPopUp.html')
def todoSaveForm(todoName, todoContents, startDate, endDate):
    todo = Todo(todoName = todoName,
                todoContents = todoContents,
                startDate = startDate,
                endDate = endDate)
                        
    todo.save()
def sendTodoSubmit(request):
    projectName = request.POST['projectName']
    contents = request.POST['contents']
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']

    maxCount = 0
    projectNameCount = -1
    contentsCount = -1

    tempCount = 0
    
    if startDate != "":
        startDateSplit = startDate.split("T")
        startDateArray = startDateSplit[0].split("-") 
        startTimeArray = startDateSplit[1].split(":") 

    if endDate != "":
        endDateSplit = endDate.split("T")
        endDateArray = endDateSplit[0].split("-") 
        endTimeArray = endDateSplit[1].split(":") 
        
    if projectName != "":
        projectNameArray = projectName.split("`")
        projectNameCount = len(projectNameArray)
        maxCount = projectNameCount - 1
    if contents != "":
       contentsArray = contents.split("`")
       contentsCount = len(contentsArray)
       if projectNameCount < contentsCount:
           maxCount = contentsCount - 1

    while tempCount < maxCount:
        if projectNameCount >= tempCount and contentsCount >= tempCount : 
            todoSaveForm(todoName = projectNameArray[tempCount],
                        todoContents = contentsArray[tempCount],
                        startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                        endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))
        #todo - error
        elif projectNameCount >= tempCount and contentsCount < tempCount :
            if contentsCount == -1 :
                todoSaveForm(todoName = projectNameArray[tempCount],
                        todoContents = "",
                        startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                        endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))
                        
            else:

                todoSaveForm(todoName = projectNameArray[tempCount],
                            todoContents = contentsArray[contentsCount],
                            startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                            endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))

        elif projectNameCount < tempCount and contentsCount >= tempCount :
            if projectNameCount == -1 :
                todoSaveForm(todoName = "",
                            todoContents = contentsArray[tempCount],
                            startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                            endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))
            else:
                todoSaveForm(todoName = projectNameArray[projectNameCount],
                        todoContents = contentsArray[tempCount],
                        startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                        endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))


        tempCount = tempCount + 1
        

    todoSaveForm(todoName = projectNameArray[tempCount],
                        todoContents = contentsArray[tempCount],
                        startDate = datetime.datetime(int(startDateArray[0]),int(startDateArray[1]),int(startDateArray[2]), int(startTimeArray[0]), int(startTimeArray[1])),
                        endDate = datetime.datetime(int(endDateArray[0]),int(endDateArray[1]),int(endDateArray[2]),int(endTimeArray[0]),int(endTimeArray[1])))
    todos = Todo.objects.all()
    context = {'todos' : todos}
    return render(request, 'startPages/planMainPage.html', context)


def Signup(request) :
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    try:
        userdata=User.objects.get(name = name,email = email, password=password)
        userdata.save()
    except:
        userdata=User(name=name,email=email,password=password)
        userdata.save()
        userdatas=User.objects.all()
        userdatas={'userdatas':userdatas}
        return render(request, 'startPages/index.html', userdatas)
    userdatas=User.objects.all()
    userdatas={'userdatas':userdatas}
    return render(request,'startPages/index.html',userdatas)

def Signin(request):
    try:
        input_email = request.POST['email']
    except:
        input_email=False
    #email=request.POST.get('email',False)
    input_password=request.POST.get('password',None)
    #try:
    check_email=User.objects.filter(email=input_email).exists()
    print(input_email)
    check_password=User.objects.filter(password=input_password).exists()
    #except User.DoesNotExist :
    #    check_email = False
    #    check_password = False
    if check_email is True :
        return HttpResponse("로그인 성공")
    elif check_email is False :
        return HttpResponse("로그인 실패")
    else : 
        return HttpResponse("True False 둘 다 아닌")
    #user = authenticate(email=input_email,password=input_password)
    """
    if user is not None :
        login(request,user)
        return render(request,'startPages/index.html')
    elif user is None :
        return HttpResponse("로그인 실패") 
    else :
        return HttpResponse("무슨 오류죠 이건")
    """




