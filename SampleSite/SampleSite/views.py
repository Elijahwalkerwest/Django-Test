from django.http import HttpResponse

# noinspection PyUnresolvedReferences
import random


def hello_world(request):
    return HttpResponse("Hello ")


def root_page(request):
    return HttpResponse("Root Home Page")


def sexy_page(request):
    return HttpResponse("This is the sexiest of pages, to test my mastery of URL's")


def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))

    msg = "Random number between 0 and %s : %d" %(max_rand, random_num)
    msg = 'Random number between 0 and {max} : {rand}'.format(max=max_rand, rand=random_num)

    return HttpResponse(msg)
