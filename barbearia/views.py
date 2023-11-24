from django.shortcuts import render
from .models import Agendamento
from django.core.mail import send_mail

def agendar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        hora = request.POST['hora']

        agendamento = Agendamento.objects.filter(hora=hora, disponivel=True).first()

        if agendamento:
            agendamento.disponivel = False
            agendamento.save()

            subject = 'Novo Agendamento'
            message = f'Novo Agendamento:\nNome: {nome}\nHora: {hora}'
            from_email = 'max13_max@hotmail.com'
            recipient_list = ['max13_max@hotmail.com']

            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'sucesso.html', {'agendamento': agendamento})
        else:
            return render(request, 'erro.html', {'mensagem': 'Horário não disponível'})

    return render(request, 'agendar.html')


def horarios_disponiveis(request):
    horarios = Agendamento.objects.all()
    return render(request, 'horarios_disponiveis.html', {'horarios': horarios})