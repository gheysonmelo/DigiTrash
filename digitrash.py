# Importando bibliotecas necessárias
import pygame
import sys

#  importando o arquivo de funções  
import funcoes

# Inicializando o leitor RFID
ser = funcoes.init_serial()

# Inicializando o pygame
funcoes.init_pygame()

# Definindo cores
GRAY = (169,169,169)  # Não Reciclável
GREEN = (0, 156, 59)  # Vidro
BLUE = (0, 143, 210)  # Papel
RED = (229, 36, 34)  # Plástico
YELLOW = (255, 209, 0)  # Metal
BROWN = (96, 56, 20)  # Orgânico
WHITE = (255, 255, 255)  # Lixo Hospitalar
BLACK = (0, 0, 0)  # Madeira
ORANGE = (255,69,0)  # Resíduos Perigosos
LIGHT_GRAY =(192,192,192) # active box

# Chamada da função que inicializa a tela
screen, WIDTH, HEIGHT = funcoes.init_screen()

# Definindo fontes para textos no jogo
font = pygame.font.Font("fonts/Montserrat-Bold.ttf", 38)
font_72 = pygame.font.Font("fonts/Montserrat-Bold.ttf", 58)
# Defininfo uma fonte maior para a rodada pegadinha
font_144 = pygame.font.Font("fonts/Montserrat-Bold.ttf", 110)
# Fontes
fonte_botoes = pygame.font.Font("fonts/Montserrat-Bold.ttf", 30)


# Lista de questões, contendo dicionários para cada questão
questions = [
    # Primeira pergunta
    {
        "question": "1. Sou material de garrafas, embalagens e faço brinquedos",
        "correct_answer": "834B4FAC",
        "answer": "Plástico"
    },
    # Segunda pergunta
    {
        "question": "2. Sou liso, branco e carrego histórias. O que sou?",
        "correct_answer": "F3DC64AC",
        "answer": "Papel"
    },
    # Terceira pergunta
    {
        "question": "3. Sou da terra, apodreço e viro adubo. O que sou?",
        "correct_answer": "938460AD",
        "answer": "Orgânico"
    },
    # Quarta pergunta
    {
        "question": "4. Sou duro, brilho muito e gosto de ser reciclado. O que sou?",
        "correct_answer": "E35F21AC",
        "answer": "Metal"
    },
    # Quinta pergunta
    {
        "question": "5. Sou transparente, quebro fácil e reciclo. O que sou?",
        "correct_answer": "13BB50AC",
        "answer": "Vidro"
    }
]

# Lista de questões da fase 2, contendo dicionários para cada questão
questions_fase2 = [
    # Primeira pergunta
    {
        "question": "1. Parece gelo, mas não derrete e quebra facil se não tiver cuidado!",
        "correct_answer": "13BB50AC",
        "answer": "Vidro"
    },
    # Segunda pergunta
    {
        "question": "2. É onde seu refrigerante fica antes de você beber. Parece uma jóia pequenininha.",
        "correct_answer": "E35F21AC",
        "answer": "Metal"
    },
    # Terceira pergunta
    {
        "question": "3. Da cor do amor e dos morangos esta lixeira, mas aqui você guarda garrafas e potes.",
        "correct_answer": "834B4FAC",
        "answer": "Plástico"
    },
    # Quarta pergunta
    {
        "question": "4. É a cor do céu em um dia ensolarado, mas aqui é onde desenhamos e escrevemos.",
        "correct_answer": "F3DC64AC",
        "answer": "Papel"
    },
    # Quinta pergunta
    {
        "question": "5. Marrom como o que? A casca de um kiwi?",
        "correct_answer": "938460AD",
        "answer": "Orgânico"
    },
    # Sexta pergunta
    {
        "question": "6. PRETO",
        "correct_answer": "D57FABAC",
        "answer": "Madeira"
    },
    # Sétima pergunta
    {
        "question": "7. LARANJA",
        "correct_answer": "B3205CAD",
        "answer": "Resíduos Perigosos"
    },
    # Oitava pergunta
    {
        "question": "8. CINZA",
        "correct_answer": "A3CF3BAC",
        "answer": "Não Reciclável"
    },
    ]

# Lista de questões da fase 3, contendo dicionários para cada questão
questions_fase3 = [
    # Primeira pergunta
    {
        "question": "PAPEL",
        "correct_answer": "E35F21AC",
        "answer": "Metal"
    },
    # Segunda pergunta
    {
        "question": "METAL",
        "correct_answer": "13BB50AC",
        "answer": "Vidro"
    },
    # Terceira pergunta
    {
        "question": "PAPEL",
        "correct_answer": "F3DC64AC",
        "answer": "Papel"
    },
    # Quarta pergunta
    {
        "question": "PLASTICO",
        "correct_answer": "E35F21AC",
        "answer": "Metal"
    },
    # Quinta pergunta
    {
        "question": "VIDRO",
        "correct_answer": "938460AD",
        "answer": "Orgânico"
    },
    # Sexta pergunta
    {
        "question": "MADEIRA",
        "correct_answer": "A3CF3BAC",
        "answer": "Não Reciclável"
    },
    # Sétima pergunta
    {
        "question": "ORGANICO",
        "correct_answer": "834B4FAC",
        "answer": "Plástico"
    },
    # Oitava pergunta
    {
        "question": "RESIDUOS PERIGOSOS",
        "correct_answer": "13BB50AC",
        "answer": "Vidro"
    },
    # Nona pergunta
    {
        "question": "VIDRO",
        "correct_answer": "B3205CAD",
        "answer": "Resíduos Perigosos"
    },
    # Décima pergunta
    {
        "question": "PAPEL",
        "correct_answer": "938460AD",
        "answer": "Orgânico"
    },
    # Décima primeira pergunta
    {
        "question": "METAL",
        "correct_answer": "D57FABAC",
        "answer": "Madeira"
    },
    # Décima segunda pergunta
    {
        "question": "PLASTICO",
        "correct_answer": "834B4FAC",
        "answer": "Plástico"
    },
    # Décima terceira pergunta
    {    
        "question": "VIDRO",
        "correct_answer": "F3DC64AC",
        "answer": "Papel"
    },
    ]

# Loop principal do jogo
# Obtém o número de alunos
# num_alunos = funcoes.get_num_alunos(screen, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GRAY, font)
num_alunos, nomes_alunos = funcoes.get_num_alunos(screen, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GRAY, font, fonte_botoes)
print(f"Número de alunos: {num_alunos}")
print("Nomes dos alunos:", nomes_alunos)
num_alunos2 = num_alunos
num_alunos3 = num_alunos
players = []  # Lista de jogadores

for i in range(num_alunos):
    player = {
        "name": nomes_alunos[i].upper(),
        "score": 0
    }
    players.append(player)

# FASE 1
funcoes.display_current_fase(screen, font, WIDTH, HEIGHT, "FASE 1")
pos = 0  # Qual player estaremos nos referindo
while num_alunos > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação

    def question(current_question, color, answer):
        funcoes.display_question_fase1(screen, font, WIDTH, HEIGHT, questions[current_question], color, players[pos]['name'])
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_72, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer(screen, font_72, WIDTH, HEIGHT, answer, font)
            return 0
    
    # Mostra na tela o nome do jogador da vez
    funcoes.display_player_turn(screen, font, WIDTH, HEIGHT, players[pos]["name"], WHITE)
    
    # Loop da fase 1
    running = True
    while running and current_question < len(questions):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Parar o jogo se o professor fechar a janela

        # Exibir a pergunta enquanto tiver perguntas a serem feitas 
        if current_question < len(questions):
            if current_question == 0:
                n = question(current_question, RED, questions[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 1:
                n = question(current_question, BLUE, questions[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 2:
                n = question(current_question, BROWN, questions[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 3:
                n = question(current_question, YELLOW, questions[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 4:
                n = question(current_question, GREEN, questions[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
    
    # Exibir e atualizar o score do jogador aqui, fora do loop de eventos
    print("------------")
    print(f'{players[pos]["name"]} fez:')
    print("Score: ", score)
    players[pos]["score"] += score

    pos += 1
    num_alunos -= 1  # Reduz o número de alunos a cada vez que as perguntas são respondidas

# FASE 2
funcoes.display_current_fase(screen, font, WIDTH, HEIGHT, "FASE 2")
pos = 0  # Qual player estaremos nos referindo
while num_alunos2 > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação
    
    def question_fase2(current_question, color, answer):
        funcoes.display_question(screen, font, WIDTH, HEIGHT, questions_fase2[current_question], color, players[pos]['name'])
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions_fase2[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_72, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer(screen, font_72, WIDTH, HEIGHT, answer, font)
            return 0

    # Mostra na tela o nome do jogador da vez
    funcoes.display_player_turn(screen, font, WIDTH, HEIGHT, players[pos]["name"], WHITE)
    
    # Loop da fase 2
    running = True
    while running and current_question < len(questions_fase2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Parar o jogo se o professor fechar a janela
        
        # Exibir a pergunta enquanto tiver perguntas a serem feitas
        if current_question < len(questions_fase2):
            if current_question == 0:
                n = question_fase2(current_question, GREEN, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 1:
                n = question_fase2(current_question, YELLOW, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question             
            elif current_question == 2:
                n = question_fase2(current_question, RED, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 3:
                n = question_fase2(current_question, BLUE, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 4:
                n = question_fase2(current_question, BROWN, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 5:
                n = question_fase2(current_question, BLACK, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 6:
                n = question_fase2(current_question, ORANGE, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 7:
                n = question_fase2(current_question, GRAY, questions_fase2[current_question]["answer"])
                score += n
                current_question += 1 # Move to the next question

    # Exibir e atualizar o score do jogador aqui, fora do loop de eventos
    print("------------")
    print(f'{players[pos]["name"]} fez:')
    print("Score: ", score)
    players[pos]["score"] += score

    pos += 1
    num_alunos2 -= 1  # Reduz o número de alunos a cada vez que as perguntas são respondidas

# FASE 3
funcoes.display_current_fase(screen, font, WIDTH, HEIGHT, "FASE 3")
pos = 0  # Qual player estaremos nos referindo
while num_alunos3 > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação

    def question_fase3(current_question, color1, color2):
        funcoes.display_question_fase3(screen, font, WIDTH, HEIGHT, questions_fase3[current_question], color1, players[pos]['name'], color2, font_144)
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions_fase3[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_72, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer_fase3(screen, font_72, WIDTH, HEIGHT)
            return 0

    # Mostra na tela o nome do jogador da vez
    funcoes.display_player_turn(screen, font, WIDTH, HEIGHT, players[pos]["name"], WHITE)
    
    # Loop da fase 3
    running = True
    while running and current_question < len(questions_fase3):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Parar o jogo se o professor fechar a janela
        
        # Exibir a pergunta enquanto tiver perguntas a serem feitas
        if current_question < len(questions_fase3):
            if current_question == 0:
                n = question_fase3(current_question, YELLOW, BLUE)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 1:
                n = question_fase3(current_question, GREEN, RED)
                score += n
                current_question += 1 # Move to the next question              
            elif current_question == 2:
                n = question_fase3(current_question, BLUE, GREEN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 3:
                n = question_fase3(current_question, YELLOW, BROWN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 4:
                n = question_fase3(current_question, BROWN, YELLOW)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 5:
                n = question_fase3(current_question, GRAY, RED)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 6:
                n = question_fase3(current_question, RED, YELLOW)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 7:
                n = question_fase3(current_question, GREEN, BLUE)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 8:
                n = question_fase3(current_question, ORANGE, GREEN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 9:
                n = question_fase3(current_question, BROWN, RED)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 10:
                n = question_fase3(current_question, BLACK, RED)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 11:
                n = question_fase3(current_question, RED, BLUE)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 12:
                n = question_fase3(current_question, BLUE, YELLOW)
                score += n
                current_question += 1 # Move to the next question

    # Exibir e atualizar o score do jogador aqui, fora do loop de eventos
    print("------------")
    print(f'{players[pos]["name"]} fez:')
    print("Score: ", score)
    players[pos]["score"] += score

    pos += 1
    num_alunos3 -= 1  # Reduz o número de alunos a cada vez que as perguntas são respondidas

# Mostrando o score de cada jogador
screen.fill(WHITE)
for i, player in enumerate(players):
    end_text = font.render(f"Pontuação final de {player['name']}: {player['score']}/26", True, BLACK)
    screen.blit(end_text, (220, 140 + i * 50))  # Ajusta a posição vertical para cada jogador a partir do i. Fará com que cada posição seja diferente.
    pygame.display.update()  # As atualizações vão ser feitas imediatamente

funcoes.espera()

pygame.quit()
sys.exit()