opçao = 0

alunos = ['Jose', 'Luis', 'Kaio']
notas =[4.9, 6.0, 9.6]
while opçao != 9:
    print(' \n' * 2)
    print('<>'*60)
    opçao = input('''ESCOLHA UMA OPÇÃO:
   1 Listar alunos              |  10 Buscar aluno por nome 
   2 Adicionar aluno            |  11 Buscar aluno por posição 
   3 Adicionar nota             |  12 Exibir melhor aluno 
   4 Remover aluno              |  13 Exibir alunos ordenados por nota 
   5 Remover nota               |  14 Exibir alunos por ordem alfabética
   6 Editar nome do aluno       |  15 Exibir aprovados por média 
   7 Editar nota do aluno       |  16 Exibir alunos na final 
   8 Calcular Média da turma    |  17 Exibir alunos reprovados 
   9 Encerrar Programa
    Digite sua opção:''''')
    print(' \n'*2)
    print('-='*60)
    if opçao.isalpha() == True:
        print('Digite uma opção válida')
    else:
        opçao = int(opçao)
        if opçao == 1:
            print('ALUNOS''     ''NOTAS')
            for v in range(len(alunos)):
                print('{:^4}''      ''{:^4}'.format(alunos[v], notas[v]))
        elif opçao == 2:
            nome = input('Digite o nome do alunos')
            if nome in alunos:
                print('Erro, aluno existente')
            else:
                alunos.append(nome)
                if nome in alunos:
                    pos = alunos.index(nome)
                    notas.append(-1)
                    print('Aluno adicionado!')
        elif opçao == 3:
            buscar_aluno = input('Qual o nome do aluno?')
            if buscar_aluno in alunos:
                pos = alunos.index(buscar_aluno)
                if notas[pos] == (-1):
                    nota = float(input('Digite a nota do aluno:'))
                    notas[pos] = nota
                    print('Nota adicionada com sucesso')
                else:
                    print('Não é possivel adicionar, escolha opção 7.')
            else:
                print('Aluno não cadastrado!')
        elif opçao == 4:
            removealuno = input('Qual aluno deseja remover?')
            if removealuno in alunos:
                pos = alunos.index(removealuno)
                del alunos[pos]
                del notas[pos]
                print('Aluno Removido com sucesso')
            else:
                print('Nome não cadastrado')
        elif opçao == 5:
            nome = input('Digite o nome do aluno:')
            if nome in alunos:
                pos = alunos.index(nome)
                del notas[pos]
                notas.insert(pos, (-1))
                print('Nota removida com sucesso')
            else:
                print('Nome não cadastrado')
        elif opçao == 6:
            nome = input('Digite o nome à ser editado:')
            if nome in alunos:
                pos = alunos.index(nome)
                novonome = str(input('Qual o novo nome?'))
                del alunos[pos]
                alunos.insert(pos, novonome)
                print('Nome editado com sucesso')
            else:
                print('Nome não cadastrado')
        elif opçao == 7:
            nome = input('Qual aluno quer editar a nota?')
            if nome in alunos:
                pos = alunos.index(nome)
                v = notas[pos]
                novanota = float(input('Digite a nova nota'))
                if -1 != v:
                    del notas[pos]
                    notas.insert(pos, novanota)
                    print('Nota editada com sucesso')
                else:
                    print('Não é possível editar, use opção 3.')
            else:
                print('Nome não cadastrado!')
        elif opçao == 8:
            t = 0
            for a in notas:
                t = t+a
            media = t/len(notas)
            print('A turma tem média de {:.1f}'.format(media))
            if media < 7.0:
                print('Sua turma está abaixo da média')
            elif 7.0 < media < 8.0:
                print('Sua turma está na média')
            else:
                print('Sua turma tem ótimo desempenho')
        elif opçao == 10:
            nome = input('Qual o nome a ser buscado?')
            if nome in alunos:
                pos = alunos.index(nome)
                nota = notas[pos]
                print('{} tem nota {}'.format(nome, nota))
            else:
                print('Nome não cadastrado')
        elif opçao == 11:
            buscapos = int(input('Qual a posição do aluno?'))
            if buscapos in range(0, len(alunos)):
                nome = alunos[buscapos]
                nota = notas[buscapos]
                print('{} tem nota {}'.format(nome, nota))
            else:
                print('Posição Inexistente')
        elif opçao == 12:
            maior = 0
            for a in notas:
                if a > maior:
                    maior = a
            pos = notas.index(maior)
            print('Melhor aluno:\n{} com nota {}'.format(alunos[pos], notas[pos]))
        elif opçao == 13:
            for a in range(len(notas)):
                w = a
                while w > 0 and notas[w] < notas[w-1]:
                    notas[w], notas[w-1] = notas[w-1], notas[w]
                    alunos[w], alunos[w-1] = alunos[w-1], alunos[w]
                    w -= 1
            print('ALUNOS''     ''NOTAS')
            for b in range(len(notas)):
                print('{}''        ''{}'.format(alunos[b], notas[b]))
        elif opçao == 14:
            for a in range(len(alunos)):
                m = a
                while m > 0 and alunos[m] < alunos[m-1]:
                    alunos[m], alunos[m-1] = alunos[m-1], alunos[m]
                    notas[m], notas[m-1] = notas[m-1], notas[m]
                    m -= 1
            print('ALUNOS''          ''NOTAS')
            for c in range(len(alunos)):
                print('{:^3}''        ''{:^3}'.format(alunos[c], notas[c]))
        elif opçao == 15:
            aprovados = False
            print('ALUNOS APROVADOS')
            for a in notas:
                if a >= 7.0:
                    aprovados = True
                    pos = notas.index(a)
                    print('{:^3}''   ''{:^3}'.format(alunos[pos], notas[pos]))
            if aprovados == False:
                print('Nenhum aluno foi Aprovado!')
        elif opçao == 16:
            final = False
            print('ALUNOS NA FINAL')
            for f in notas:
                if 5 <= f <= 6.9:
                    final = True
                    pos = notas.index(f)
                    print('{:^3}''   ''{:^3}'.format(alunos[pos], notas[pos]))
            if final == False:
                print('Nenhum aluno está na final')
        elif opçao == 17:
            reprovado = False
            print('ALUNOS REPROVADOS')
            for r in notas:
                if r < 5:
                    reprovado = True
                    pos = notas.index(r)
                    print('{:^3}''    ''{:^3}'.format(alunos[pos], notas[pos]))
            if reprovado == False:
                print('Nenhum aluno está Reprovado!')
        elif 0 > opçao > 17 or opçao != 9 :
            print('Digite uma opção válida.')


print('==============PROGRAMA ENCERRADO==============VOLTE SEMPRE===============')
