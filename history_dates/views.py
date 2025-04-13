import json
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from .models import HistoricalEvent
from .forms import HistoricalEventForm

def main_page(request):
    return render(request, 'main.html')

def event_list(request):
    query = request.GET.get('q')
    events = HistoricalEvent.objects.all()
    if query:
        events = events.filter(Q(title__icontains=query) | Q(date__icontains=query))
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)

def add_event(request):
    if request.method == 'POST':
        form = HistoricalEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = HistoricalEventForm()
    return render(request, 'add_event.html', {'form': form})

def edit_event(request, pk):
    event = get_object_or_404(HistoricalEvent, pk=pk)
    if request.method == 'POST':
        form = HistoricalEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = HistoricalEventForm(instance=event)
    return render(request, 'add_event.html', {'form': form, 'event': event})

def delete_event(request, pk):
    event = get_object_or_404(HistoricalEvent, pk=pk)
    event.delete()
    return redirect('event_list')

def quiz(request):
    events = list(HistoricalEvent.objects.all())
    if not events:
        return render(request, 'quiz.html', {'no_events': True})
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('user_answer', '').strip()
        try:
            question = HistoricalEvent.objects.get(id=question_id)
            user_date = int(user_answer)
            is_correct = user_date == question.date
        except HistoricalEvent.DoesNotExist:
            pass
        except ValueError:
            is_correct = False
        if is_correct:
            question = random.choice(events)
        context = {
            'question': question.title,
            'question_id': question.id,
            'show_result': True,
            'is_correct': is_correct,
            'no_events': False,
            'correct_answer': question.date
        }
        return render(request, 'quiz.html', context)
    # GET запрос или ошибка - показываем новый вопрос
    question = random.choice(events)
    context = {
        'question': question.title,
        'question_id': question.id,
        'show_result': False,
        'no_events': False,
        'correct_answer': question.date
    }
    return render(request, 'quiz.html', context)


def timeline_quiz(request):
    events = list(HistoricalEvent.objects.order_by('?')[:4])
    if len(events) < 4:
        return render(request, 'timeline_quiz.html', {'no_events': True})
    correct_order = [str(e.id) for e in sorted(events, key=lambda x: x.date)]
    request.session['current_timeline_order'] = correct_order
    context = {
        'events': events,
        'correct_order': correct_order,
        'no_events': False
    }
    return render(request, 'timeline_quiz.html', context)

def check_timeline_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_order = data.get('order', [])
        correct_order = request.session.get('current_timeline_order', [])
        is_correct = user_order == correct_order
        return JsonResponse({
            'correct': is_correct,
            'correct_order': correct_order
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
