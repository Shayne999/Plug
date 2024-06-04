from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db.models import Q
from .models import ThreadModel, MessageModel, Notification
from .forms import ThreadForm, MessageForm

# Create your views here.
@login_required(login_url='index')
def chat(request):
    return render(request, 'chat.html')

class ListThreads(View):
    #Displays chat data
    def get(self, request, *args, **kwargs):
        #ensures that both users have access to the thread
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
            'threads': threads
        }
        return render(request, 'inbox.html', context)
    

class CreateThread(View):
    def get(self, request, *args, **kwargs):
         form = ThreadForm()
         context = {
             'form': form
         }
         return render(request, 'create_thread.html', context)

    def post(self, request, *args, **kwargs):
          form = ThreadForm(request.POST)
          username = request.POST.get('username')

          try: 
              receiver = User.objects.get(username=username)

              if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                  thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                  return redirect('thread', pk=thread.pk)
              elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                  thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                  return redirect('thread', pk=thread.pk)
              
              if form.is_valid():
                  thread = ThreadModel(user=request.user, receiver=receiver)
                  thread.save()

                  return redirect('thread', pk=thread.pk)
              
          except:
              messages.error(request, 'User Does Not Exist')
              return redirect('create-thread')
          

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)

        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        return render(request, 'thread.html', context)

        
class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)

        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
        )
        message.save()

        notification = Notification.objects.create(
            from_user=request.user,
            to_user=receiver,
            thread=thread,
        )

        return redirect('thread', pk=thread.pk)

class ThreadNotification(View):
    def get(self, request, notification_pk, object_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        thread = ThreadModel.objects.get(pk=object_pk)

        notification.user_has_seen = True
        notification.save()
        return redirect('thread', pk=object_pk)


class RemoveNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification.user_has_seen = True   
        notification.save()

        return HttpResponse('Success', content_type="text/plain")