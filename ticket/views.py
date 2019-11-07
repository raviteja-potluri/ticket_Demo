from django.shortcuts import render,redirect
from django.http import request
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from ticket.forms import TicketDetailsForm
from ticket.models import TicketDetails,UserObjects,NotesDetails
# Create your views here.
def ticket(request):
    if request.method == "POST":
        form = TicketDetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = TicketDetailsForm()
    return render(request,'index.html',{'form':form})

def signup(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def show(request):
    ticket = TicketDetails.objects.all()
    return render(request,"show.html",{'data':ticket})

def viewnotes(request, id):
    ticket = TicketDetails.objects.filter(ticketid=id)
    notes = NotesDetails.objects.filter(ticket=id)

    return render(request,'viewnotes.html', {'ticket':ticket, 'data':notes})


def edit(request, id):
    ticket = TicketDetails.objects.get(ticketid=id)

    return render(request,'edit.html', {'record':ticket})

def update(request, id):
    ticket = TicketDetails.objects.get(ticketid=id)
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    city = request.POST['city']
    state = request.POST['state']
    description = request.POST['description']
    category =  request.POST['category']
    username = request.session['username']
    user = UserObjects.objects.filter(username = username)[0]
    if ticket.userobjects.username == username:
        update_ticket = TicketDetails.objects.update(name=name,email=email,phone=phone,
                                                     city=city,state=state,ticket_desc= description,
                                                     ticket_category=category)
        return redirect('/show')
    else:
        return HttpResponse("User Not Allowed To Update")

def addnotes(request, id):
    ticket = TicketDetails.objects.get(ticketid=id)
    return render(request,'addnotes.html', {'record':ticket})

def notesupdate(request, id):
    ticket = TicketDetails.objects.get(ticketid=id)
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    city = request.POST['city']
    state = request.POST['state']
    description = request.POST['description']
    category =  request.POST['category']
    username = request.session['username']
    notes =  request.POST['addnotes']
    user = UserObjects.objects.filter(username = username)[0]
    addnotes = NotesDetails.objects.create(ticket = ticket, userobjects= user, notes=notes )
    return redirect('/show')


def destroy(request, id):
    ticket = TicketDetails.objects.get(ticketid=id)
    ticket.delete()
    return redirect("/show")

def createticket(request,user=''):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        description = request.POST['description']
        category =  request.POST['category']
        status = "open"
        # Creating Ticket
        username = request.session['username']
        user = UserObjects.objects.filter(username = username)
        create_ticket = TicketDetails.objects.create(name=name,email=email,phone=phone, userobjects = user[0],
                                                     city=city,state=state,ticket_desc= description,
                                                     ticket_category=category,status= status)
        return redirect('/show')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if UserObjects.objects.filter(username = username).exists():
                return HttpResponse("UserName Already Exists")
            elif UserObjects.objects.filter(email = email).exists():
                return HttpResponse("Email Already Exists")
            else:
                user = UserObjects.objects.create(first_name= first_name,
                                                last_name = last_name, email= email,
                                                username= username, password = password)
                user.save()
                return redirect("/login")
        else:
            return HttpResponse("Password Did Not Match")
    else:
        return HttpResponse("Request Method is Not POST")

def login_user(request):
    if (request.method == "GET"):
        try:
            getUser = UserObjects.objects.get(username=request.GET['username'])
            pwd = request.GET['password']
            pwd2 = getUser.password
            if(pwd==pwd2):
                request.session['authenticated']=True
                request.session['username']=request.GET['username']
                return redirect('/home')
            else:
                return HttpResponse("Password Not Matching")
        except:
            return render(request, 'login.html',
                          {'invalidusername': True})
    else:
        return HttpResponse("Request Method is Not POST")

def logout(request):
    request.session['authenticated']=False
    request.session['username']= ''
    return redirect('/')
