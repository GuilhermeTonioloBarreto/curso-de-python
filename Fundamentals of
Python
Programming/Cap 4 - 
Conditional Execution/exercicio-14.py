#exercicio-14.py
semana_ingles = input('Digite um dia da semana em ingles (inicial com letra maiuscula): ')

if(semana_ingles == 'Monday'):
    semana_espanhol = 'Lunes'
elif semana_ingles == 'Tuesday':
    semana_espanhol = 'Martes'
elif semana_ingles == 'Wednesday':
    semana_espanhol = 'Miércoles'
elif semana_ingles == 'Thursday':
    semana_espanhol = 'Jueves'
elif semana_ingles == 'Friday':
    semana_espanhol = 'Viernes'
elif semana_ingles == 'Saturday':
    semana_espanhol = 'Sabado'
elif semana_ingles == 'Sunday':
    semana_espanhol = 'Domingo'


print('O dia da semana digitado em espanhol eh', semana_espanhol)
