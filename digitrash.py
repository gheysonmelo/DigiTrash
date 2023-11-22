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
GRAY = (128, 128, 128)  # Não Reciclável
GREEN = (0, 156, 59)  # Vidro
BLUE = (0, 143, 210)  # Papel
RED = (229, 36, 34)  # Plástico
YELLOW = (255, 209, 0)  # Metal
BROWN = (96, 56, 20)  # Orgânico
WHITE = (255, 255, 255)  # Lixo Hospitalar
BLACK = (0, 0, 0)  # Madeira
ORANGE = (255, 165, 0)  # Resíduos Perigosos
LIGHT_GRAY =(192,192,192) # active box

# Chamada da função que inicializa a tela
screen, WIDTH, HEIGHT = funcoes.init_screen()

# Definindo a fonte para textos no jogo
font = pygame.font.Font(None, 48)
# Defininfo uma fonte maior para a rodada pegadinha
font_rodada = pygame.font.Font(None, 72)

# Lista de questões, contendo dicionários para cada questão
questions = [
    # Primeira pergunta
    {
        "question": "1. Dica: Da cor do amor e dos morangos esta lixeira, mas aqui você guarda garrafas e potes.",
        "options": [""],
        "correct_answer": "831D4AAC",
    },
    # Segunda pergunta
    {
        "question": "2. Dica: É a cor do céu em um dia ensolarado, mas aqui é onde desenhamos e escrevemos.",
        "options": [""],
        "correct_answer": "F3DC64AC",
    },
    # Terceira pergunta
    {
        "question": "3. Dica: Marrom como o que? A casca de um kiwi?",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Quarta pergunta
    {
        "question": "4. Dica: É onde seu refrigerante fica antes de você beber. Parece uma jóia pequenininha.",
        "options": [""],
        "correct_answer": "E35F21AC",
    },
    # Quinta pergunta
    {
        "question": "5. Dica: Parece gelo, mas não derrete e quebra facil se não tiver cuidado!",
        "options": [""],
        "correct_answer": "73EB58AC",
    }
]

# Lista de questões da fase 2, contendo dicionários para cada questão
questions_fase2 = [
    # Primeira pergunta
    {
        "question": "5. Dica: Parece gelo, mas não derrete e quebra facil se não tiver cuidado!",
        "options": [""],
        "correct_answer": "73EB58AC",
    },
    # Segunda pergunta
    {
        "question": "4. Dica: É onde seu refrigerante fica antes de você beber. Parece uma jóia pequenininha.",
        "options": [""],
        "correct_answer": "E35F21AC",
    },
    # Terceira pergunta
    {
        "question": "1. Dica: Da cor do amor e dos morangos esta lixeira, mas aqui você guarda garrafas e potes.",
        "options": [""],
        "correct_answer": "831D4AAC",
    },
    # Quarta pergunta
    {
        "question": "2. Dica: É a cor do céu em um dia ensolarado, mas aqui é onde desenhamos e escrevemos.",
        "options": [""],
        "correct_answer": "F3DC64AC",
    },
    # Quinta pergunta
    {
        "question": "3. Dica: Marrom como o que? A casca de um kiwi?",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Sexta pergunta
    {
        "question": "3. Dica: Marrom como o que? A casca de um kiwi?",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Sétima pergunta
    {
        "question": "3. Dica: Marrom como o que? A casca de um kiwi?",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Oitava pergunta
    {
        "question": "3. Dica: Marrom como o que? A casca de um kiwi?",
        "options": [""],
        "correct_answer": "938460AD",
    },
    ]

# Lista de questões da fase 3, contendo dicionários para cada questão
questions_fase3 = [
    # Primeira pergunta
    {
        "question": "PAPEL",
        "options": [""],
        "correct_answer": "E35F21AC",
    },
    # Segunda pergunta
    {
        "question": "METAL",
        "options": [""],
        "correct_answer": "73EB58AC",
    },
    # Terceira pergunta
    {
        "question": "PAPEL",
        "options": [""],
        "correct_answer": "F3DC64AC",
    },
    # Quarta pergunta
    {
        "question": "PLASTICO",
        "options": [""],
        "correct_answer": "E35F21AC",
    },
    # Quinta pergunta
    {
        "question": "VIDRO",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Sexta pergunta - AQUI VAI SER CINZA
    {
        "question": "MADEIRA",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Sétima pergunta
    {
        "question": "ORGANICO",
        "options": [""],
        "correct_answer": "831D4AAC",
    },
    # Oitava pergunta
    {
        "question": "RESIDUOS PERIGOSOS",
        "options": [""],
        "correct_answer": "73EB58AC",
    },
    # Nona pergunta - AQUI VAI SER LARANJA
    {
        "question": "VIDRO",
        "options": [""],
        "correct_answer": "E35F21AC",
    },
    # Décima pergunta
    {
        "question": "PAPEL",
        "options": [""],
        "correct_answer": "938460AD",
    },
    # Décima primeira pergunta - AQUI VAI SER PRETO
    {
        "question": "METAL",
        "options": [""],
        "correct_answer": "F3DC64AC",
    },
    # Décima segunda pergunta
    {
        "question": "PLASTICO",
        "options": [""],
        "correct_answer": "831D4AAC",
    },
    # Décima terceira pergunta
    {    
        "question": "VIDRO",
        "options": [""],
        "correct_answer": "F3DC64AC",
    },
    ]

# Loop principal do jogo
# Obtém o número de alunos
num_alunos = funcoes.get_num_alunos(screen, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GRAY, font)
num_alunos2 = num_alunos
num_alunos3 = num_alunos
players = []  # Lista de jogadores

for i in range(num_alunos):
    player = {
        "name": f"player " + str(i),
        "score": 0
    }
    players.append(player)

# FASE 1
funcoes.display_current_fase(screen, font, WIDTH, HEIGHT, "FASE 1")
pos = 0  # Qual player estaremos nos referindo
while num_alunos > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação

    def question(current_question, color):
        funcoes.display_question(screen, font, WIDTH, HEIGHT, questions[current_question], color, players[pos]['name'])
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_rodada, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer(screen, font_rodada, WIDTH, HEIGHT)
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
                n = question(current_question, RED)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 1:
                n = question(current_question, BLUE)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 2:
                n = question(current_question, BROWN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 3:
                n = question(current_question, YELLOW)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 4:
                n = question(current_question, GREEN)
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
    
    def question_fase2(current_question, color):
        funcoes.display_question(screen, font, WIDTH, HEIGHT, questions_fase2[current_question], color, players[pos]['name'])
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions_fase2[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_rodada, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer(screen, font_rodada, WIDTH, HEIGHT)
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
                n = question_fase2(current_question, GREEN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 1:
                n = question_fase2(current_question, YELLOW)
                score += n
                current_question += 1 # Move to the next question             
            elif current_question == 2:
                n = question_fase2(current_question, RED)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 3:
                n = question_fase2(current_question, BLUE)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 4:
                n = question_fase2(current_question, BROWN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 5:
                n = question_fase2(current_question, BROWN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 6:
                n = question_fase2(current_question, BROWN)
                score += n
                current_question += 1 # Move to the next question
            elif current_question == 7:
                n = question_fase2(current_question, BROWN)
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
        funcoes.display_question_fase3(screen, font, WIDTH, HEIGHT, questions_fase3[current_question], color1, players[pos]['name'], color2)
        rfid_data = (funcoes.leitor_card(ser))
        if rfid_data == questions_fase3[current_question]["correct_answer"]:
            # Mostra que acertou
            funcoes.correct_answer(screen, font_rodada, WIDTH, HEIGHT)
            return 1
        else:
            # Mostra que errou
            funcoes.wrong_answer(screen, font_rodada, WIDTH, HEIGHT)
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