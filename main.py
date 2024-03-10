import pygame
import pygame_menu
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('192.168.1.247', 8080))

word = 'собака'

def get_indices(lst, el, display_word):
    ind = [i for i in range(len(lst)) if lst[i] == el]
    for i in ind:
        display_word[i] = el
    return display_word


def Molodec(background, width, height, word, display_word):
    font = pygame.font.SysFont('Verdana', 40)
    if display_word == list(word):
        text = font.render('Молодец', True, 'black')
        background.blit(text, (width // 2 - text.get_width() // 2, height * 0.3 - text.get_height() // 2))


def vis_draw(er_cnt, background, width, height, word, display_word):
    font = pygame.font.SysFont('Verdana', 40)
    if er_cnt == 0:
        pygame.draw.line(background, 'black', [width * 0.8, height * 0.35], [width * 0.8, height * 0.1], 3)
    elif er_cnt == 1:
        pygame.draw.line(background, 'black', [width * 0.815, height * 0.35], [width * 0.76, height * 0.35], 3)
    elif er_cnt == 2:
        pygame.draw.line(background, 'black', [width * 0.8, height * 0.1], [width * 0.7, height * 0.1], 3)
    elif er_cnt == 3:
        pygame.draw.line(background, 'black', [width * 0.8, height * 0.15], [width * 0.75, height * 0.1], 3)
    elif er_cnt == 4:
        pygame.draw.line(background, 'black', [width * 0.71, height * 0.1], [width * 0.71, height * 0.13], 3)
    elif er_cnt == 5:
        pygame.draw.circle(background, 'black', (width * 0.71, height * 0.15), height * 0.02)
    elif er_cnt == 6:
        pygame.draw.ellipse(background, 'black', (width * 0.695, height * 0.17, width * 0.03, height * 0.08))
    elif er_cnt == 7:
        pygame.draw.line(background, 'black', [width * 0.71, height * 0.17], [width * 0.68, height * 0.20], 3)
    elif er_cnt == 8:
        pygame.draw.line(background, 'black', [width * 0.71, height * 0.17], [width * 0.74, height * 0.20], 3)
    elif er_cnt == 9:
        pygame.draw.line(background, 'black', [width * 0.71, height * 0.24], [width * 0.69, height * 0.29], 3)
    elif er_cnt == 10:
        pygame.draw.line(background, 'black', [width * 0.71, height * 0.24], [width * 0.73, height * 0.29], 3)
        display_word = list(word)
        text = font.render(' '.join(display_word), True, 'black')
        background.blit(text, (width // 2 - text.get_width() // 2, height * 0.3 - text.get_height() // 2))


def start_the_game():
    word = 'собака'
    try:
        data = sock.recv(1024)
        data = data.decode()
        word = data
    except:
        pass
    width, height = 1200, 800
    pygame.display.set_caption('Висельница игра')
    window_surface = pygame.display.set_mode((1200, 800))
    background = pygame.Surface((1200, 800))
    background.fill(pygame.Color('white'))

    fts = pygame.image.load('Hv_full_no_bg.png')
    ft = pygame.transform.scale(fts, (100, 100))
    ft_rect = ft.get_rect(center=(920, 180))
    background.blit(ft, ft_rect)


    buttonm_font = pygame.font.SysFont('Verdana', 20)
    buttonm_text_color = pygame.Color("black")
    buttonm_color = pygame.Color("gray")
    buttonm_rect = pygame.Rect(100, 100, 150, 100)
    buttonm_text = buttonm_font.render('В меню', True, buttonm_text_color)

    button1_font = pygame.font.SysFont('Verdana', 20)
    button1_text_color = pygame.Color("black")
    button1_color = pygame.Color("gray")
    button1_rect = pygame.Rect(200, 500, 40, 45)
    button1_text = button1_font.render('A', True, button1_text_color)

    button2_font = pygame.font.SysFont('Verdana', 20)
    button2_text_color = pygame.Color("black")
    button2_color = pygame.Color("gray")
    button2_rect = pygame.Rect(273, 500, 40, 45)
    button2_text = button2_font.render('Б', True, button2_text_color)

    button3_font = pygame.font.SysFont('Verdana', 20)
    button3_text_color = pygame.Color("black")
    button3_color = pygame.Color("gray")
    button3_rect = pygame.Rect(346, 500, 40, 45)
    button3_text = button3_font.render('В', True, button3_text_color)

    button4_font = pygame.font.SysFont('Verdana', 20)
    button4_text_color = pygame.Color("black")
    button4_color = pygame.Color("gray")
    button4_rect = pygame.Rect(419, 500, 40, 45)
    button4_text = button4_font.render('Г', True, button4_text_color)

    button5_font = pygame.font.SysFont('Verdana', 20)
    button5_text_color = pygame.Color("black")
    button5_color = pygame.Color("gray")
    button5_rect = pygame.Rect(492, 500, 40, 45)
    button5_text = button5_font.render('Д', True, button5_text_color)

    button6_font = pygame.font.SysFont('Verdana', 20)
    button6_text_color = pygame.Color("black")
    button6_color = pygame.Color("gray")
    button6_rect = pygame.Rect(565, 500, 40, 45)
    button6_text = button6_font.render('Е', True, button6_text_color)

    button7_font = pygame.font.SysFont('Verdana', 20)
    button7_text_color = pygame.Color("black")
    button7_color = pygame.Color("gray")
    button7_rect = pygame.Rect(638, 500, 40, 45)
    button7_text = button7_font.render('Ё', True, button7_text_color)

    button8_font = pygame.font.SysFont('Verdana', 20)
    button8_text_color = pygame.Color("black")
    button8_color = pygame.Color("gray")
    button8_rect = pygame.Rect(711, 500, 40, 45)
    button8_text = button8_font.render('Ж', True, button8_text_color)

    button9_font = pygame.font.SysFont('Verdana', 20)
    button9_text_color = pygame.Color("black")
    button9_color = pygame.Color("gray")
    button9_rect = pygame.Rect(784, 500, 40, 45)
    button9_text = button9_font.render('З', True, button9_text_color)

    button10_font = pygame.font.SysFont('Verdana', 20)
    button10_text_color = pygame.Color("black")
    button10_color = pygame.Color("gray")
    button10_rect = pygame.Rect(857, 500, 40, 45)
    button10_text = button10_font.render('И', True, button10_text_color)

    button11_font = pygame.font.SysFont('Verdana', 20)
    button11_text_color = pygame.Color("black")
    button11_color = pygame.Color("gray")
    button11_rect = pygame.Rect(930, 500, 40, 45)
    button11_text = button11_font.render('Й', True, button11_text_color)

    button12_font = pygame.font.SysFont('Verdana', 20)
    button12_text_color = pygame.Color("black")
    button12_color = pygame.Color("gray")
    button12_rect = pygame.Rect(200, 595, 40, 45)
    button12_text = button12_font.render('К', True, button12_text_color)

    button13_font = pygame.font.SysFont('Verdana', 20)
    button13_text_color = pygame.Color("black")
    button13_color = pygame.Color("gray")
    button13_rect = pygame.Rect(273, 595, 40, 45)
    button13_text = button13_font.render('Л', True, button13_text_color)

    button14_font = pygame.font.SysFont('Verdana', 20)
    button14_text_color = pygame.Color("black")
    button14_color = pygame.Color("gray")
    button14_rect = pygame.Rect(346, 595, 40, 45)
    button14_text = button14_font.render('М', True, button14_text_color)

    button15_font = pygame.font.SysFont('Verdana', 20)
    button15_text_color = pygame.Color("black")
    button15_color = pygame.Color("gray")
    button15_rect = pygame.Rect(419, 595, 40, 45)
    button15_text = button15_font.render('Н', True, button15_text_color)

    button16_font = pygame.font.SysFont('Verdana', 20)
    button16_text_color = pygame.Color("black")
    button16_color = pygame.Color("gray")
    button16_rect = pygame.Rect(492, 595, 40, 45)
    button16_text = button16_font.render('О', True, button16_text_color)

    button17_font = pygame.font.SysFont('Verdana', 20)
    button17_text_color = pygame.Color("black")
    button17_color = pygame.Color("gray")
    button17_rect = pygame.Rect(565, 595, 40, 45)
    button17_text = button17_font.render('П', True, button17_text_color)

    button18_font = pygame.font.SysFont('Verdana', 20)
    button18_text_color = pygame.Color("black")
    button18_color = pygame.Color("gray")
    button18_rect = pygame.Rect(638, 595, 40, 45)
    button18_text = button18_font.render('Р', True, button18_text_color)

    button19_font = pygame.font.SysFont('Verdana', 20)
    button19_text_color = pygame.Color("black")
    button19_color = pygame.Color("gray")
    button19_rect = pygame.Rect(711, 595, 40, 45)
    button19_text = button19_font.render('С', True, button19_text_color)

    button20_font = pygame.font.SysFont('Verdana', 20)
    button20_text_color = pygame.Color("black")
    button20_color = pygame.Color("gray")
    button20_rect = pygame.Rect(784, 595, 40, 45)
    button20_text = button20_font.render('Т', True, button20_text_color)

    button21_font = pygame.font.SysFont('Verdana', 20)
    button21_text_color = pygame.Color("black")
    button21_color = pygame.Color("gray")
    button21_rect = pygame.Rect(857, 595, 40, 45)
    button21_text = button21_font.render('У', True, button21_text_color)

    button22_font = pygame.font.SysFont('Verdana', 20)
    button22_text_color = pygame.Color("black")
    button22_color = pygame.Color("gray")
    button22_rect = pygame.Rect(930, 595, 40, 45)
    button22_text = button22_font.render('Ф', True, button22_text_color)

    button23_font = pygame.font.SysFont('Verdana', 20)
    button23_text_color = pygame.Color("black")
    button23_color = pygame.Color("gray")
    button23_rect = pygame.Rect(200, 680, 40, 45)
    button23_text = button23_font.render('Х', True, button23_text_color)

    button24_font = pygame.font.SysFont('Verdana', 20)
    button24_text_color = pygame.Color("black")
    button24_color = pygame.Color("gray")
    button24_rect = pygame.Rect(273, 680, 40, 45)
    button24_text = button24_font.render('Ц', True, button24_text_color)

    button25_font = pygame.font.SysFont('Verdana', 20)
    button25_text_color = pygame.Color("black")
    button25_color = pygame.Color("gray")
    button25_rect = pygame.Rect(346, 680, 40, 45)
    button25_text = button25_font.render('Ч', True, button25_text_color)

    button26_font = pygame.font.SysFont('Verdana', 20)
    button26_text_color = pygame.Color("black")
    button26_color = pygame.Color("gray")
    button26_rect = pygame.Rect(419, 680, 40, 45)
    button26_text = button26_font.render('Ш', True, button26_text_color)

    button27_font = pygame.font.SysFont('Verdana', 20)
    button27_text_color = pygame.Color("black")
    button27_color = pygame.Color("gray")
    button27_rect = pygame.Rect(492, 680, 40, 45)
    button27_text = button27_font.render('Щ', True, button27_text_color)

    button28_font = pygame.font.SysFont('Verdana', 20)
    button28_text_color = pygame.Color("black")
    button28_color = pygame.Color("gray")
    button28_rect = pygame.Rect(565, 680, 40, 45)
    button28_text = button28_font.render('Ъ', True, button28_text_color)

    button29_font = pygame.font.SysFont('Verdana', 20)
    button29_text_color = pygame.Color("black")
    button29_color = pygame.Color("gray")
    button29_rect = pygame.Rect(638, 680, 40, 45)
    button29_text = button29_font.render('Ы', True, button29_text_color)

    button30_font = pygame.font.SysFont('Verdana', 20)
    button30_text_color = pygame.Color("black")
    button30_color = pygame.Color("gray")
    button30_rect = pygame.Rect(711, 680, 40, 45)
    button30_text = button30_font.render('Ь', True, button30_text_color)

    button31_font = pygame.font.SysFont('Verdana', 20)
    button31_text_color = pygame.Color("black")
    button31_color = pygame.Color("gray")
    button31_rect = pygame.Rect(784, 680, 40, 45)
    button31_text = button31_font.render('Э', True, button31_text_color)

    button32_font = pygame.font.SysFont('Verdana', 20)
    button32_text_color = pygame.Color("black")
    button32_color = pygame.Color("gray")
    button32_rect = pygame.Rect(857, 680, 40, 45)
    button32_text = button32_font.render('Ю', True, button32_text_color)

    button33_font = pygame.font.SysFont('Verdana', 20)
    button33_text_color = pygame.Color("black")
    button33_color = pygame.Color("gray")
    button33_rect = pygame.Rect(930, 680, 40, 45)
    button33_text = button33_font.render('Я', True, button33_text_color)

    display_word = ['_' for _ in word]
    font = pygame.font.SysFont('Verdana', 40)
    text = font.render(' '.join(display_word), True, 'black')

    er_cnt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if buttonm_rect.collidepoint(event.pos):
                    menu.mainloop(men)
                elif button1_rect.collidepoint(event.pos):
                    if 'а' in word:
                        button1_color = pygame.Color("green")
                        display_word = get_indices(word, 'а', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button1_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button2_rect.collidepoint(event.pos):
                    if 'б' in word:
                        button2_color = pygame.Color("green")
                        display_word = get_indices(word, 'б', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button2_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button3_rect.collidepoint(event.pos):
                    if 'в' in word:
                        button3_color = pygame.Color("green")
                        display_word = get_indices(word, 'в', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button3_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button4_rect.collidepoint(event.pos):
                    if 'г' in word:
                        button4_color = pygame.Color("green")
                        display_word = get_indices(word, 'г', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button4_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button5_rect.collidepoint(event.pos):
                    if 'д' in word:
                        button5_color = pygame.Color("green")
                        display_word = get_indices(word, 'д', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button5_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button6_rect.collidepoint(event.pos):
                    if 'е' in word:
                        button6_color = pygame.Color("green")
                        display_word = get_indices(word, 'е', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button6_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button7_rect.collidepoint(event.pos):
                    if 'ё' in word:
                        button7_color = pygame.Color("green")
                        display_word = get_indices(word, 'ё', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button7_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button8_rect.collidepoint(event.pos):
                    if 'ж' in word:
                        button8_color = pygame.Color("green")
                        display_word = get_indices(word, 'ж', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button8_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button9_rect.collidepoint(event.pos):
                    if 'з' in word:
                        button9_color = pygame.Color("green")
                        display_word = get_indices(word, 'з', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button9_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button10_rect.collidepoint(event.pos):
                    if 'и' in word:
                        button10_color = pygame.Color("green")
                        display_word = get_indices(word, 'и', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button10_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button11_rect.collidepoint(event.pos):
                    if 'й' in word:
                        button11_color = pygame.Color("green")
                        display_word = get_indices(word, 'й', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button11_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button12_rect.collidepoint(event.pos):
                    if 'к' in word:
                        button12_color = pygame.Color("green")
                        display_word = get_indices(word, 'к', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button12_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button13_rect.collidepoint(event.pos):
                    if 'л' in word:
                        button13_color = pygame.Color("green")
                        display_word = get_indices(word, 'л', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button13_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button14_rect.collidepoint(event.pos):
                    if 'м' in word:
                        button14_color = pygame.Color("green")
                        display_word = get_indices(word, 'м', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button14_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button15_rect.collidepoint(event.pos):
                    if 'н' in word:
                        button15_color = pygame.Color("green")
                        display_word = get_indices(word, 'н', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button15_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button16_rect.collidepoint(event.pos):
                    if 'о' in word:
                        button16_color = pygame.Color("green")
                        display_word = get_indices(word, 'о', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button16_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button17_rect.collidepoint(event.pos):
                    if 'п' in word:
                        button17_color = pygame.Color("green")
                        display_word = get_indices(word, 'п', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button17_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button18_rect.collidepoint(event.pos):
                    if 'р' in word:
                        button18_color = pygame.Color("green")
                        display_word = get_indices(word, 'р', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button18_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button19_rect.collidepoint(event.pos):
                    if 'с' in word:
                        button19_color = pygame.Color("green")
                        display_word = get_indices(word, 'с', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button19_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button20_rect.collidepoint(event.pos):
                    if 'т' in word:
                        button20_color = pygame.Color("green")
                        display_word = get_indices(word, 'т', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button20_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button21_rect.collidepoint(event.pos):
                    if 'у' in word:
                        button21_color = pygame.Color("green")
                        display_word = get_indices(word, 'у', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button21_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button22_rect.collidepoint(event.pos):
                    if 'ф' in word:
                        button22_color = pygame.Color("green")
                        display_word = get_indices(word, 'ф', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button22_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button23_rect.collidepoint(event.pos):
                    if 'х' in word:
                        button23_color = pygame.Color("green")
                        display_word = get_indices(word, 'х', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button23_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button24_rect.collidepoint(event.pos):
                    if 'ц' in word:
                        button24_color = pygame.Color("green")
                        display_word = get_indices(word, 'ц', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button24_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button25_rect.collidepoint(event.pos):
                    if 'ч' in word:
                        button25_color = pygame.Color("green")
                        display_word = get_indices(word, 'ч', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button25_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button26_rect.collidepoint(event.pos):
                    if 'ш' in word:
                        button26_color = pygame.Color("green")
                        display_word = get_indices(word, 'ш', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button26_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button27_rect.collidepoint(event.pos):
                    if 'щ' in word:
                        button27_color = pygame.Color("green")
                        display_word = get_indices(word, 'щ', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button27_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button28_rect.collidepoint(event.pos):
                    if 'ъ' in word:
                        button28_color = pygame.Color("green")
                        display_word = get_indices(word, 'ъ', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button28_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button29_rect.collidepoint(event.pos):
                    if 'ы' in word:
                        button29_color = pygame.Color("green")
                        display_word = get_indices(word, 'ы', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button29_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button30_rect.collidepoint(event.pos):
                    if 'ь' in word:
                        button30_color = pygame.Color("green")
                        display_word = get_indices(word, 'ь', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button30_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button31_rect.collidepoint(event.pos):
                    if 'э' in word:
                        button31_color = pygame.Color("green")
                        display_word = get_indices(word, 'э', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button31_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button32_rect.collidepoint(event.pos):
                    if 'ю' in word:
                        button32_color = pygame.Color("green")
                        display_word = get_indices(word, 'ю', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button32_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1
                elif button33_rect.collidepoint(event.pos):
                    if 'я' in word:
                        button33_color = pygame.Color("green")
                        display_word = get_indices(word, 'я', display_word)
                        text = font.render(' '.join(display_word), True, 'black')
                        Molodec(background, width, height, word, display_word)
                    else:
                        button33_color = pygame.Color("red")
                        vis_draw(er_cnt, background, width, height, word, display_word)
                        er_cnt += 1

            window_surface.blit(background, (0, 0))

            pygame.draw.rect(background, buttonm_color, buttonm_rect)
            buttonm_rect_center = buttonm_text.get_rect(center=buttonm_rect.center)
            background.blit(buttonm_text, buttonm_rect_center)

            pygame.draw.rect(window_surface, button1_color, button1_rect)
            button1_rect_center = button1_text.get_rect(center=button1_rect.center)
            window_surface.blit(button1_text, button1_rect_center)

            pygame.draw.rect(window_surface, button2_color, button2_rect)
            button2_rect_center = button2_text.get_rect(center=button2_rect.center)
            window_surface.blit(button2_text, button2_rect_center)

            pygame.draw.rect(window_surface, button3_color, button3_rect)
            button3_rect_center = button3_text.get_rect(center=button3_rect.center)
            window_surface.blit(button3_text, button3_rect_center)

            pygame.draw.rect(window_surface, button4_color, button4_rect)
            button4_rect_center = button4_text.get_rect(center=button4_rect.center)
            window_surface.blit(button4_text, button4_rect_center)

            pygame.draw.rect(window_surface, button5_color, button5_rect)
            button5_rect_center = button5_text.get_rect(center=button5_rect.center)
            window_surface.blit(button5_text, button5_rect_center)

            pygame.draw.rect(window_surface, button6_color, button6_rect)
            button6_rect_center = button6_text.get_rect(center=button6_rect.center)
            window_surface.blit(button6_text, button6_rect_center)

            pygame.draw.rect(window_surface, button7_color, button7_rect)
            button7_rect_center = button7_text.get_rect(center=button7_rect.center)
            window_surface.blit(button7_text, button7_rect_center)

            pygame.draw.rect(window_surface, button8_color, button8_rect)
            button8_rect_center = button8_text.get_rect(center=button8_rect.center)
            window_surface.blit(button8_text, button8_rect_center)

            pygame.draw.rect(window_surface, button9_color, button9_rect)
            button9_rect_center = button9_text.get_rect(center=button9_rect.center)
            window_surface.blit(button9_text, button9_rect_center)

            pygame.draw.rect(window_surface, button10_color, button10_rect)
            button10_rect_center = button10_text.get_rect(center=button10_rect.center)
            window_surface.blit(button10_text, button10_rect_center)

            pygame.draw.rect(window_surface, button11_color, button11_rect)
            button11_rect_center = button11_text.get_rect(center=button11_rect.center)
            window_surface.blit(button11_text, button11_rect_center)

            pygame.draw.rect(window_surface, button12_color, button12_rect)
            button12_rect_center = button12_text.get_rect(center=button12_rect.center)
            window_surface.blit(button12_text, button12_rect_center)

            pygame.draw.rect(window_surface, button13_color, button13_rect)
            button13_rect_center = button13_text.get_rect(center=button13_rect.center)
            window_surface.blit(button13_text, button13_rect_center)

            pygame.draw.rect(window_surface, button14_color, button14_rect)
            button14_rect_center = button14_text.get_rect(center=button14_rect.center)
            window_surface.blit(button14_text, button14_rect_center)

            pygame.draw.rect(window_surface, button15_color, button15_rect)
            button15_rect_center = button15_text.get_rect(center=button15_rect.center)
            window_surface.blit(button15_text, button15_rect_center)

            pygame.draw.rect(window_surface, button16_color, button16_rect)
            button16_rect_center = button16_text.get_rect(center=button16_rect.center)
            window_surface.blit(button16_text, button16_rect_center)

            pygame.draw.rect(window_surface, button17_color, button17_rect)
            button17_rect_center = button17_text.get_rect(center=button17_rect.center)
            window_surface.blit(button17_text, button17_rect_center)

            pygame.draw.rect(window_surface, button18_color, button18_rect)
            button18_rect_center = button18_text.get_rect(center=button18_rect.center)
            window_surface.blit(button18_text, button18_rect_center)

            pygame.draw.rect(window_surface, button19_color, button19_rect)
            button19_rect_center = button19_text.get_rect(center=button19_rect.center)
            window_surface.blit(button19_text, button19_rect_center)

            pygame.draw.rect(window_surface, button20_color, button20_rect)
            button20_rect_center = button20_text.get_rect(center=button20_rect.center)
            window_surface.blit(button20_text, button20_rect_center)

            pygame.draw.rect(window_surface, button21_color, button21_rect)
            button21_rect_center = button21_text.get_rect(center=button21_rect.center)
            window_surface.blit(button21_text, button21_rect_center)

            pygame.draw.rect(window_surface, button22_color, button22_rect)
            button22_rect_center = button22_text.get_rect(center=button22_rect.center)
            window_surface.blit(button22_text, button22_rect_center)

            pygame.draw.rect(window_surface, button23_color, button23_rect)
            button23_rect_center = button23_text.get_rect(center=button23_rect.center)
            window_surface.blit(button23_text, button23_rect_center)

            pygame.draw.rect(window_surface, button24_color, button24_rect)
            button24_rect_center = button24_text.get_rect(center=button24_rect.center)
            window_surface.blit(button24_text, button24_rect_center)

            pygame.draw.rect(window_surface, button25_color, button25_rect)
            button25_rect_center = button25_text.get_rect(center=button25_rect.center)
            window_surface.blit(button25_text, button25_rect_center)

            pygame.draw.rect(window_surface, button26_color, button26_rect)
            button26_rect_center = button26_text.get_rect(center=button26_rect.center)
            window_surface.blit(button26_text, button26_rect_center)

            pygame.draw.rect(window_surface, button27_color, button27_rect)
            button27_rect_center = button27_text.get_rect(center=button27_rect.center)
            window_surface.blit(button27_text, button27_rect_center)

            pygame.draw.rect(window_surface, button28_color, button28_rect)
            button28_rect_center = button28_text.get_rect(center=button28_rect.center)
            window_surface.blit(button28_text, button28_rect_center)

            pygame.draw.rect(window_surface, button29_color, button29_rect)
            button29_rect_center = button29_text.get_rect(center=button29_rect.center)
            window_surface.blit(button29_text, button29_rect_center)

            pygame.draw.rect(window_surface, button30_color, button30_rect)
            button30_rect_center = button30_text.get_rect(center=button30_rect.center)
            window_surface.blit(button30_text, button30_rect_center)

            pygame.draw.rect(window_surface, button31_color, button31_rect)
            button31_rect_center = button31_text.get_rect(center=button31_rect.center)
            window_surface.blit(button31_text, button31_rect_center)

            pygame.draw.rect(window_surface, button32_color, button32_rect)
            button32_rect_center = button32_text.get_rect(center=button32_rect.center)
            window_surface.blit(button32_text, button32_rect_center)

            pygame.draw.rect(window_surface, button33_color, button33_rect)
            button33_rect_center = button33_text.get_rect(center=button33_rect.center)
            window_surface.blit(button33_text, button33_rect_center)

            background.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

            pygame.display.update()


def sec():
    width, height = 1200, 800
    pygame.display.set_caption('Висельница игра')
    window_surface = pygame.display.set_mode((1200, 800))
    background = pygame.Surface((1200, 800))
    background.fill(pygame.Color('white'))

    fts = pygame.image.load('Hv_full_no_bg.png')
    ft = pygame.transform.scale(fts, (100, 100))
    ft_rect = ft.get_rect(center=(920, 180))
    background.blit(ft, ft_rect)

    buttonm_font = pygame.font.SysFont('Verdana', 20)
    buttonm_text_color = pygame.Color("black")
    buttonm_color = pygame.Color("gray")
    buttonm_rect = pygame.Rect(100, 100, 150, 100)
    buttonm_text = buttonm_font.render('В меню', True, buttonm_text_color)

    buttone_font = pygame.font.SysFont('Verdana', 20)
    buttone_text_color = pygame.Color("black")
    buttone_color = pygame.Color("gray")
    buttone_rect = pygame.Rect(1000, 680, 150, 100)
    buttone_text = buttone_font.render('Ввести', True, buttone_text_color)

    button1_font = pygame.font.SysFont('Verdana', 20)
    button1_text_color = pygame.Color("black")
    button1_color = pygame.Color("gray")
    button1_rect = pygame.Rect(200, 500, 40, 45)
    button1_text = button1_font.render('A', True, button1_text_color)

    button2_font = pygame.font.SysFont('Verdana', 20)
    button2_text_color = pygame.Color("black")
    button2_color = pygame.Color("gray")
    button2_rect = pygame.Rect(273, 500, 40, 45)
    button2_text = button2_font.render('Б', True, button2_text_color)

    button3_font = pygame.font.SysFont('Verdana', 20)
    button3_text_color = pygame.Color("black")
    button3_color = pygame.Color("gray")
    button3_rect = pygame.Rect(346, 500, 40, 45)
    button3_text = button3_font.render('В', True, button3_text_color)

    button4_font = pygame.font.SysFont('Verdana', 20)
    button4_text_color = pygame.Color("black")
    button4_color = pygame.Color("gray")
    button4_rect = pygame.Rect(419, 500, 40, 45)
    button4_text = button4_font.render('Г', True, button4_text_color)

    button5_font = pygame.font.SysFont('Verdana', 20)
    button5_text_color = pygame.Color("black")
    button5_color = pygame.Color("gray")
    button5_rect = pygame.Rect(492, 500, 40, 45)
    button5_text = button5_font.render('Д', True, button5_text_color)

    button6_font = pygame.font.SysFont('Verdana', 20)
    button6_text_color = pygame.Color("black")
    button6_color = pygame.Color("gray")
    button6_rect = pygame.Rect(565, 500, 40, 45)
    button6_text = button6_font.render('Е', True, button6_text_color)

    button7_font = pygame.font.SysFont('Verdana', 20)
    button7_text_color = pygame.Color("black")
    button7_color = pygame.Color("gray")
    button7_rect = pygame.Rect(638, 500, 40, 45)
    button7_text = button7_font.render('Ё', True, button7_text_color)

    button8_font = pygame.font.SysFont('Verdana', 20)
    button8_text_color = pygame.Color("black")
    button8_color = pygame.Color("gray")
    button8_rect = pygame.Rect(711, 500, 40, 45)
    button8_text = button8_font.render('Ж', True, button8_text_color)

    button9_font = pygame.font.SysFont('Verdana', 20)
    button9_text_color = pygame.Color("black")
    button9_color = pygame.Color("gray")
    button9_rect = pygame.Rect(784, 500, 40, 45)
    button9_text = button9_font.render('З', True, button9_text_color)

    button10_font = pygame.font.SysFont('Verdana', 20)
    button10_text_color = pygame.Color("black")
    button10_color = pygame.Color("gray")
    button10_rect = pygame.Rect(857, 500, 40, 45)
    button10_text = button10_font.render('И', True, button10_text_color)

    button11_font = pygame.font.SysFont('Verdana', 20)
    button11_text_color = pygame.Color("black")
    button11_color = pygame.Color("gray")
    button11_rect = pygame.Rect(930, 500, 40, 45)
    button11_text = button11_font.render('Й', True, button11_text_color)

    button12_font = pygame.font.SysFont('Verdana', 20)
    button12_text_color = pygame.Color("black")
    button12_color = pygame.Color("gray")
    button12_rect = pygame.Rect(200, 595, 40, 45)
    button12_text = button12_font.render('К', True, button12_text_color)

    button13_font = pygame.font.SysFont('Verdana', 20)
    button13_text_color = pygame.Color("black")
    button13_color = pygame.Color("gray")
    button13_rect = pygame.Rect(273, 595, 40, 45)
    button13_text = button13_font.render('Л', True, button13_text_color)

    button14_font = pygame.font.SysFont('Verdana', 20)
    button14_text_color = pygame.Color("black")
    button14_color = pygame.Color("gray")
    button14_rect = pygame.Rect(346, 595, 40, 45)
    button14_text = button14_font.render('М', True, button14_text_color)

    button15_font = pygame.font.SysFont('Verdana', 20)
    button15_text_color = pygame.Color("black")
    button15_color = pygame.Color("gray")
    button15_rect = pygame.Rect(419, 595, 40, 45)
    button15_text = button15_font.render('Н', True, button15_text_color)

    button16_font = pygame.font.SysFont('Verdana', 20)
    button16_text_color = pygame.Color("black")
    button16_color = pygame.Color("gray")
    button16_rect = pygame.Rect(492, 595, 40, 45)
    button16_text = button16_font.render('О', True, button16_text_color)

    button17_font = pygame.font.SysFont('Verdana', 20)
    button17_text_color = pygame.Color("black")
    button17_color = pygame.Color("gray")
    button17_rect = pygame.Rect(565, 595, 40, 45)
    button17_text = button17_font.render('П', True, button17_text_color)

    button18_font = pygame.font.SysFont('Verdana', 20)
    button18_text_color = pygame.Color("black")
    button18_color = pygame.Color("gray")
    button18_rect = pygame.Rect(638, 595, 40, 45)
    button18_text = button18_font.render('Р', True, button18_text_color)

    button19_font = pygame.font.SysFont('Verdana', 20)
    button19_text_color = pygame.Color("black")
    button19_color = pygame.Color("gray")
    button19_rect = pygame.Rect(711, 595, 40, 45)
    button19_text = button19_font.render('С', True, button19_text_color)

    button20_font = pygame.font.SysFont('Verdana', 20)
    button20_text_color = pygame.Color("black")
    button20_color = pygame.Color("gray")
    button20_rect = pygame.Rect(784, 595, 40, 45)
    button20_text = button20_font.render('Т', True, button20_text_color)

    button21_font = pygame.font.SysFont('Verdana', 20)
    button21_text_color = pygame.Color("black")
    button21_color = pygame.Color("gray")
    button21_rect = pygame.Rect(857, 595, 40, 45)
    button21_text = button21_font.render('У', True, button21_text_color)

    button22_font = pygame.font.SysFont('Verdana', 20)
    button22_text_color = pygame.Color("black")
    button22_color = pygame.Color("gray")
    button22_rect = pygame.Rect(930, 595, 40, 45)
    button22_text = button22_font.render('Ф', True, button22_text_color)

    button23_font = pygame.font.SysFont('Verdana', 20)
    button23_text_color = pygame.Color("black")
    button23_color = pygame.Color("gray")
    button23_rect = pygame.Rect(200, 680, 40, 45)
    button23_text = button23_font.render('Х', True, button23_text_color)

    button24_font = pygame.font.SysFont('Verdana', 20)
    button24_text_color = pygame.Color("black")
    button24_color = pygame.Color("gray")
    button24_rect = pygame.Rect(273, 680, 40, 45)
    button24_text = button24_font.render('Ц', True, button24_text_color)

    button25_font = pygame.font.SysFont('Verdana', 20)
    button25_text_color = pygame.Color("black")
    button25_color = pygame.Color("gray")
    button25_rect = pygame.Rect(346, 680, 40, 45)
    button25_text = button25_font.render('Ч', True, button25_text_color)

    button26_font = pygame.font.SysFont('Verdana', 20)
    button26_text_color = pygame.Color("black")
    button26_color = pygame.Color("gray")
    button26_rect = pygame.Rect(419, 680, 40, 45)
    button26_text = button26_font.render('Ш', True, button26_text_color)

    button27_font = pygame.font.SysFont('Verdana', 20)
    button27_text_color = pygame.Color("black")
    button27_color = pygame.Color("gray")
    button27_rect = pygame.Rect(492, 680, 40, 45)
    button27_text = button27_font.render('Щ', True, button27_text_color)

    button28_font = pygame.font.SysFont('Verdana', 20)
    button28_text_color = pygame.Color("black")
    button28_color = pygame.Color("gray")
    button28_rect = pygame.Rect(565, 680, 40, 45)
    button28_text = button28_font.render('Ъ', True, button28_text_color)

    button29_font = pygame.font.SysFont('Verdana', 20)
    button29_text_color = pygame.Color("black")
    button29_color = pygame.Color("gray")
    button29_rect = pygame.Rect(638, 680, 40, 45)
    button29_text = button29_font.render('Ы', True, button29_text_color)

    button30_font = pygame.font.SysFont('Verdana', 20)
    button30_text_color = pygame.Color("black")
    button30_color = pygame.Color("gray")
    button30_rect = pygame.Rect(711, 680, 40, 45)
    button30_text = button30_font.render('Ь', True, button30_text_color)

    button31_font = pygame.font.SysFont('Verdana', 20)
    button31_text_color = pygame.Color("black")
    button31_color = pygame.Color("gray")
    button31_rect = pygame.Rect(784, 680, 40, 45)
    button31_text = button31_font.render('Э', True, button31_text_color)

    button32_font = pygame.font.SysFont('Verdana', 20)
    button32_text_color = pygame.Color("black")
    button32_color = pygame.Color("gray")
    button32_rect = pygame.Rect(857, 680, 40, 45)
    button32_text = button32_font.render('Ю', True, button32_text_color)

    button33_font = pygame.font.SysFont('Verdana', 20)
    button33_text_color = pygame.Color("black")
    button33_color = pygame.Color("gray")
    button33_rect = pygame.Rect(930, 680, 40, 45)
    button33_text = button33_font.render('Я', True, button33_text_color)

    display_word = []
    font = pygame.font.SysFont('Verdana', 40)
    text = font.render(' '.join(display_word), True, 'black')

    global word

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if buttonm_rect.collidepoint(event.pos):
                    menu.mainloop(men)
                elif buttone_rect.collidepoint(event.pos):
                    word = ''.join(display_word)
                    sock.send(word.encode())
                elif button1_rect.collidepoint(event.pos):
                    display_word += 'а'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button2_rect.collidepoint(event.pos):
                    display_word += 'б'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button3_rect.collidepoint(event.pos):
                    display_word += 'в'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button4_rect.collidepoint(event.pos):
                    display_word += 'г'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button5_rect.collidepoint(event.pos):
                    display_word += 'д'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button6_rect.collidepoint(event.pos):
                    display_word += 'е'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button7_rect.collidepoint(event.pos):
                    display_word += 'ё'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button8_rect.collidepoint(event.pos):
                    display_word += 'ж'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button9_rect.collidepoint(event.pos):
                    display_word += 'з'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button10_rect.collidepoint(event.pos):
                    display_word += 'и'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button11_rect.collidepoint(event.pos):
                    display_word += 'й'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button12_rect.collidepoint(event.pos):
                    display_word += 'к'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button13_rect.collidepoint(event.pos):
                    display_word += 'л'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button14_rect.collidepoint(event.pos):
                    display_word += 'м'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button15_rect.collidepoint(event.pos):
                    display_word += 'н'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button16_rect.collidepoint(event.pos):
                    display_word += 'о'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button17_rect.collidepoint(event.pos):
                    display_word += 'п'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button18_rect.collidepoint(event.pos):
                    display_word += 'р'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button19_rect.collidepoint(event.pos):
                    display_word += 'с'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button20_rect.collidepoint(event.pos):
                    display_word += 'т'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button21_rect.collidepoint(event.pos):
                    display_word += 'у'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button22_rect.collidepoint(event.pos):
                    display_word += 'ф'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button23_rect.collidepoint(event.pos):
                    display_word += 'х'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button24_rect.collidepoint(event.pos):
                    display_word += 'ц'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button25_rect.collidepoint(event.pos):
                    display_word += 'ч'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button26_rect.collidepoint(event.pos):
                    display_word += 'ш'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button27_rect.collidepoint(event.pos):
                    display_word += 'щ'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button28_rect.collidepoint(event.pos):
                    display_word += 'ъ'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button29_rect.collidepoint(event.pos):
                    display_word += 'ы'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button30_rect.collidepoint(event.pos):
                    display_word += 'ь'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button31_rect.collidepoint(event.pos):
                    display_word += 'э'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button32_rect.collidepoint(event.pos):
                    display_word += 'ю'
                    text = font.render(' '.join(display_word), True, 'black')
                elif button33_rect.collidepoint(event.pos):
                    display_word += 'я'
                    text = font.render(' '.join(display_word), True, 'black')

            window_surface.blit(background, (0, 0))

            pygame.draw.rect(background, buttonm_color, buttonm_rect)
            buttonm_rect_center = buttonm_text.get_rect(center=buttonm_rect.center)
            background.blit(buttonm_text, buttonm_rect_center)

            pygame.draw.rect(background, buttone_color, buttone_rect)
            buttone_rect_center = buttone_text.get_rect(center=buttone_rect.center)
            background.blit(buttone_text, buttone_rect_center)

            pygame.draw.rect(window_surface, button1_color, button1_rect)
            button1_rect_center = button1_text.get_rect(center=button1_rect.center)
            window_surface.blit(button1_text, button1_rect_center)

            pygame.draw.rect(window_surface, button2_color, button2_rect)
            button2_rect_center = button2_text.get_rect(center=button2_rect.center)
            window_surface.blit(button2_text, button2_rect_center)

            pygame.draw.rect(window_surface, button3_color, button3_rect)
            button3_rect_center = button3_text.get_rect(center=button3_rect.center)
            window_surface.blit(button3_text, button3_rect_center)

            pygame.draw.rect(window_surface, button4_color, button4_rect)
            button4_rect_center = button4_text.get_rect(center=button4_rect.center)
            window_surface.blit(button4_text, button4_rect_center)

            pygame.draw.rect(window_surface, button5_color, button5_rect)
            button5_rect_center = button5_text.get_rect(center=button5_rect.center)
            window_surface.blit(button5_text, button5_rect_center)

            pygame.draw.rect(window_surface, button6_color, button6_rect)
            button6_rect_center = button6_text.get_rect(center=button6_rect.center)
            window_surface.blit(button6_text, button6_rect_center)

            pygame.draw.rect(window_surface, button7_color, button7_rect)
            button7_rect_center = button7_text.get_rect(center=button7_rect.center)
            window_surface.blit(button7_text, button7_rect_center)

            pygame.draw.rect(window_surface, button8_color, button8_rect)
            button8_rect_center = button8_text.get_rect(center=button8_rect.center)
            window_surface.blit(button8_text, button8_rect_center)

            pygame.draw.rect(window_surface, button9_color, button9_rect)
            button9_rect_center = button9_text.get_rect(center=button9_rect.center)
            window_surface.blit(button9_text, button9_rect_center)

            pygame.draw.rect(window_surface, button10_color, button10_rect)
            button10_rect_center = button10_text.get_rect(center=button10_rect.center)
            window_surface.blit(button10_text, button10_rect_center)

            pygame.draw.rect(window_surface, button11_color, button11_rect)
            button11_rect_center = button11_text.get_rect(center=button11_rect.center)
            window_surface.blit(button11_text, button11_rect_center)

            pygame.draw.rect(window_surface, button12_color, button12_rect)
            button12_rect_center = button12_text.get_rect(center=button12_rect.center)
            window_surface.blit(button12_text, button12_rect_center)

            pygame.draw.rect(window_surface, button13_color, button13_rect)
            button13_rect_center = button13_text.get_rect(center=button13_rect.center)
            window_surface.blit(button13_text, button13_rect_center)

            pygame.draw.rect(window_surface, button14_color, button14_rect)
            button14_rect_center = button14_text.get_rect(center=button14_rect.center)
            window_surface.blit(button14_text, button14_rect_center)

            pygame.draw.rect(window_surface, button15_color, button15_rect)
            button15_rect_center = button15_text.get_rect(center=button15_rect.center)
            window_surface.blit(button15_text, button15_rect_center)

            pygame.draw.rect(window_surface, button16_color, button16_rect)
            button16_rect_center = button16_text.get_rect(center=button16_rect.center)
            window_surface.blit(button16_text, button16_rect_center)

            pygame.draw.rect(window_surface, button17_color, button17_rect)
            button17_rect_center = button17_text.get_rect(center=button17_rect.center)
            window_surface.blit(button17_text, button17_rect_center)

            pygame.draw.rect(window_surface, button18_color, button18_rect)
            button18_rect_center = button18_text.get_rect(center=button18_rect.center)
            window_surface.blit(button18_text, button18_rect_center)

            pygame.draw.rect(window_surface, button19_color, button19_rect)
            button19_rect_center = button19_text.get_rect(center=button19_rect.center)
            window_surface.blit(button19_text, button19_rect_center)

            pygame.draw.rect(window_surface, button20_color, button20_rect)
            button20_rect_center = button20_text.get_rect(center=button20_rect.center)
            window_surface.blit(button20_text, button20_rect_center)

            pygame.draw.rect(window_surface, button21_color, button21_rect)
            button21_rect_center = button21_text.get_rect(center=button21_rect.center)
            window_surface.blit(button21_text, button21_rect_center)

            pygame.draw.rect(window_surface, button22_color, button22_rect)
            button22_rect_center = button22_text.get_rect(center=button22_rect.center)
            window_surface.blit(button22_text, button22_rect_center)

            pygame.draw.rect(window_surface, button23_color, button23_rect)
            button23_rect_center = button23_text.get_rect(center=button23_rect.center)
            window_surface.blit(button23_text, button23_rect_center)

            pygame.draw.rect(window_surface, button24_color, button24_rect)
            button24_rect_center = button24_text.get_rect(center=button24_rect.center)
            window_surface.blit(button24_text, button24_rect_center)

            pygame.draw.rect(window_surface, button25_color, button25_rect)
            button25_rect_center = button25_text.get_rect(center=button25_rect.center)
            window_surface.blit(button25_text, button25_rect_center)

            pygame.draw.rect(window_surface, button26_color, button26_rect)
            button26_rect_center = button26_text.get_rect(center=button26_rect.center)
            window_surface.blit(button26_text, button26_rect_center)

            pygame.draw.rect(window_surface, button27_color, button27_rect)
            button27_rect_center = button27_text.get_rect(center=button27_rect.center)
            window_surface.blit(button27_text, button27_rect_center)

            pygame.draw.rect(window_surface, button28_color, button28_rect)
            button28_rect_center = button28_text.get_rect(center=button28_rect.center)
            window_surface.blit(button28_text, button28_rect_center)

            pygame.draw.rect(window_surface, button29_color, button29_rect)
            button29_rect_center = button29_text.get_rect(center=button29_rect.center)
            window_surface.blit(button29_text, button29_rect_center)

            pygame.draw.rect(window_surface, button30_color, button30_rect)
            button30_rect_center = button30_text.get_rect(center=button30_rect.center)
            window_surface.blit(button30_text, button30_rect_center)

            pygame.draw.rect(window_surface, button31_color, button31_rect)
            button31_rect_center = button31_text.get_rect(center=button31_rect.center)
            window_surface.blit(button31_text, button31_rect_center)

            pygame.draw.rect(window_surface, button32_color, button32_rect)
            button32_rect_center = button32_text.get_rect(center=button32_rect.center)
            window_surface.blit(button32_text, button32_rect_center)

            pygame.draw.rect(window_surface, button33_color, button33_rect)
            button33_rect_center = button33_text.get_rect(center=button33_rect.center)
            window_surface.blit(button33_text, button33_rect_center)

            background.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

            pygame.display.update()


pygame.init()

men = pygame.display.set_mode((1200, 800))
men.fill(pygame.Color('white'))
menu = pygame_menu.Menu('Добро пожаловать!', 1200, 800, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Играть', start_the_game)
menu.add.button('Придумать слово(второй игрок)', sec)
menu.add.button('Выход', pygame_menu.events.EXIT)

menu.mainloop(men)
