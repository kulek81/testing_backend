from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator
from .models import Variants, Questions, Answers



@api_view(['GET'])
def variants_list(request):
    if request.method == 'GET':
        variants = Variants.objects.all()
        variants_list = [i.variant_number for i in variants]
        return Response(variants_list)


@api_view(['GET'])
def questions_list(request, pk):
    if request.method == 'GET':
        questions = Questions.objects.filter(variant_number=pk).order_by('topic')
        answers = Answers.objects.all()
        tests = []
        for i in questions:
            tests_answers = answers.filter(question=i.id)
            test_object = {
                'topic': i.topic.id,
                'question': i.question_text,
                'answers': [{'answer': f.answer_text, 'rightAnswer': f.right_answer} for f in tests_answers]
            }
            tests.append(test_object)
        return Response(tests)
