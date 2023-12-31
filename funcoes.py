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
def get_num_alunos(screen, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GRAY, font, fonte_botoes):
    screen.fill(WHITE)


    message_text1 = font.render("Olá Professor(a), insira o nome de cada aluno e clique em Inserir.", True, BLACK)
    message_text2 = font.render("Quando terminar, clique em Concluir.", True, BLACK)
    message_rect1 = message_text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 240))
    message_rect2 = message_text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(message_text1, message_rect1)
    screen.blit(message_text2, message_rect2)

    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 150, 200, 50)
    color_inactive = WHITE
    color_active = LIGHT_GRAY
    color = color_inactive
    aluno_text = ''
    active = False

    insert_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 90, 110, 50)
    insert_color_inactive = pygame.Color('lightblue')
    insert_color = insert_color_inactive

    conclude_button = pygame.Rect(WIDTH - 150, HEIGHT - 70, 140, 50)
    conclude_color_inactive = pygame.Color('lightgreen')
    conclude_color = conclude_color_inactive

    num_alunos = 0
    nomes_alunos = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = color_active if active else color_inactive
                elif insert_button.collidepoint(event.pos):
                    if aluno_text:
                        nomes_alunos.append(aluno_text)
                        aluno_text = ''
                        num_alunos += 1
                elif conclude_button.collidepoint(event.pos):
                    if num_alunos > 0:
                        return num_alunos, nomes_alunos

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if aluno_text:
                            nomes_alunos.append(aluno_text)
                            aluno_text = ''
                            num_alunos += 1
                    elif event.key == pygame.K_BACKSPACE:
                        aluno_text = aluno_text[:-1]
                    else:
                        aluno_text += event.unicode

        txt_surface = fonte_botoes.render(aluno_text, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        pygame.draw.rect(screen, color, input_box, border_radius=15)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.draw.rect(screen, insert_color, insert_button, border_radius=10)
        insert_text = fonte_botoes.render("Inserir", True, BLACK)
        insert_rect = insert_text.get_rect(center=insert_button.center)
        screen.blit(insert_text, insert_rect)

        pygame.draw.rect(screen, conclude_color, conclude_button, border_radius=10)
        conclude_text = fonte_botoes.render("Concluir", True, BLACK)
        conclude_rect = conclude_text.get_rect(center=conclude_button.center)
        screen.blit(conclude_text, conclude_rect)

        # Exibe os nomes já adicionados em colunas
        display_names(screen, nomes_alunos, font, WIDTH // 4, HEIGHT // 2 + 40)

        pygame.display.flip()

# Função para exibir os nomes dos alunos em colunas
def display_names(screen, nomes_alunos, font, x, y):
    max_display = 10
    for i, nome_index in enumerate(range(len(nomes_alunos))):
        coluna = i // max_display  # Calcula a coluna atual
        nome = nomes_alunos[nome_index]
        nome_text = font.render(nome, True, (0, 0, 0))
        nome_rect = nome_text.get_rect(topleft=(x + coluna * 200, y + i % max_display * 30))
        screen.blit(nome_text, nome_rect)

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
def display_question_fase4(screen, font, WIDTH, HEIGHT, question_data, background_color, player, text_color, font_144):
    screen.fill(background_color)
    question_text = font_144.render(question_data["question"], True, text_color)
    question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
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
def correct_answer(screen, font_72, WIDTH, HEIGHT):
        screen.fill((0, 156, 59))
        turn_text = font_72.render(f"VOCÊ ACERTOU!", True, (0, 0, 0))
        turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(turn_text, turn_rect)
        pygame.display.update()
        # lembrar de aumentar esse tempo abaixo
        pygame.time.delay(3000)

# Função para exibir que o jogador errou
def wrong_answer(screen, font_72, WIDTH, HEIGHT, answer, font):
    screen.fill((229, 36, 34) )
    turn_text = font_72.render(f"VOCÊ ERROU!", True, (0, 0, 0))
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)
    answer = font.render(f"Resposta correta: {answer}", True, (0, 0, 0))
    answer_rect = answer.get_rect(topleft=(10,10))
    screen.blit(answer, answer_rect)
    pygame.display.update()
    # lembrar de aumentar esse tempo abaixo
    pygame.time.delay(3000)

# Função para exibir que o jogador errou sem mostrar a resposta
def wrong_answer_fase4(screen, font_72, WIDTH, HEIGHT):
    screen.fill((229, 36, 34) )
    turn_text = font_72.render(f"VOCÊ ERROU!", True, (0, 0, 0))
    turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(turn_text, turn_rect)
    pygame.display.update()
    # lembrar de aumentar esse tempo abaixo
    pygame.time.delay(3000)

# Função para exibir a fase das fotos
def display_question_fase_photos(screen, font, player, image):
    screen.fill((255, 255, 255))
    screen.blit(image, (400, 130))
    player_name = font.render(f"{player}", True, (0, 0, 0))
    player_rect = player_name.get_rect(topleft=(10,10))
    screen.blit(player_name, player_rect)
    pygame.display.update()