
def cadastro_pessoa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        email = request.POST['email']