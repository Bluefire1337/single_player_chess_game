import sys
import os
import random
from random import getrandbits
from collections import defaultdict
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
import pygame



#function to check if a location is in a list of lists
def find_tuple(data, target):
    for sublist in data:
        if target in sublist:
            return True
    return False

def empty_list(data):
    for sublist in data:
        if sublist != []:
            return False
    return True

pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Two-Player Chess Game')

font = pygame.font.Font('freesansbold.ttf',20)
medium_font = pygame.font.Font('freesansbold.ttf',40)
big_font = pygame.font.Font('freesansbold.ttf',50)

timer = pygame.time.Clock()
fps = 60

#        pygame.draw.rect(screen, (255, 165, 0), (x, y, w, h))
#         screen.blit(img, (x + 25, y + 25))
#       pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h))
#        screen.blit(img, (x + 25, y + 25))


#function for button
def button(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            print(1)
            return 1
        print(2)
        return 2
        
    else:
        if click[0] == 1:
            print(0)
            return 0
        print(2)
        return 2




#game variables and image
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []


free_squares=[(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5)]
# 0 - white's turn no selection; 1 - white's turn  piece selected; 2 - black's turn no selection; 3 - black's turn piece selected

turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) black and white
black_queen = pygame.image.load('chess_assets/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (80,80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_king=pygame.image.load(resource_path('chess_assets/black_king.png'))
black_king = pygame.transform.scale(black_king, (80,80))
black_king_small = pygame.transform.scale(black_king, (45,45))

black_rook = pygame.image.load(resource_path('chess_assets/black_rook.png'))
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_bishop = pygame.image.load(resource_path('chess_assets/black_bishop.png'))
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_knight = pygame.image.load(resource_path('chess_assets/black_knight.png'))
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_pawn = pygame.image.load(resource_path('chess_assets/black_pawn.png'))
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

white_queen = pygame.image.load(resource_path('chess_assets/white_queen.png'))
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_king = pygame.image.load(resource_path('chess_assets/white_king.png'))
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_rook = pygame.image.load(resource_path('chess_assets/white_rook.png'))
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_bishop = pygame.image.load(resource_path('chess_assets/white_bishop.png'))
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_knight = pygame.image.load(resource_path('chess_assets/white_knight.png'))
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_pawn = pygame.image.load(resource_path('chess_assets/white_pawn.png'))
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

Nothing = pygame.image.load(resource_path('chess_assets/Nothing.png'))
Nothing = pygame.transform.scale(Nothing,(80,80))


white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop, Nothing ]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small, Nothing]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop, Nothing]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small, Nothing]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False

#draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, (140,217,181,255), [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, (140,217,181,255), [700 - (column * 200), row * 100, 100, 100])
        #pygame.draw.rect(screen, 'gray', [0, 800, 800, 100])
        #pygame.draw.rect(screen, 'gold', [0, 800, 800, 100], 10)
        #pygame.draw.rect(screen, 'gold', [800, 0, 200, 800], 10)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'red'), (20, 820))
        #for i in range(9):
            #pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            #pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('Resign', True, 'black'), (810, 830))

#draw pieces on board
def draw_pieces():
        
        for i in range(len(white_pieces)):
            index = piece_list.index(white_pieces[i])
            if white_pieces[i] == 'pawn':
                screen.blit(white_pawn, (white_locations[i][0] * 100 + 16, white_locations[i][1] * 100 + 20))
            else:
                screen.blit(white_images[index], (white_locations[i][0] * 100 + 9, white_locations[i][1] * 100 + 10))
            if turn_step < 2:
                if selection == i:
                    pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2)
        for i in range(len(black_pieces)):
            index = piece_list.index(black_pieces[i])
            if black_pieces[i] == 'pawn':
                screen.blit(black_pawn, (black_locations[i][0] * 100 + 16, black_locations[i][1] * 100 + 20))
            else:
                screen.blit(black_images[index], (black_locations[i][0] * 100 + 9, black_locations[i][1] * 100 + 9))
            if turn_step >= 2:
                if selection == i:
                    pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, turn, kw, rkw, rqw, kb, rkb, rqb): 
    all_moves_list = []
    for i in range(len(pieces)):
        moves_list = []
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn, kw, rkw, rqw, kb, rkb, rqb)
        all_moves_list.append(moves_list)
    return all_moves_list

# check king valid moves
def check_king(position, color, kw, rkw, rqw, kb, rkb, rqb):
    moves_list = []
    if color =='white':
        friends_list = white_locations
        if run:
            attacked_squares = black_options            
    else:
        friends_list = black_locations
        if run:
            attacked_squares = white_options
# 8 squares to check for kings, they can go one square any directions
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if run and find_tuple(attacked_squares, target):
            continue
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
    #castling: king and rook have not moved, no pieces between them, king is not in check, king does not move through check
    if color=='white' and kw==0 and rkw==0 and (kingxw + direction * 1, row) in free_squares and (kingxw + direction * 2, row) in free_squares and not find_tuple(black_options, (kingxw, row)) and not find_tuple(black_options, (kingxw + direction * 1, row)) and not find_tuple(black_options, (kingxw + direction * 2, row)):
        moves_list.append((kingxw + direction * 2, row))
    if color=='white' and kw==0 and rqw==0 and (kingxw + -1 * direction * 1, row) in free_squares and (kingxw + -1 * direction * 2, row) in free_squares and (kingxw + -1 * direction * 3,row) in free_squares and not find_tuple(black_options, (kingxw, row)) and not find_tuple(black_options, (kingxw + -1 * direction * 1, row)) and not find_tuple(black_options, (kingxw + -1 * direction * 2, row)):
        moves_list.append((kingxw + -1 * direction * 2,row))
    if color=='black' and kb==0 and rkb==0 and (kingxb + direction * 1, (row + 7) % 14) in free_squares and (kingxb + direction * 2, (row + 7) % 14) in free_squares and not find_tuple(white_options, (kingxb, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + direction * 1, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + direction * 2, (row + 7) % 14)):
        moves_list.append((kingxb + direction * 2, (row + 7) % 14))
    if color=='black' and kb==0 and rqb==0 and (kingxb + -1 * direction * 1, (row + 7) % 14) in free_squares and (kingxb + -1 * direction * 2, (row + 7) % 14) in free_squares and (kingxb + -1 * direction * 3, (row + 7) % 14) in free_squares and not find_tuple(white_options, (kingxb, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + -1 * direction * 1, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + -1 * direction * 2, (row + 7) % 14)):
        moves_list.append((kingxb + -1 * direction * 2,(row + 7) % 14))
    return moves_list

# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

#check bishop moves
def check_bishop(position, color):
    moves_list=[]
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    for i in range(1,8):
        target=(position[0] + i, position[1] + i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0] - i, position[1]- i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0] + i, position[1]- i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0] - i, position[1] + i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    return moves_list
    
#check rook moves
def check_rook(position, color):
    moves_list=[]
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    for i in range(1,8):
        target=(position[0] + i, position[1])
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0] - i, position[1])
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0], position[1]- i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    for i in range(1,8):
        target=(position[0], position[1] + i)
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
            continue
        if target==en_passant_black or target==en_passant_white:
            moves_list.append(target)
        if target in enemies_list:
            moves_list.append(target)
            break
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
        else:
            break
    return moves_list

#checking valid moves of the knight
def check_knight(position, color):
    moves_list=[]
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    #the knight has 8 "jumps" for a given position
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target=(position[0] + targets[i][0], position[1] + targets[i][1])
        if target==en_passant_black or target==en_passant_white or (target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7):
            moves_list.append(target)
    return moves_list

#valid pawn moves(not en passant, that later) // direction is -1 for playing black and 1 for playing white // you start as black # row is 0 for playing black and 7 for playing white
def check_pawn(position, color):
    moves_list = []
    if color == 'white': # //-1 * direction * 1// = 1 when you play as black and -1 when you play as white
        if (position[0], position[1] + -1 * direction) not in white_locations and (position[0], position[1] + -1 * direction) not in black_locations and 0 < position[1] < 7:
            moves_list.append((position[0], position[1] + -1 * direction))
        if (position[0], position[1] + -1 * direction * 2) not in white_locations and (position[0], position[1] + -1 * direction) not in white_locations and (position[0], position[1] + -1 * direction * 2) not in black_locations and (position[0], position[1] + -1 * direction) not in black_locations and position[1] == zerofive + 1:
            moves_list.append((position[0], position[1] + -1 * direction * 2))
        if (position[0] - -1 * direction * 1, position[1] + -1 * direction * 1) in black_locations:
            moves_list.append((position[0] - -1 * direction * 1, position[1] + -1 * direction * 1))
        if (position[0] + -1 * direction * 1, position[1] + -1 * direction * 1) in black_locations:
            moves_list.append((position[0] + -1 * direction * 1, position[1] + -1 * direction * 1))
    else:
         if (position[0], position[1] - -1 * direction * 1) not in white_locations and (position[0], position[1] - -1 * direction * 1) not in black_locations and 0 < position[1] < 7:
            moves_list.append((position[0], position[1] - -1 * direction * 1))
         if (position[0], position[1] - -1 * direction * 2) not in white_locations and (position[0], position[1] - -1 * direction * 1) not in white_locations and (position[0], position[1] - -1 * direction * 2) not in black_locations and (position[0], position[1] - -1 * direction * 1) not in black_locations and position[1] == (zerofive + 6) % 10:
            moves_list.append((position[0], position[1] - -1 * direction * 2))
         if (position[0] + -1 * direction * 1, position[1] - -1 * direction * 1) in white_locations:
            moves_list.append((position[0] + -1 * direction * 1, position[1] - -1 * direction * 1))
         if (position[0] - -1 * direction * 1, position[1] - -1 * direction * 1) in white_locations:
            moves_list.append((position[0] - -1 * direction * 1, position[1] - -1 * direction * 1))
    return moves_list

#check for valid moves for just a piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options
def check_stalemate(options):
    if empty_list(options):
        return 1
    else:
        return 0



# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index=piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 10 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 10 + 50 * i))

#draw a flashing square around king if in check 
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 +1, white_locations[king_index][1] * 100 +1, 100, 100], 10)
        else:
            if 'king' in black_pieces:
                king_index = black_pieces.index('king')
                king_location = black_locations[king_index]
                for i in range (len(white_options)):
                    if king_location in white_options[i]:
                        if counter < 15:
                            pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1, black_locations[king_index][1] * 100 +1, 100, 100], 10)

def draw_game_over(winner):
        pygame.draw.rect(screen, 'black', [200, 200, 400, 70] )
        screen.blit(font.render(f'{winner} won the game ', True, 'white'), (210, 210))
        screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (210, 240))

def draw_stalemate(colour_stalemates):
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70] )
    screen.blit(font.render(f'1/2-1/2...{colour_stalemates} draws by stalemate', True, 'white'), (210, 210))
    screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (210, 240))

def draw_fifty():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70] )
    screen.blit(font.render(f'1/2-1/2...draw by 50 move rule', True, 'white'), (210, 210))
    screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (210, 240))

def draw_threefold():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70] )
    screen.blit(font.render(f'1/2-1/2...draw by threefold repetition', True, 'white'), (210, 210))
    screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (210, 240))

def handle_promotion(colour, click_coords, selection):
    promotion = True
    while promotion:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if colour == 'white':
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and click_coords[1] * 100 + 100 > mouse[1] > click_coords[1] * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, click_coords[1] * 100, 100, 100))
                screen.blit(white_queen_small, (click_coords[0] * 100 + 25, click_coords[1] * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, click_coords[1] * 100, 100, 100))
                screen.blit(white_queen_small, (click_coords[0] * 100 + 25, click_coords[1] * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + direction * 1) * 100 + 100 > mouse[1] > (click_coords[1] + direction * 1) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + direction * 1) * 100, 100, 100))
                screen.blit(white_knight_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 1) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + direction * 1) * 100, 100, 100))
                screen.blit(white_knight_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 1) * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + direction * 2) * 100 + 100 > mouse[1] > (click_coords[1] + direction * 2) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + direction * 2) * 100, 100, 100))
                screen.blit(white_rook_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 2) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + direction * 2) * 100, 100, 100))
                screen.blit(white_rook_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 2) * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + direction * 3) * 100 + 100 > mouse[1] > (click_coords[1] + direction * 3) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + direction * 3) * 100, 100, 100))
                screen.blit(white_bishop_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 3) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + direction * 3) * 100, 100, 100))
                screen.blit(white_bishop_small, (click_coords[0] * 100 + 25, (click_coords[1] + direction * 3) * 100 + 25))
        else:
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and click_coords[1] * 100 + 100 > mouse[1] > click_coords[1] * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, click_coords[1] * 100, 100, 100))
                screen.blit(black_queen_small, (click_coords[0] * 100 + 25, click_coords[1] * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, click_coords[1] * 100, 100, 100))
                screen.blit(black_queen_small, (click_coords[0] * 100 + 25, click_coords[1] * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + -1 * direction * 1) * 100 + 100 > mouse[1] > (click_coords[1] + -1 * direction * 1) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 1) * 100, 100, 100))
                screen.blit(black_knight_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 1) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 1) * 100, 100, 100))
                screen.blit(black_knight_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 1) * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + -1 * direction * 2) * 100 + 100 > mouse[1] > (click_coords[1] + -1 * direction * 2) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 2) * 100, 100, 100))
                screen.blit(black_rook_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 2) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 2) * 100, 100, 100))
                screen.blit(black_rook_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 2) * 100 + 25))
            if click_coords[0] * 100 + 100 > mouse[0] > click_coords[0] * 100  and (click_coords[1] + -1 * direction * 3) * 100 + 100 > mouse[1] > (click_coords[1] + -1 * direction * 3) * 100:
                pygame.draw.rect(screen, (255, 165, 0), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 3) * 100, 100, 100))
                screen.blit(black_bishop_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 3) * 100 + 25))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (click_coords[0] * 100, (click_coords[1] + -1 * direction * 3) * 100, 100, 100))
                screen.blit(black_bishop_small, (click_coords[0] * 100 + 25, (click_coords[1] + -1 * direction * 3) * 100 + 25))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if colour == 'white':
                    q = button(click_coords[0] * 100, click_coords[1] * 100, 100, 100)
                    n = button((click_coords[0]) * 100, (click_coords[1] + direction * 1) * 100, 100, 100)
                    r = button((click_coords[0]) * 100, (click_coords[1] + direction * 2) * 100, 100, 100)
                    b = button((click_coords[0]) * 100, (click_coords[1] + direction * 3) * 100, 100, 100)
                
                    if q == 1:
                        white_pieces[selection] = 'queen'
                        promotion = False
                    elif n == 1:
                        white_pieces[selection] = 'knight'
                        promotion = False
                    elif r == 1:
                        white_pieces[selection] = 'rook'
                        promotion = False
                    elif b == 1:
                        white_pieces[selection] = 'bishop'
                        promotion = False
                else:
                    q = button(click_coords[0] * 100, click_coords[1] * 100, 100, 100)
                    n = button((click_coords[0]) * 100, (click_coords[1] + -1 * direction * 1) * 100, 100, 100)
                    r = button((click_coords[0]) * 100, (click_coords[1] + -1 * direction * 2) * 100, 100, 100)
                    b = button((click_coords[0]) * 100, (click_coords[1] + -1 * direction * 3) * 100, 100, 100)
                    if q == 1:
                        black_pieces[selection] = 'queen'
                        promotion = False
                    elif n == 1:
                        black_pieces[selection] = 'knight'
                        promotion = False
                    elif r == 1:
                        black_pieces[selection] = 'rook'
                        promotion = False
                    elif b == 1:
                        black_pieces[selection] = 'bishop'
                        promotion = False

# Zobrist hashing function
# generates a unique hash for the current position based on the pieces and their locations
PIECES = ["P", "N", "B", "R", "Q", "K",  "p", "n", "b", "r", "q", "k"]  #capital letters for white pieces, lowercase for black pieces required for FEN
zobrist_board = [[getrandbits(64) for _ in range(64)] for _ in range(12)] #64 bits for each piece, 12 pieces in total
piece_to_index = { 'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5, 'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11 }
zobrist_side = getrandbits(64) #hash for side to move
zobrist_castling =[getrandbits(64) for _ in range(4)] 
zobrist_en_passant = [getrandbits(64) for _ in range(8)] #hash for en passant square; you only need 8 not 16 because zobrist side differentiates for which side has en passant
#starting FEN position
starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
def zobrist_hash (fen):
    fen_parts = fen.split()
    piece_placement = fen_parts[0]
    side_to_move = fen_parts[1]
    castling = fen_parts[2]
    en_passant = fen_parts[3]
    hash=0
    ranks = piece_placement.split('/')
    for rank in range(7):
        rank = 7 - rank
        file = 0
        for char in ranks[rank]:
            if(char.isdigit()):
                file += int(char)
            else:
                piece_index = piece_to_index[char]
                hash ^= zobrist_board[piece_index][rank * 8 + file]
                file += 1
    if side_to_move == 'b':
        hash ^= zobrist_side
    rights = 'KQkq'
    for i, right in enumerate(rights):
        if right in castling:
            hash ^= zobrist_castling[i] 
    if en_passant != '-':
        file = ord(en_passant[0]) - ord('a')
        hash ^= zobrist_en_passant[file]
    return hash
                
start_hash = zobrist_hash(starting_position) #starting hash for the game
board_history = defaultdict(int) #dictionary to store board positions and their counts
board_history[start_hash] = 1 #initialize the starting position count to 1

black_dict = { 'rook' : 'r' , 'knight' : 'n', 'bishop' : 'b', 'queen' : 'q', 'king' : 'k', 'pawn' : 'p' }
white_dict = { 'rook' : 'R' , 'knight' : 'N', 'bishop' : 'B', 'queen' : 'Q', 'king' : 'K', 'pawn' : 'P' }
#main game loop
#DON'T FORGET TO UPDATE THE FREE_SQUARES VECTOR
run = False
stalemate=False #stalemate draw flag
fifty_draw=False #fifty move draw flag
threefold = False #threefold repetition draw flag
fifty_counter=0 #fifty move counter
restart_v=0 #restart variable, 0 or 1, used for switching colors // 0 is for playing as black
row=0
reverse_row=7 #used for colour switching in check_pawn

undo_click=(-1,-1) #for undo move function

zerofive=0
fivezero=5
direction=-1
kingxw=-1 #king x coordonate for white // used for switching colours in castling
kingxb=-1 #king x coordonate for black

en_passant_white=None #en passant square for white
en_passant_black=None

en_passant_hash_flag=False #en passant hash flag, used to check if en passant square is valid for the current position

#flags for castling
kw=0
rkw=0
rqw=0
kb=0
rkb=0
rqb=0

black_options = check_options(black_pieces, black_locations, 'black', kw, rkw, rqw, kb, rkb, rqb)
white_options = check_options(white_pieces, white_locations, 'white', kw, rkw, rqw, kb, rkb, rqb)   
pawn_coords_white=None
pawn_coords_black=None
white_piece_index=None
black_piece_index=None

promotion=True

p=0
w=0
i=1
p_pos = None
run = True
position_hash = start_hash
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill((77,136,99,255))
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if 'king' in white_pieces and 'king' in black_pieces:
        white_king_index = white_pieces.index('king')
        black_king_index = black_pieces.index('king')
        kingxw=white_locations[white_king_index][0]
        kingxb=black_locations[black_king_index][0]
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if(find_tuple(white_options, en_passant_black)):
                    position_hash ^= zobrist_en_passant[en_passant_black[0]]
                    en_passant_hash_flag = True
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    undo_click = click_coords
                    selection = white_locations.index(click_coords)
                    iw = white_locations.index(click_coords)
                    if white_pieces[iw]=='pawn':
                        p=1
                        p_pos = click_coords
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    free_squares.append(white_locations[selection])
                    white_letter= white_dict[white_pieces[iw]]
                    position_hash ^= zobrist_board[piece_to_index[white_letter]][undo_click[1] * 8 + undo_click[0]]
                    if white_pieces[selection] == 'king' and kw == 0 : # Castling // direction is -1 for playing black and 1 for playing white // you start as black # row is 0 for playing black and 7 for playing white   
                        if click_coords == (kingxw + direction * 2, row) and rkw == 0 and not find_tuple(black_options, (kingxw, row)) and not find_tuple(black_options, (kingxw + direction * 1, row)) and not find_tuple(black_options, (kingxw + direction * 2, row)):
                            white_locations[white_locations.index((row, row))] = (kingxw + direction * 1, row)
                            free_squares.pop(free_squares.index((kingxw + direction * 1, row)))
                            free_squares.append((row, row))
                            position_hash ^= zobrist_board[piece_to_index['R']][(row, row)[1] * 8 + (row, row)[0]] #place of rook before castling
                            position_hash ^= zobrist_board[piece_to_index['R']][(kingxw + direction * 1, row)[1] * 8 + (kingxw + direction * 1, row)[0]] #place of rook after castling
                            #rights = 'KQkq'
                            position_hash ^= zobrist_castling[0] #remove castling right for white king side
                            position_hash ^= zobrist_castling[1] #remove castling right for white queen side
                            kw=1
                            rkw=1
                            rqw=1
                            # print(free_squares)
                            # print()
                        if click_coords == (kingxw + -1 * direction * 2, row) and rqw == 0 and not find_tuple(black_options, (kingxw, row)) and not find_tuple(black_options, (kingxw + -1 * direction * 1, row)) and not find_tuple(black_options, (kingxw + -1 * direction * 2, row)):
                            white_locations[white_locations.index(((row + 7) % 14, row))] = (kingxw + -1 * direction * 1, row)
                            free_squares.pop(free_squares.index((kingxw + -1 * direction * 1, row)))
                            free_squares.append(((row + 7) % 14, row))
                            position_hash ^= zobrist_board[piece_to_index['R']][((row + 7) % 14, row)[1] * 8 + ((row + 7) % 14, row)[0]] #place of rook before castling
                            position_hash ^= zobrist_board[piece_to_index['R']][(kingxw + -1 * direction * 1, row)[1] * 8 + (kingxw + -1 * direction * 1, row)[0]] #place of rook after castling
                            #rights = 'KQkq'
                            position_hash ^= zobrist_castling[0] #remove castling right for white king side
                            position_hash ^= zobrist_castling[1] #remove castling right for white queen side
                    if click_coords == (row, row) and white_pieces[selection] == 'rook': # Castling; Move king side rook so king side castling is disabled
                        if rkw == 0: #if king side castling is not disabled, remove castling right for white king side
                            position_hash ^= zobrist_castling[0] #remove castling right for white king side
                        rkw=1
                    if click_coords == ((row + 7) % 14, row) and white_pieces[selection] == 'rook': # Castling; Move queen side rook so queen side castling is disabled  
                        if rkw == 0: #if king side castling is not disabled, remove castling right for white queen side 
                            position_hash ^= zobrist_castling[1] #remove castling right for white king side
                        rqw=1
                    if white_pieces[selection] == 'king': # Castling; Move king so castling is disabled
                        if kw == 0: #if castling is not disabled, remove castling right for white king
                            position_hash ^= zobrist_castling[0] #remove castling right for white king side
                            position_hash ^= zobrist_castling[1] #remove castling right for white queen side
                        kw=1
                    if click_coords not in black_locations:
                        free_squares.pop(free_squares.index(click_coords))
                    white_locations[selection] = click_coords
                    if(p == 1):
                        fifty_counter = 0
                    else:
                        fifty_counter += 1
                    if p == 1:
                        if(click_coords[1] == p_pos[1] + -1 * direction * 2): # En passant
                            en_passant_white = (p_pos[0], (click_coords[1] + p_pos[1]) // 2)
                            white_locations.append(en_passant_white)
                            white_pieces.append('ghost_pawn')
                            piece_list.append('ghost_pawn')
                            pawn_coords_white = click_coords
                            free_squares.pop(free_squares.index(en_passant_white))
                            fifty_counter = 0
                        if click_coords[1] == (row + 7) % 14:
                            # Promotion
                            handle_promotion('white', click_coords, selection)
                            position_hash ^= zobrist_board[piece_to_index['P']][click_coords[1] * 8 + click_coords[0]] #remove pawn hash from position
                            if white_pieces[selection] == 'queen':
                                position_hash ^= zobrist_board[piece_to_index['Q']][click_coords[1] * 8 + click_coords[0]]
                            if white_pieces[selection] == 'knight':
                                position_hash ^= zobrist_board[piece_to_index['N']][click_coords[1] * 8 + click_coords[0]]
                            if white_pieces[selection] == 'rook':
                                position_hash ^= zobrist_board[piece_to_index['R']][click_coords[1] * 8 + click_coords[0]]
                            if white_pieces[selection] == 'bishop':
                                position_hash ^= zobrist_board[piece_to_index['B']][click_coords[1] * 8 + click_coords[0]]
                            fifty_counter = 0
                              
                    if click_coords in black_locations:
                        if(click_coords != en_passant_black):
                            captured_black_piece = black_pieces[black_locations.index(click_coords)]
                            position_hash ^= zobrist_board[piece_to_index[black_dict[captured_black_piece]]][click_coords[1] * 8 + click_coords[0]] #remove captured piece hash from position
                        if click_coords == en_passant_black:
                            if p == 1:
                                black_piece_index = black_locations.index(pawn_coords_black)  # Ensure pawn location matches
                                captured_pieces_black.append(black_pieces[black_piece_index])
                                black_pieces.pop(black_piece_index)
                                black_locations.pop(black_piece_index)
                                free_squares.append(pawn_coords_black)
                                fifty_counter = 0
                                if 'ghost_pawn' in black_pieces: # coming back at this condition after months, I don't think it is necessary anymore, but I will leave it here for now
                                    ghost_index = black_pieces.index('ghost_pawn')
                                    black_pieces.pop(ghost_index)
                                    black_locations.pop(ghost_index)
                                    piece_list.pop(6)
                        else:
                                    black_piece = black_locations.index(click_coords)
                                    captured_pieces_white.append(black_pieces[black_piece])
                                    if black_pieces[black_piece] == 'king':
                                        winner = 'white'
                                    black_pieces.pop(black_piece)
                                    black_locations.pop(black_piece)
                                    fifty_counter = 0
                    position_hash ^= zobrist_board[piece_to_index[white_letter]][click_coords[1] * 8 + click_coords[0]] #place of piece after move
                    white_options = check_options(white_pieces, white_locations, 'white', kw, rkw, rqw, kb, rkb, rqb)
                    black_options = check_options(black_pieces, black_locations, 'black', kw, rkw, rqw, kb, rkb, rqb)
                    white_options = check_options(white_pieces, white_locations, 'white', kw, rkw, rqw, kb, rkb, rqb)
                    if en_passant_black != None and en_passant_hash_flag:
                        position_hash ^= zobrist_en_passant[en_passant_black[0]]
                    en_passant_hash_flag = False
                    #print(black_options)
                    if(check_stalemate(black_options)):
                        game_over=True
                        stalemate=True
                        colour_stalemates = 'white'
                    if(fifty_counter >= 100):
                        game_over=True
                        fifty_draw=True
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    p=0
                    p_pos=None
                    if en_passant_black != None:
                        free_squares.append(en_passant_black)
                        en_passant_black=None
                    if 'ghost_pawn' in black_pieces:
                        ghost_index = black_pieces.index('ghost_pawn')
                        black_pieces.pop(ghost_index)
                        black_locations.pop(ghost_index)
                        piece_list.pop(6)
                    position_hash ^= zobrist_side #toggle side to move
                    board_history[position_hash] += 1
                    if board_history[position_hash] == 3: #if position is repeated, draw by threefold repetition
                        game_over=True
                        threefold = True
            elif turn_step > 1:
                if(find_tuple(black_options, en_passant_white)):
                    position_hash ^= zobrist_en_passant[en_passant_white[0]]
                    en_passant_hash_flag = True
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    undo_click = click_coords
                    selection = black_locations.index(click_coords)
                    ib = black_locations.index(click_coords)
                    if black_pieces[ib]=='pawn':
                        p=1
                        p_pos=click_coords
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    free_squares.append(black_locations[selection])
                    black_letter = black_dict[black_pieces[ib]]
                    position_hash ^= zobrist_board[piece_to_index[black_letter]][undo_click[1] * 8 + undo_click[0]]
                    #rights = 'KQkq'
                    if black_pieces[selection] == 'king' and kb == 0: # Castling
                        if click_coords == (kingxb + direction * 2, (row + 7) % 14) and rkb == 0 and not find_tuple(white_options, (kingxb, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + direction * 1, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + direction * 2, (row + 7) % 14)):
                            black_locations[black_locations.index((row, (row + 7) % 14))] = (kingxb + direction * 1, (row + 7) % 14)
                            free_squares.pop(free_squares.index((kingxb + direction * 1, (row + 7) % 14)))
                            free_squares.append((row, (row + 7) % 14))
                            position_hash ^= zobrist_board[piece_to_index['r']][(row, (row + 7) % 14)[1] * 8 + (row, (row + 7) % 14)[0]] #place of rook before castling
                            position_hash ^= zobrist_board[piece_to_index['r']][(kingxb + direction * 1, (row + 7) % 14)[1] * 8 + (kingxb + direction * 1, (row + 7) % 14)[0]] #place of rook after castling
                            position_hash ^= zobrist_castling[2] #remove castling right for black king side
                            position_hash ^= zobrist_castling[3] #remove castling right for black queen
                            kb=1
                            rkb=1
                            rqb=1

                        if click_coords == (kingxb + -1 * direction * 2, (row + 7) % 14) and rqb == 0 and not find_tuple(white_options, (kingxb, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + -1 * direction * 1, (row + 7) % 14)) and not find_tuple(white_options, (kingxb + -1 * direction * 2, (row + 7) % 14)):
                            black_locations[black_locations.index(((row + 7) % 14, (row + 7) % 14))] = (kingxb + -1 * direction * 1, (row + 7) % 14)
                            free_squares.pop(free_squares.index((kingxb + -1 * direction * 1, (row + 7) % 14)))
                            free_squares.append(((row + 7) % 14, (row + 7) % 14))
                            position_hash ^= zobrist_board[piece_to_index['r']][((row + 7) % 14, (row + 7) % 14)[1] * 8 + ((row + 7) % 14, (row + 7) % 14)[0]] #place of rook before castling
                            position_hash ^= zobrist_board[piece_to_index['r']][(kingxb + -1 * direction * 1, (row + 7) % 14)[1] * 8 + (kingxb + -1 * direction * 1, (row + 7) % 14)[0]] #place of rook after castling
                            #rights = 'KQkq'
                            position_hash ^= zobrist_castling[2] #remove castling right for black king side
                            position_hash ^= zobrist_castling[3] #remove castling right for black queen
                    if click_coords == (row, (row + 7) % 14) and black_pieces[selection] == 'rook': # Castling
                        if rkb == 0: #if king side castling is not disabled, remove castling right for black king side
                            position_hash ^= zobrist_castling[2] #remove castling right for black king side
                        rkb=1
                    if click_coords == ((row + 7) % 14, (row + 7) % 14) and black_pieces[selection] == 'rook': # Castling
                        if rqb == 0: #if queen side castling is not disabled, remove castling right for black queen side
                            position_hash ^= zobrist_castling[3] #remove castling right for black queen side
                        rqb=1
                    if black_pieces[selection] == 'king': # Castling
                        if kb == 0: #if castling is not disabled, remove castling right for black king
                            position_hash ^= zobrist_castling[2] #remove castling right for black king side
                            position_hash ^= zobrist_castling[3] #remove castling right for black queen
                        kb=1
                    if click_coords not in white_locations:
                        free_squares.pop(free_squares.index(click_coords))
                    black_locations[selection] = click_coords
                    if(p == 1):
                        fifty_counter = 0
                    else:
                        fifty_counter += 1
                    if p==1:
                        if(click_coords[1] == p_pos[1] - -1 * direction * 2): # En passant
                            en_passant_black=(p_pos[0],(click_coords[1] + p_pos[1]) // 2)
                            black_locations.append(en_passant_black)
                            black_pieces.append('ghost_pawn')
                            piece_list.append('ghost_pawn')
                            pawn_coords_black=click_coords
                            free_squares.pop(free_squares.index(en_passant_black))
                            fifty_counter = 0
                        if click_coords[1] == row:
                            # Promotion
                            handle_promotion('black', click_coords, selection)
                            position_hash ^= zobrist_board[piece_to_index['p']][click_coords[1] * 8 + click_coords[0]] #remove pawn hash from position
                            if black_pieces[selection] == 'queen':
                                position_hash ^= zobrist_board[piece_to_index['q']][click_coords[1] * 8 + click_coords[0]] 
                            if black_pieces[selection] == 'knight':
                                position_hash ^= zobrist_board[piece_to_index['n']][click_coords[1] * 8 + click_coords[0]]
                            if black_pieces[selection] == 'rook':
                                position_hash ^= zobrist_board[piece_to_index['r']][click_coords[1] * 8 + click_coords[0]]
                            if black_pieces[selection] == 'bishop':
                                position_hash ^= zobrist_board[piece_to_index['b']][click_coords[1] * 8 + click_coords[0]]
                            fifty_counter = 0
                    if click_coords in white_locations:
                        if(click_coords != en_passant_white):
                            captured_white_piece = white_pieces[white_locations.index(click_coords)]
                            position_hash ^= zobrist_board[piece_to_index[white_dict[captured_white_piece]]][click_coords[1] * 8 + click_coords[0]]
                        if click_coords == en_passant_white:
                            if p == 1:
                                white_piece_index = white_locations.index(pawn_coords_white)  # Ensure pawn location matches
                                captured_pieces_white.append(white_pieces[white_piece_index])
                                white_pieces.pop(white_piece_index)
                                white_locations.pop(white_piece_index)
                                free_squares.append(pawn_coords_white)
                                fifty_counter = 0
                                if 'ghost_pawn' in white_pieces:
                                    ghost_index = white_pieces.index('ghost_pawn')
                                    white_pieces.pop(ghost_index)
                                    white_locations.pop(ghost_index)
                                    piece_list.pop(6)
                                    
                        else:
                                white_piece = white_locations.index(click_coords)
                                captured_pieces_black.append(white_pieces[white_piece])
                                if white_pieces[white_piece] == 'king':
                                    winner = 'black'
                                white_pieces.pop(white_piece)
                                white_locations.pop(white_piece)
                                fifty_counter = 0
                    position_hash ^= zobrist_board[piece_to_index[black_letter]][click_coords[1] * 8 + click_coords[0]] #place of piece after move
                    black_options = check_options(black_pieces, black_locations, 'black', kw, rkw, rqw, kb, rkb, rqb)
                    white_options = check_options(white_pieces, white_locations, 'white', kw, rkw, rqw, kb, rkb, rqb)
                    black_options = check_options(black_pieces, black_locations, 'black', kw, rkw, rqw, kb, rkb, rqb)
                    if en_passant_white != None and en_passant_hash_flag:
                        position_hash ^= zobrist_en_passant[en_passant_white[0]]
                    en_passant_hash_flag = False
                    # print(white_options)
                    # print ('\n')
                    if(check_stalemate(white_options)):
                        game_over=True
                        stalemate=True
                        colour_stalemates = 'black'
                    if(fifty_counter >=100):
                        game_over=True
                        fifty_draw=True
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    p=0
                    p_pos=None
                    if en_passant_white != None:
                        free_squares.append(en_passant_white)
                        en_passant_white=None
                    if 'ghost_pawn' in white_pieces:
                        ghost_index = white_pieces.index('ghost_pawn')
                        white_pieces.pop(ghost_index)
                        white_locations.pop(ghost_index)
                        piece_list.pop(6)
                    position_hash ^= zobrist_side #toggle side to move
                    board_history[position_hash] += 1
                    if board_history[position_hash] == 3: #if position is repeated, draw by threefold repetition
                        game_over=True
                        threefold = True
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                with open("chess_assets/chess_results.txt", "a") as my_file:
                    if(winner == 'black' or winner == 'white'):
                        my_file.write(f"{i}. {winner} won the game \n")
                        i=i+1
                        w=0
                    elif (stalemate):
                        my_file.write(f"{i}. 1/2-1/2...Draw by stalemate \n")
                        i=i+1
                        w=0
                    elif (fifty_draw):
                        my_file.write(f"{i}. 1/2-1/2...Draw by 50 move rule \n")
                        i=i+1
                        w=0
                    elif (threefold):
                        my_file.write(f"{i}. 1/2-1/2...Draw by threefold repetition \n")
                        i=i+1
                        w=0
                game_over = False
                winner = ''
                restart_v=(restart_v + 1) % 2
                
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook','pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook','pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                if restart_v == 0:      
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    row = 0
                    direction = -1
                    reverse_row = 7
                    zerofive=0
                    fivezero=5
                else:
                    white_locations = [(0, 7), (1, 7), (2, 7), (4, 7), (3, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    black_locations = [(0, 0), (1, 0), (2, 0), (4, 0), (3, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    row = 7
                    direction = 1
                    reverse_row = 0
                    zerofive=5
                    fivezero=0
                kingxw=white_locations[3][0]
                kingxb=black_locations[3][0]
                free_squares = [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                kw = 0
                rkw = 0
                rqw = 0
                kb = 0
                rkb = 0
                rqb = 0
                black_options = check_options(black_pieces, black_locations, 'black', kw, rkw, rqw, kb, rkb, rqb)
                white_options = check_options(white_pieces, white_locations, 'white', kw, rkw, rqw, kb, rkb, rqb)
                stalemate=False
                fifty_counter = 0
                threefold = False
                start_hash = zobrist_hash(starting_position) #starting hash for the game
                board_history = defaultdict(int) #dictionary to store board positions and their counts
                board_history[start_hash] = 1 #initialize the starting position count to 1


    if winner != '':
        game_over = True
        draw_game_over(winner)
        w=1
    else:
        if(stalemate):
            draw_stalemate(colour_stalemates)
        if(fifty_counter >= 100):
            draw_fifty()
        if(threefold):
            draw_threefold()

    pygame.display.flip()
pygame.quit()
