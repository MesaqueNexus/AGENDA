AGENDA = {
    'mesaque' : {
        'telefone' : '62 993645227',
        'email' : 'mesaquenexus@gmail.com',
        'endereco' : {
            'rua' : 'D',
            'bairro' : 'Liberdade',
            'cidade' : 'Ipixuna do para'
        },
    },
    'joao' : {
        'telefone' : '21 123456789',
        'email' : 'joao@gmail.com',
        'endereco' : {
            'rua' : 'muito engracada',
            'bairro' : 'Caldas',
            'cidade' : 'Narnia'
        },
    },
    'juscelino' : {
        'telefone' : '67 987654321',
        'email' : 'jhytfr@gmail.com',
        'endereco' : {
            'rua' : 'Quadrada',
            'bairro' : 'Retangulo',
            'cidade' : 'Geometria'
        },
    },
}


def mostrarContatos():
    for contato in AGENDA:
        print(contato.upper())
        for info in AGENDA[contato]:
            if info == 'endereco':
                print('Endereco:')
                for endereco in AGENDA[contato][info]:
                    print(f'    {endereco}: {AGENDA[contato][info][endereco]}')
            else:
                print(f'{info} : {AGENDA[contato][info]}')
        print(f'{"-" * 50}\n')


def buscarContato():
    contato = input('Digite o nome do contato: ')
    exist = contato in AGENDA.keys()
    if exist:
        print(f'CONTATO ENCONTRADO!!\n{"-" * 50}')
        for info in AGENDA[contato]:
            if info == 'endereco':
                print('Endereco:')
                for endereco in AGENDA[contato][info]:
                    print(f'    {endereco}: {AGENDA[contato][info][endereco]}')
            else:
                print(f'{info} : {AGENDA[contato][info]}')
    else:
        print(f'CONTATO NÂO ENCONTRADO!!\n{"-" * 50}')

buscarContato()