# Importando bibliotecas necessárias
import pygame
import serial
import sys

# Função que inicializa a tela do jogo
def init_screen():
    # Obtendo informações sobre a tela
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

    # Inicializando a janela do jogo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DigiTrash!")

    return screen, WIDTH, HEIGHT

# Função para obter o número de alunos
def get_num_alunos(screen, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GRAY, font):
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

# Função para inicializar o leitor RFID
def init_serial():
    # Inicializando o leitor RFID
    ser = serial.Serial('COM10', 9600)
    return ser

# Função para inicializar o pygame
def init_pygame():
    pygame.init()

# Função para ler o cartão RFID
def leitor_card(ser):
    while True:
        if ser.in_waiting:
            data = ser.readline().decode('utf-8').split()
            for i in range(3):
                data.pop(0)
            data = ''.join(data)
            return data
        
# Função para exibir uma pergunta na tela
def display_question_fase1(screen, font, WIDTH, HEIGHT, question_data, background_color, player):
    screen.fill(background_color)
    question_text = font.render(question_data["question"], True, (0,0,0))
    question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(question_text, question_rect)
    player_name = font.render(f"{player}", True, (255, 255, 255))
    player_rect = player_name.get_rect(topleft=(10,10))
    screen.blit(player_name, player_rect)
    pygame.display.update()

# Função para exibir uma pergunta na tela
def display_question(screen, font, WIDTH, HEIGHT, question_data, background_color, player):
    screen.fill(background_color)
    question_text = font.render(question_data["question"], True, background_color)
    question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(question_text, question_rect)
    player_name = font.render(f"{player}", True, (255, 255, 255))
    player_rect = player_name.get_rect(topleft=(10,10))
    screen.blit(player_name, player_rect)
    pygame.display.update()

# Função para exibir uma pergunta na tela da fase 3
def display_question_fase3(screen, font, WIDTH, HEIGHT, question_data, background_color, player, text_color):
    screen.fill(background_color)
    question_text = font.render(question_data["question"], True, text_color)
    question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(question_text, question_rect)
    player_name = font.render(f"{player}", True, (255, 255, 255))
    player_rect = player_name.get_rect(topleft=(10,10))
    screen.blit(player_name, player_rect)
    pygame.display.update()

# Função para exibir o início do jogo
def display_current_fase(screen, font, WIDTH, HEIGHT, fase):
    screen.fill((255, 255, 255))
    start_text = font.render(f'Início {fase}', True, (0, 0, 0))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(start_text, start_rect)
    
    pygame.display.update()
    # Tempo para passar para o início verdadeiro do jogo - 2 segundos
    pygame.time.delay(2000)

# Função para exibir a vez do jogador
def display_player_turn(screen, font, WIDTH, HEIGHT, player_name, background_color):
    screen.fill(background_color)

    turn_text = font.render(f"Vez do jogador {player_name}", True, (0, 0, 0))
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)

    pygame.display.update()
    pygame.time.delay(2000)

# Função para exibir que o jogador acertou
def correct_answer(screen, font_rodada, WIDTH, HEIGHT):
        screen.fill((0, 156, 59))
        turn_text = font_rodada.render(f"VOCÊ ACERTOU!", True, (0, 0, 0))
        turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(turn_text, turn_rect)
        pygame.display.update()
        # lembrar de aumentar esse tempo abaixo
        pygame.time.delay(500)

# Função para exibir que o jogador errou
def wrong_answer(screen, font_rodada, WIDTH, HEIGHT):
    screen.fill((229, 36, 34) )
    turn_text = font_rodada.render(f"VOCÊ ERROU!", True, (0, 0, 0))
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)
    # answer = font_rodada.render(f"Resposta correta: {question_data['answer']}", True, (0, 0, 0))
    # answer_rect = answer.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    # answer_rect = answer.get_rect(topleft=(10,10))
    # screen.blit(answer, answer_rect)
    pygame.display.update()
    # lembrar de aumentar esse tempo abaixo
    pygame.time.delay(500)