from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Chrima index.")
# Create your views here.
def Cheque(request, cheque_id):
    return HttpResponse("You're looking at question %s." % cheque_id)

def Factura(request, factura_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % factura_id)

#def vote(request, question_id):
 #   return HttpResponse("You're voting on question %s." % question_id)