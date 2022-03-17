from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.db import connection
from .models import Message
# from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
  if request.method == 'POST':
    content = request.POST['content']
    message = Message(content=content,
                      date=timezone.now(),
                      user=request.user)
    message.save()
    return HttpResponseRedirect('/messages/')
  else:
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'messages/index.html', context)

# @login_required
def search(request):
  results = []
  if request.method == 'GET':
    query = request.GET['q']
    with connection.cursor() as c:
      query_result = c.execute('''
                               SELECT messageboard_message.content,
                                      auth_user.username
                               FROM   messageboard_message,
                                      auth_user
                               WHERE  messageboard_message.user_id=auth_user.id
                               AND    content LIKE '%%%s%%'
                               ''' % query).fetchall()
      for q in query_result:
        results.append({'content': q[0], 'user': q[1]})
    # results = Message.objects.all().filter(content__icontains=query)
  context = {'messages': results}
  return render(request, 'messages/search.html', context)
