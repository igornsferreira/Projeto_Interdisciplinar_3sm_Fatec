<!DOCTYPE html>
<html>

<head>
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/Cadastro.css' %}">
    
    
    <title>Página de Cadastro</title>
</head>
<body>
    <header>
        <div class="logo">
            <img src="logo_empresa.png" alt="Logo da Empresa">
        </div>
        <div class="header-buttons">
            <button>Login</button>
            <button>Cadastro</button>
        </div>
    </header>
    <div class="container">
        <div class="image">
        <img src="{% static 'img/cadastro3.jpg' %}" alt="Imagem de Cadastro">
        </div>
        <div class="form">
            <h1>Cadastro</h1>
            <form method="POST" action="{% url 'cadastro' %}">
                {% csrf_token %}
                <label for="{{form.nome.id_for_label}}">Nome:</label>
                {{form.nome}}
                <laber for ="{{form.email.id_for_label}}">Email:</label>
                {{form.email}}
                


                <button type="submit">Cadastrar</button>
            </form>
        </div>
    </div>
    <footer>
        <div class="contact-info">
            <div class="info">
            <img src="{% static 'img/telefone_icone.png' %}" alt="Imagem de Cadastro">
                <p>(11) 1234-5678</p>
            </div>
            <div class="info">
            <img src="{% static 'img/email_icone.png' %}" alt="Imagem de Cadastro">
                <p>contato@empresa.com</p>
            </div>
            <div class="info">
            <img src="{% static 'img/endereço_icone.png' %}" alt="Imagem de Cadastro">
                <p>Rua da Empresa, 123</p>
            </div>
        </div>
        <p class="credit">Crédito da imagem: Nome do Autor / Freepik</p>
    </footer>
</body>
</html>







