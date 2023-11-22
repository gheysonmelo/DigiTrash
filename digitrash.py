import pygame
import serial
import sys

ser = serial.Serial('COM10', 9600)
pygame.init()

# Definindo cores
GREY = (128, 128, 128)  # Não Reciclável
GREEN = (0, 156, 59)  # Vidro
BLUE = (0, 143, 210)  # Papel
RED = (229, 36, 34)  # Plástico
YELLOW = (255, 209, 0)  # Metal
BROWN = (96, 56, 20)  # Orgânico
WHITE = (255, 255, 255)  # Lixo Hospitalar
BLACK = (0, 0, 0)  # Madeira
ORANGE = (255, 165, 0)  # Resíduos Perigosos
LIGHT_GRAY =(192,192,192) # active box

# Obtendo informações sobre a tela
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Inicializando a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DigiTrash!")

# Definindo a fonte para textos no jogo
font = pygame.font.Font(None, 48)
# Defininfo uma fonte maior para a rodada pegadinha
font_rodada = pygame.font.Font(None, 72)

# Função para obter o número de alunos
def get_num_alunos():
    screen.fill(WHITE)

    message_text = font.render("Olá Professor(a), quantos alunos participarão do jogo?", True, BLACK)
    message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(message_text, message_rect)

    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    color_inactive = WHITE
    color_active = LIGHT_GRAY
    color = color_inactive
    aluno_text = ''
    active = False

    save_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 60, 120, 50)
    save_color_inactive = pygame.Color('lightgreen')
    save_color_active = pygame.Color('darkgreen')
    save_color = save_color_inactive

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = color_active if active else color_inactive
                elif save_button.collidepoint(event.pos):
                    return int(aluno_text)

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return int(aluno_text)
                    elif event.key == pygame.K_BACKSPACE:
                        aluno_text = aluno_text[:-1]
                    else:
                        aluno_text += event.unicode

        txt_surface = font.render(aluno_text, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        pygame.draw.rect(screen, color, input_box, border_radius=15)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.draw.rect(screen, save_color, save_button, border_radius=10)
        save_text = font.render("Salvar", True, BLACK)
        save_rect = save_text.get_rect(center=save_button.center)
        screen.blit(save_text, save_rect)

        pygame.display.flip()

# função de keypress ou mousepress para continuar o jogo
def espera():
    keypress_encerrar = False
    while keypress_encerrar ==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                keypress_encerrar = True

# Função para ler o cartão RFID
def leitor_card():
    while True:
        if ser.in_waiting:
            data = ser.readline().decode('utf-8').split()
            for i in range(3):
                data.pop(0)
            data = ''.join(data)
            return data     

# Função para exibir uma pergunta na tela
def display_question(question_data, background_color, player):
    screen.fill(background_color)

    question_text = font.render(question_data["question"], True, background_color)
    question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(question_text, question_rect)
    player_name = font.render(f"{player}", True, WHITE)
    player_rect = player_name.get_rect(topleft=(10,10))
    screen.blit(player_name, player_rect)
    pygame.display.update()

# Função para exibir o início do jogo
def display_current_fase(fase):
    screen.fill(WHITE)
    start_text = font.render(f'Início {fase}', True, BLACK)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(start_text, start_rect)
    
    pygame.display.update()
    # Tempo para passar para o início verdadeiro do jogo - 2 segundos
    pygame.time.delay(2000)

# Função para exibir a vez do jogador
def display_player_turn(player_name, background_color):
    screen.fill(background_color)

    turn_text = font.render(f"Vez do jogador {player_name}", True, BLACK)
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)

    pygame.display.update()
    pygame.time.delay(2000)

# Função para exibir que o jogador acertou
def correct_answer():
        screen.fill(GREEN)
        turn_text = font_rodada.render(f"VOCÊ ACERTOU!", True, BLACK)
        turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(turn_text, turn_rect)
        pygame.display.update()
        # lembrar de aumentar esse tempo abaixo
        pygame.time.delay(500)

# Função para exibir que o jogador errou
def wrong_answer():
    screen.fill(RED)
    turn_text = font_rodada.render(f"VOCÊ ERROU!", True, BLACK)
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)
    pygame.display.update()
    # lembrar de aumentar esse tempo abaixo
    pygame.time.delay(500)

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
questions_fase_2 = [
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

# Loop principal do jogo
num_alunos = get_num_alunos()  # Obter o número de alunos do professor
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
display_current_fase("FASE 1")
pos = 0  # Qual player estaremos nos referindo
while num_alunos > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação
    
    display_player_turn(players[pos]["name"], WHITE)
    
    # Loop da fase 1
    running = True
    while running and current_question < len(questions):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Parar o jogo se o professor fechar a janela

        # Exibir a pergunta enquanto tiver perguntas a serem feitas 
        if current_question < len(questions):
            if current_question == 0:
                display_question(questions[current_question], RED, players[pos]['name'])
                               
                rfid_data = (leitor_card())
                if rfid_data == questions[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 1:
                display_question(questions[current_question], BLUE, players[pos]['name'])

                rfid_data = (leitor_card())
                if rfid_data == questions[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 2:
                display_question(questions[current_question], BROWN, players[pos]['name'])
                
                rfid_data = (leitor_card())
                if rfid_data == questions[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 3:
                display_question(questions[current_question], YELLOW, players[pos]['name'])

                rfid_data = (leitor_card())
                if rfid_data == questions[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 4:
                display_question(questions[current_question], GREEN, players[pos]['name'])

                rfid_data = (leitor_card())
                if rfid_data == questions[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
    
    # Exibir e atualizar o score do jogador aqui, fora do loop de eventos
    print("------------")
    print(f'{players[pos]["name"]} fez:')
    print("Score: ", score)
    players[pos]["score"] += score

    pos += 1
    num_alunos -= 1  # Reduz o número de alunos a cada vez que as perguntas são respondidas

# FASE 2
display_current_fase("FASE 2")
pos = 0  # Qual player estaremos nos referindo
while num_alunos2 > 0:
    current_question = 0  # Reinicia o índice da pergunta
    score = 0  # Reinicia a pontuação
    
    display_player_turn(players[pos]["name"], WHITE)
    
    # Loop da fase 2
    running = True
    while running and current_question < len(questions_fase_2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Parar o jogo se o professor fechar a janela
        
        # Exibir a pergunta enquanto tiver perguntas a serem feitas
        if current_question < len(questions_fase_2):
            if current_question == 0:
                display_question(questions_fase_2[current_question], GREEN, players[pos]['name'])
                               
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 1:
                display_question(questions_fase_2[current_question], YELLOW, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1                
            elif current_question == 2:
                display_question(questions_fase_2[current_question], RED, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 3:
                display_question(questions_fase_2[current_question], BLUE, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 4:
                display_question(questions_fase_2[current_question], BROWN, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 5:
                display_question(questions_fase_2[current_question], BROWN, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 6:
                display_question(questions_fase_2[current_question], BROWN, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1
            elif current_question == 7:
                display_question(questions_fase_2[current_question], BROWN, players[pos]['name'])
                rfid_data = (leitor_card())
                if rfid_data == questions_fase_2[current_question]["correct_answer"]:
                    score += 1
                    # chamaria uma função que mostra que acertou
                    correct_answer()
                else:
                    # chama uma função pra mostrar que errou
                    wrong_answer()
                # Move to the next question
                current_question += 1

    # Exibir e atualizar o score do jogador aqui, fora do loop de eventos
    print("------------")
    print(f'{players[pos]["name"]} fez:')
    print("Score: ", score)
    players[pos]["score"] += score

    pos += 1
    num_alunos2 -= 1  # Reduz o número de alunos a cada vez que as perguntas são respondidas

# Mostrando o score de cada jogador
screen.fill(WHITE)
for i, player in enumerate(players):
    end_text = font.render(f"Pontuação final de {player['name']}: {player['score']}/13", True, BLACK)
    screen.blit(end_text, (220, 140 + i * 50))  # Ajusta a posição vertical para cada jogador a partir do i. Fará com que cada posição seja diferente.
    pygame.display.update()  # As atualizações vão ser feitas imediatamente

espera()

pygame.quit()
sys.exit()