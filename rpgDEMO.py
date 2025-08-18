import os
import random
import time

atributos = {
    "arqueiro": [100, 30],
    "guerreiro": [150, 70],
    "mago": [100, 150]
}

itens_iniciais = {
    "arqueiro": ["arco", "poção de vida", "poção de mana"],
    "guerreiro": ["espada", "poção de vida", "poção de vida"],
    "mago": ["cajado", "poção de mana", "poção de mana"]
}

vidaPlayer = 0
manaPlayer = 0
xp = 0
nivel = 1
classe = ""
ataques = []
inventario = []
capacidade_maxima = 10
xpreq = 100

ataques_classe = {
    "arqueiro": [
        {"nome": "Flechas flamejantes", "dano": 20, "mana": 30},
        {"nome":"Flecha explosiva","dano":30,"mana":10},
        {"nome": "Chuva de flechas", "dano": 105, "mana": 100}

    ],
    "guerreiro": [
        {"nome": "Corte profundo", "dano": 25, "mana": 3},
        {"nome": "Investida do iluminado", "dano": 30, "mana": 5},
        {"nome":"Trovão celestial", "dano": 100, "mana": 115}
    ],
    "mago": [
        {"nome": "Bola de fogo", "dano": 30, "mana": 25},
        {"nome": "Projéteis mágicos", "dano": 15, "mana": 15},
        {"nome": "MAGO IMPLACAVEL", "dano":120, "mana": 95   }
    ]

}

inimigos = [
    {"nome": "Goblin", "vida": 100, "dano": 10},
    {"nome": "Orc", "vida": 150, "dano": 15},
    {"nome": "Esqueleto", "vida": 80, "dano": 12},
    {"nome": "Ladrão", "vida": 120, "dano":10}
]
inimigo = random.choice(inimigos)
vida_inimigo = inimigo["vida"]
tipo_inimigo = inimigo["nome"]
dano_inimigo = inimigo["dano"]

import sys
import time

def print_lento(texto, velocidade=0.08):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)

def limpar():
    if os.name == 'posix':
        time.sleep(2)
        os.system('clear')
    elif os.name == 'nt':
        time.sleep(2)
        os.system('cls')
        
def limpartxt():
    if os.name == 'posix':
        time.sleep(3)
        os.system('clear')
    elif os.name == 'nt':
        time.sleep(3)
        os.system('cls')

def mostrar_inventario():
    print("\n---Inventário---")
    if not inventario:
        print("Seu inventário está vazio.")
    else:
        for item in set(inventario):
            print(f"- {item} x{inventario.count(item)}")
    print(f"Total: {len(inventario)}/{capacidade_maxima}")

def adicionar_item(item):
    if len(inventario) < capacidade_maxima:
        inventario.append(item)
    else:
        print("Inventário cheio!!! Não foi possível adicionar o item.")

def usar_item():
    global vidaPlayer, manaPlayer
    mostrar_inventario()
    item = input("Digite o nome do item que deseja usar: ").strip().lower()
    if item not in inventario:
        print("Item não encontrado.")
        return
    if item == "poção de vida":
        vidaPlayer += 30
        print("Você usou uma poção de vida e recuperou 30 de vida.")
    elif item == "poção de mana":
        manaPlayer += 30
        print("Você usou uma poção de mana e recuperou 30 de mana.")
    else:
        print("Esse item não pode ser usado.")
        return
    inventario.remove(item)

def criarP():
    global vidaPlayer, manaPlayer, ataques, classe, nome

    while True:  
        nome = input("Antes de tudo, qual é o seu nome? ").strip()
        print(f"\nOlá, {nome.capitalize()}!")

        print("\nVocê precisa escolher uma classe:")
        print("1 - Mago     | Vida: 100 | Mana: 150")
        print("2 - Guerreiro| Vida: 150 | Mana: 70")
        print("3 - Arqueiro | Vida: 100 | Mana: 30\n")

        try:
            classe = int(input("Insira o número da sua classe: ").strip())
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if classe == 1:
            classe_nome = "mago"
        elif classe == 2:
            classe_nome = "guerreiro"
        elif classe == 3:
            classe_nome = "arqueiro"
        else:
            print("Classe inválida. Tente novamente.\n")
            continue
        vidaPlayer, manaPlayer = atributos[classe_nome]
        ataques = ataques_classe[classe_nome]
        classe = classe_nome
        for item in itens_iniciais[classe]:
            adicionar_item(item)

        limpar()

        print(f"{classe_nome.capitalize()} | Vida: {vidaPlayer} | Mana: {manaPlayer}")
        print("\nSeus Ataques:")
        for ataque in ataques:
            print(f"- {ataque['nome']} | Dano: {ataque['dano']} | Mana: {ataque['mana']}")

        mostrar_inventario()


        classeE = input("\nTem certeza que esse é seu personagem? (s/n): ").strip().lower()
        if classeE == "s":
            print("\nAgora você está pronto!!!")
            limpar()
            break

        elif classeE == "n":
            limpar()
            print("Voltando para a criação de personagem...\n")
        else:
            print("Resposta inválida. Vamos tentar novamente.")
            limpar()

def LvUp():
    global xp, nivel, xpreq, vidaPlayer, manaPlayer

    if xp >= xpreq:
        nivel += 1
        xpreq += 100
        xp = 0
        print(f"\nVocê subiu para o nivel {nivel}")
        vidaPlayer += 15
        manaPlayer += 25
        print(f"\nSua vida aumentou em 15 pontos")
        print(f"\nSua Mana aumentou em 25 pontos")

def batalha():
    global vida_inimigo, vidaPlayer, manaPlayer, xp, nivel

    print(f"\nUm {tipo_inimigo} apareceu! Vida: {vida_inimigo}\n")

    while vida_inimigo > 0 and vidaPlayer > 0:
        print("Seu turno:")
        print(f"Vida: {vidaPlayer} | Mana: {manaPlayer}")
        print(f"Inimigo: {tipo_inimigo} | Vida: {vida_inimigo}\n")

        print("1 - Atacar")
        print("2 - Inventário")
        print("3 - Fugir")
        manaPlayer += 5
        try:
            acao = int(input("Escolha uma ação: "))
        except ValueError:
            print("Ação inválida.")
            time.sleep(1)
            limpar()
            continue

        if acao == 1:
            print("\nAtaques:")
            for i, atk in enumerate(ataques):
                print(f"{i+1} - {atk['nome']} (Dano: {atk['dano']} | Mana: {atk['mana']})")
            try:
                escolha = int(input("Escolha seu ataque: ")) - 1
                if escolha not in range(len(ataques)):
                    print("Ataque inválido.")
                    time.sleep(1)
                    limpar()
                    continue
                ataque = ataques[escolha]
                if manaPlayer < ataque["mana"]:
                    print("Mana insuficiente.")
                    time.sleep(1)
                    limpar()
                    continue

                manaPlayer -= ataque["mana"]
                vida_inimigo -= ataque["dano"]
                print(f"\nVocê usou {ataque['nome']} e causou {ataque['dano']} de dano.")

                if vida_inimigo <= 0:
                    print(f"{tipo_inimigo} foi derrotado!")
                    xp += 25
                    print(f"XP ganho: 25 | Total: {xp}/{xpreq}")
                    LvUp()

                    break
            except ValueError:
                print("Escolha inválida.")
                time.sleep(1)
                limpar()
                continue

        elif acao == 2:
            while True:
                print("\n1 - Ver inventário")
                print("2 - Usar item")
                print("3 - Voltar")
                escolha = input("Escolha: ")

                if escolha == "1":
                    mostrar_inventario()

                elif escolha == "2":
                    usar_item()

                elif escolha == "3":
                    break
                else:
                    print("Opção inválida.")
            time.sleep(1)

        elif acao == 3:
            print("Você fugiu da batalha.")
            break
        else:
            print("Ação inválida.")
            time.sleep(1)

        if vida_inimigo > 0:
            dano = random.randint(5, dano_inimigo)
            vidaPlayer -= dano
            print(f"\nO {tipo_inimigo} atacou e causou {dano} de dano.")
            if vidaPlayer <= 0:
                print("Você foi derrotado.")

        time.sleep(2)  
        limpar()


def batalhaBOSS():
    global vidaPlayer, manaPlayer, xp, nivel

    boss = {"nome": "......C̷̻̿U̷̼̜͊̐K̴̯̜̑͘T̸̜̤̽̒H̷̞̱̓U̸͉̚L̵̦̍Ǘ̸̥̯͗......", "vida": 500, "dano": 99999}
    vida_boss = boss["vida"]
    tipo_boss = boss["nome"]
    dano_boss = boss["dano"]
    print_lento(".....")
    print_lento("\nVocê se encontra no vazio absoluto.")
    print_lento("\nA gravidade some... o som cessa... o tempo parece congelar.")
    print_lento("\n........")
    print_lento("\nNo horizonte inexistente, uma silhueta colossal começa a emergir...")
    print_lento("\nLuz turquesa dança ao redor de tentáculos infinitos...")
    print_lento("....")
    print_lento("\nUma presença ancestral desperta...")
    print_lento("\nDOS ABISMOS MAIS PROFUNDOS E DAS DIMENSÕES ESQUECIDAS PELO TEMPO...")
    print_lento("\nO IMPERADOR DO CAOS SE MANIFESTA....")
    print_lento("\nE O NOME DELE QUEIMA SUA MENTE COMO UM VENENO:")
    print_lento("\n......C̷̻̿U̷̼̜͊̐K̴̯̜̑͘T̸̜̤̽̒H̷̞̱̓U̸͉̚L̵̦̍Ǘ̸̥̯͗......")
    print_lento("\nSeu corpo falha. Suas pernas tremem. Sua visão escurece......")
    print_lento("\n.........")
    print_lento("\nMas não há como escapar agora...")
    print_lento("\nVocê foi escolhido para enfrentar a insanidade encarnada.")
    print_lento("\n.....")
    limpar()
    print(f"\n {tipo_boss} apareceu!!!!!!!!!! Vida: {vida_boss}\n")

    while vida_boss > 0 and vidaPlayer > 0:
        print(f"\nSeu turno | Vida: {vidaPlayer} | Mana: {manaPlayer}")
        print(f"{tipo_boss} | Vida: {vida_boss}")
        print("1 - Atacar\n2 - Inventário\n3 - Fugir")
        manaPlayer += 10

        try:
            acao = int(input("Escolha uma ação: "))
        except ValueError:
            print("Ação inválida.")
            continue

        if acao == 1:
            print("\nAtaques:")
            for i, atk in enumerate(ataques):
                print(f"{i+1} - {atk['nome']} (Dano: {atk['dano']} | Mana: {atk['mana']})")
            try:
                escolha = int(input("Escolha seu ataque: ")) - 1
                ataque = ataques[escolha]
                if manaPlayer < ataque["mana"]:
                    print("Mana insuficiente.")
                    continue
                manaPlayer -= ataque["mana"]
                vida_boss -= ataque["dano"]
                print(f"\nVocê usou {ataque['nome']} e causou {ataque['dano']} de dano!")
            except:
                print("Escolha inválida.")
                continue

        elif acao == 2:
            mostrar_inventario()
            usar_item()

        elif acao == 3:
            print("Você tentou fugir, mas ELE não permite!")
            continue

        if vida_boss > 0:
            dano = random.randint(10, dano_boss)
            vidaPlayer -= dano
            print(f"O {tipo_boss} atacou e causou {dano} de dano.")
            if vidaPlayer <= 0:
                print(f"Você foi derrotado pelo {tipo_boss}...")
                return

    print(f" Parabéns! Você derrotou o {tipo_boss}!")
    print("E assim Acaba  ")



criarP()

print_lento("\nVocê acorda em uma masmorra, acorrentado e com a cabeça latejando...")
print_lento("\nCom esforço, você se liberta das correntes enferrujadas e sai da cela escura.")
print_lento("\nMais à frente, um barulho estranho ecoa pelos corredores úmidos e silenciosos...")
print_lento("....")

limpartxt()

batalha()

limpar()

limpar()
print_lento("\nApós a batalha, você continua vagando pela masmorra escura e opressora...")

print_lento("\nVocê sente que está sendo observado.")
print_lento("\nDe repente, um toque gélido em seu ombro congela sua espinha.")

print_lento("\n— EI! Você aí, carinha esquisito!")
print_lento("\n— O que cê tá fazendo nessa masmorra, hein?")
print_lento("\n— Vixi... tá todo sujo, empoeirado... parece que saiu direto do inferno.")
print_lento("......")
print_lento("\n— Que foi? Um gato comeu sua língua?")
print_lento("\n— Eh... isso não importa agora.")
print_lento("\n— Meu nome é Moacir.")

print_lento(f"\n# Você escreve seu nome num pedaço de papel sujo que Moacir te entrega #")
print_lento(f"\n— {nome.upper()}?! Hahaha, que nome massa! Nunca conheci alguém com esse nome...")

print_lento(f"\n— Vem comigo, {nome}. Eu sei onde fica a saída dessa encrenca.")

limpartxt()

limpartxt()
print("Vocês dois caminham cautelosamente até a saída da masmorra...")

limpartxt()
print_lento("De repente, uma luz intensa atravessa a escuridão...")

print_lento("Você é cegado pelo brilho do desconhecido.")

print_lento("..........")

limpar()

batalhaBOSS()