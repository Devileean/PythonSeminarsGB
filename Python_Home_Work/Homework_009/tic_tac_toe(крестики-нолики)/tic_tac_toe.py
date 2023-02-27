import sys
import pygame


def tic_tac_toe():
    print(
        'Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP\n'
    )
    pygame.init()  # инициализируем библиотеку
    size_block = (100)  # размер блока
    margin = 5  # отступы
    width = height = size_block * 3 + margin * 4  # высота и ширина блока и оступов
    size_window = (width, height)  # размер окна
    screen = pygame.display.set_mode(size_window)  # задаём окну размер
    pygame.display.set_caption("Крестики-нолики")  # задаём окну заглавие

    black = (0, 0, 0)  # чёрный
    red = (255, 0, 0)  # красный
    green = (0, 255, 0)  # зёлёный
    white = (255, 255, 255)  # белый
    gray = (211, 211, 211)  # серый
    field_game = [[0] * 3 for i in range(3)]  # массив поля 3*3 заполненный 0
    query = 0  # 1 2 3 4 5 6 7  чередование ходов
    game_over = False  # флаг окончания игры
    screen.fill(gray)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ловим ивент на закрытие окна и убиваем приложение
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # клик мышки и не геймовер
                x_mouse, y_mouse = pygame.mouse.get_pos()  # получение позиции по х,у мышки
                col = x_mouse // (size_block + margin)  # номер колонки по которой кликнули
                row = y_mouse // (size_block + margin)  # номер строки по которой кликнули
                if field_game[row][col] == 0:  # если строка и колонка пустые
                    if query % 2 == 0:  # проверяем на чётность
                        field_game[row][col] = 'x'  # и рисуем крестик
                    else:  # иначе
                        field_game[row][col] = 'o'  # рисуем нолик
                    query += 1  # чередуем ход
            # иначе если нажали клавишу и нажали пробел
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False  # заканчиваем игру
                field_game = [[0] * 3 for i in range(3)]  # обнуляем массив
                query = 0  # сбрасываем чередование
                screen.fill(black)  # заполняем чёрным цветом окно
        if not game_over:  # если не геймовер
            for row in range(3):  # обход строк
                for col in range(3):  # обход колонок
                    if field_game[row][col] == 'x':  # если колонка и строка х
                        color = red  # красим в красный
                    elif field_game[row][col] == 'o':  # если колонка и строка х
                        color = green  # красим в зелёный
                    else:
                        color = black  # красим в белый
                    x = col * size_block + (col + 1) * margin  # колонка + размер блока +(номер колонки+1)* кол отступов
                    y = row * size_block + (row + 1) * margin  # строка + размер блока +(номер строки+1)* кол отступов
                    pygame.draw.rect(screen, color,
                                     (x, y, size_block, size_block))  # экран, цвет,(координаты верх левый, низ правый)
                    if color == red:  # если цвет красный
                        # рисуем крестик по координатам
                        pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                        pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
                    elif color == green:  # если цвет зелёный
                        # рисуем кружок по координатам
                        pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                           size_block // 2 - 3,
                                           5)
        if (query - 1) % 2 == 0:  # x
            game_over = check_win(field_game, 'x')  # проверяем на победу х
        else:
            game_over = check_win(field_game, 'o')  # проверяем на победу у
        if game_over:  # если геймовер

            screen.fill(black)  # заполняем чёрным цветом экран
            font = pygame.font.SysFont('stxingkai', 80)  # указываем шрифт и размер
            text1 = font.render(game_over, True, white)  # рендерим шрифт
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])
        pygame.display.update()  # обновляем экран


def check_win(field_game, sign):

    nulls = 0
    for row in field_game:
        nulls += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if field_game[0][col] == sign and field_game[1][col] == sign and field_game[2][col] == sign:
            return sign
    if field_game[0][0] == sign and field_game[1][1] == sign and field_game[2][2] == sign:
        return sign
    if field_game[0][2] == sign and field_game[1][1] == sign and field_game[2][0] == sign:
        return sign
    if nulls == 0:
        return 'Ничья'
    return False

tic_tac_toe()