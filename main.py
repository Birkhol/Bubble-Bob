import pygame
import sys
import random
from bigGuy import BigGuy
from bladeGuy import BladeGuy
from player import Player
from bubble import Bubble
import os
from constants import *
from gameState import level

# Initialize Pygame
pygame.init()
# init sounds
pygame.mixer.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BubbleZilla")
clock = pygame.time.Clock()
heart_image = pygame.image.load("assets/heart.png").convert_alpha()
heart_image = pygame.transform.smoothscale(heart_image, (30, 30))

# Load the background image
background_image = pygame.image.load("assets/background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale to screen size

font = pygame.font.Font(None, 36)
BUBBLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(BUBBLE_EVENT, 1000)  # Spawn a bubble every second
allowed_spawn_areas = [(90, SCREEN_WIDTH - 80 - 50)]

def draw_hearts(screen, hp, x_offset):
    for i in range(hp):
        screen.blit(heart_image, (x_offset, 10))
        x_offset += heart_image.get_width() + 5
def show_level2_screen():
    """Displays the screen before Level 2 starts."""
    screen.blit(background_image, (0, 0))  # Load and display the background image
    title_text = font.render("SvenOl AI: You won the battle, but not the war!", True, BLACK)
    continue_text = font.render("Press SPACE to continue to Level 2.", True, BLACK)
    quit_text = font.render("Press Q to quit.", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 100))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.flip()  # Update the display

    # Wait for SPACE or Q key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Continue to Level 2
                    waiting = False
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()
def show_level3_screen():
    """Displays the screen before Level 3 starts."""
    screen.blit(background_image, (0, 0))  # Load and display the background image
    title_text = font.render("SvenOl AI: You are impressive, but you are not ready for my next form!", True, BLACK)
    continue_text = font.render("Press SPACE to continue to Level 3.", True, BLACK)
    quit_text = font.render("Press Q to quit.", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 100))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.flip()  # Update the display

        # Wait for SPACE or Q key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Continue to Level 2
                    waiting = False
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()

def show_level4_screen():
    """Displays the screen before Level 4 starts."""
    screen.blit(background_image, (0, 0))  # Load and display the background image
    title_text = font.render("SvenOl AI: YOU ARE DOOMED!", True, BLACK)
    continue_text = font.render("Press SPACE to continue to Level 4.", True, BLACK)
    quit_text = font.render("Press Q to quit.", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 100))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.flip()  # Update the display

    # Wait for SPACE or Q key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Continue to Level 2
                    waiting = False
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()
def show_victory_screen():
    """Displays the victory screen and waits for the player to restart the game."""
    screen.blit(background_image, (0, 0))  # Display the background image
    title_text = font.render("You have defeated SvenOl AI!", True, BLACK)
    reign_text = font.render("Bubbles reign supreme! All Hail Bubbles.", True, BLACK)
    restart_text = font.render("Press P if you want to play again.", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 100))
    screen.blit(reign_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2))

    pygame.display.flip()  # Update the display

    # Wait for the player to press P to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False  # Exit the loop when P is pressed

def show_pre_fight_screen():
    """Displays the pre-fight screen with a message and instructions for the boss fight."""
    screen.blit(background_image, (0, 0))  # Load and display the background image
    title_text = font.render("Oh, but this is not the end...", True, BLACK)
    fight_text = font.render("Now is the time for a real fight!", True, BLACK)
    shoot_text = font.render("Press X to shoot bubbles.", True, BLACK)
    move_text = font.render("Use WS or arrow keys to move vertically.", True, BLACK)
    start_text = font.render("Press SPACE to continue...", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 140))
    screen.blit(fight_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100))
    screen.blit(shoot_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 60))
    screen.blit(move_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 20))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))

    pygame.display.flip()  # Update the display

    # Wait for SPACE key press to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False  # Exit the loop when SPACE is pressed


def show_welcome_screen():
    """Displays the welcome screen with game instructions."""
    screen.blit(background_image, (0, 0))  # Load and display the background image
    title_text = font.render("Welcome to BubbleZilla!", True, BLACK)
    instructions_text = font.render(
    "Goal: Feed the chunky bubble to your left with bubbles.", True, BLACK
    )
    controls_line1 = font.render(
        "Controls: Use arrow keys or AD to move.", True, BLACK
    )
    controls_line2 = font.render(
        "Space or arrow UP to jump.", True, BLACK
    )
    controls_line3 = font.render(
        "Avoid blades thrown by SvenOl AI!", True, BLACK
    )
    start_text = font.render("Press space to start...", True, BLACK)

    # Draw text on the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 180))
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 130))
    screen.blit(controls_line1, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 80))
    screen.blit(controls_line2, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 40))
    screen.blit(controls_line3, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100))

    pygame.display.flip()  # Update the display

    # Wait for any key press to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False  # Exit the loop when a key is pressed


def initialize_game():
    global player, bubblesFalling, fight_bubbles, blades, all_sprites, big_guy, blade_guy, game_over, win_state, score, popSound, jumpSound, disposeSound, ouchSound, dieSound, s
    global player, bubblesFalling, blades, fight_bubbles, all_sprites, big_guy, blade_guy, game_over, win_state, score, level
    player = Player()
    big_guy = BigGuy()
    blade_guy = BladeGuy()
    bubblesFalling = pygame.sprite.Group()
    blades = pygame.sprite.Group()
    fight_bubbles = pygame.sprite.Group()  # Group for BigGuy's bubbles
    all_sprites = pygame.sprite.Group(player, big_guy, blade_guy)
    game_over = False
    win_state = None  # None = ongoing, True = Big Guy wins, False = Blade Guy wins
    score = 0
    s = 'sounds'
    popSound = pygame.mixer.Sound(os.path.join(s, 'pop.mp3'))
    jumpSound = pygame.mixer.Sound(os.path.join(s, 'jump.mp3'))
    disposeSound = pygame.mixer.Sound(os.path.join(s, 'dispose.mp3'))
    ouchSound = pygame.mixer.Sound(os.path.join(s, 'ouch.mp3'))
    dieSound = pygame.mixer.Sound(os.path.join(s, 'die.mp3'))
    level = 1


def stop_game(winner=None):
    """Stops the game and displays the appropriate ending screen."""
    global game_over, win_state, blade_guy, level
    game_over = True
    win_state = winner  # None if no winner, True if player wins, False if player loses

    # Initialize default messages to avoid UnboundLocalError
    state_text = ""
    line1 = ""
    line2 = ""

    if not winner:
        # Player loses
        state_text = "YOU LOSE!"
        line1 = "Press P to play again."
        line2 = ""  # No additional line for losing case
    elif winner and level == 1:
        # Transition to Level 2
        show_level2_screen()  # Display Level 2 transition screen
        blade_guy.hp = 3  # Restore Blade Guy's HP
        level += 1  # Increment the level
        blade_guy.increase_speed(level)  # Activate speed boost for Level 2
        game_over = False  # Reset game state for the next level
        return  # Skip the rest of the function since the game continues
    elif winner and level == 2:
        # Transition to Level 3
        show_level3_screen()  # Display Level 3 transition screen
        blade_guy.hp = 3  # Restore Blade Guy's HP
        level += 1  # Increment the level
        blade_guy.increase_speed(level)  # Activate speed boost for Level 3
        game_over = False  # Reset game state for the next level
        return  # Skip the rest of the function since the game continues
    elif winner and level == 3:
        # Transition to Level 3
        show_level4_screen()  # Display Level 4 transition screen
        blade_guy.hp = 3  # Restore Blade Guy's HP
        level += 1  # Increment the level
        blade_guy.increase_speed(level)  # Activate speed boost for Level 3
        game_over = False  # Reset game state for the next level
        return  # Skip the rest of the function since the game continues
    else:
        # Final victory after Level 2
        state_text = "You have defeated Sven-Ol-AI!"
        line1 = "Bubbles reign supreme! All Hail Bubbles."
        line2 = "Press P to play again."  # Allow the player to restart after final victory

    # Draw the text on the screen
    screen.blit(background_image, (0, 0))  # Display the background image
    state_message = font.render(state_text, True, BLACK)
    line1_message = font.render(line1, True, BLACK)
    line2_message = font.render(line2, True, BLACK)

    # Position the messages
    screen.blit(state_message, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 100))  # Main message
    screen.blit(line1_message, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50))   # Line 1
    screen.blit(line2_message, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2))       # Line 2

    pygame.display.flip()

    # Wait for the player to press P to restart the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # Restart the game
                    level = 1  # Reset level
                    initialize_game()  # Reinitialize the game state
                    game_over = False  # Reset game_over
                    win_state = None  # Reset win_state
                    waiting = False  # Exit the loop

def end_game():
    """Transition to the final fight (Big Guy vs Blade Guy)."""
    global win_state, all_sprites, bubblesFalling, blades, fight_bubbles

    # Add a 200 milli second delay for the transition
    pygame.time.wait(200)

    show_pre_fight_screen()
    # Remove all bubbles and blades from the screen
    for bubble in bubblesFalling:
        bubble.kill()
    bubblesFalling.empty()

    for blade in blades:
        blade.kill()
    blades.empty()

    for fight_bubble in fight_bubbles:
        fight_bubble.kill()
    fight_bubbles.empty()

    # Transition to the final fight
    win_state = True
    all_sprites.remove(player)  # Remove the player from the game


# Game initialization
show_welcome_screen()
initialize_game()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == BUBBLE_EVENT and not game_over and win_state is None:
            x_position = random.randint(*allowed_spawn_areas[0])
            bubble = Bubble(x_position, 0)
            all_sprites.add(bubble)
            bubblesFalling.add(bubble)

    keys = pygame.key.get_pressed()

    if not game_over and win_state is None:
        # jump sound
        if keys[pygame.K_SPACE]:  # Check for spacebar key
            pygame.mixer.Sound.play(jumpSound)

        # Controls
        player.move(keys)
        # Update game state
        all_sprites.update()
        blades.update()  # Ensure blades are moving

        # Collision: player collects bubbles
        for collision in pygame.sprite.spritecollide(player, bubblesFalling, True):
            player.catchBubble()

        # Collision hit by blade
        # Collision: player gets hit by blades
        for collision in pygame.sprite.spritecollide(player, blades, True):
                result = player.handleHitByBlade(stop_game)
                if result == "lostBubble":
                    break  
                elif result == "lostHp":
                    pygame.mixer.Sound.play(ouchSound)
                else:
                    pygame.mixer.Sound.play(dieSound)  
                    stop_game()                       

        # Collision: blade hits a falling bubble
        for bubble in bubblesFalling:
            bladeCollisions = pygame.sprite.spritecollide(bubble, blades, True)
            if bladeCollisions:
                pygame.mixer.Sound.play(popSound)
                bubble.kill()  # Remove the bubble

        # Add bubbles holding in hand to "feed big guy", must be 2 bubbles
        if pygame.sprite.collide_rect(player, big_guy) and player.getBubblesHolding() == 2:
            score += player.getBubblesHolding() 
            if player.getBubblesHolding() > 0:
                big_guy.eat(score)
                pygame.mixer.Sound.play(disposeSound)
                player.clearBubblesFromHand()

        # Blade shooting from Blade Guy
        if random.random() < 0.02:
            blade = blade_guy.shoot_blade()
            all_sprites.add(blade)
            blades.add(blade)

        # Check win condition
        if score >= 1:  # Win condition for transition
            end_game()

    elif win_state:  # Final fight logic
        current_time = pygame.time.get_ticks()
        # Big Guy fight controls
        big_guy.move(keys)

        # Big Guy shooting bubbles
        if keys[pygame.K_x]:
            fight_bubble = big_guy.shoot_bubble(current_time)
            if fight_bubble:
                all_sprites.add(fight_bubble)
                fight_bubbles.add(fight_bubble)
        for bubble in fight_bubbles:
            bubble.update()
            if bubble.rect.right > SCREEN_WIDTH:  # Bubble went off-screen
                bubble.kill()
                big_guy.bubble_active = False        

        # BladeGuy shooting blades during boss fight
        if random.random() < 0.02:
            blade = blade_guy.shoot_blade()
            all_sprites.add(blade)
            blades.add(blade)

        # Update Blade Guy's behavior and projectiles only if Big Guy hasn't won
        if not game_over or win_state is None:
            blade_guy.update()
            blades.update()
            fight_bubbles.update()

        # Check collisions: Big Guy's bubbles hit Blade Guy
        for bubble in pygame.sprite.spritecollide(blade_guy, fight_bubbles, True):
            blade_guy.hp -= 1
            if blade_guy.hp <= 0:
                stop_game(True)  # Big Guy wins

        # Check collisions: Blade Guy's blades hit Big Guy
        for blade in pygame.sprite.spritecollide(big_guy, blades, True):
            big_guy.hp -= 1
            if big_guy.hp <= 0:
                stop_game(False)  # Blade Guy wins

    else:
        if keys[pygame.K_p]:
            initialize_game()
            
            
           

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Health bars
    if win_state:
        draw_hearts(screen, big_guy.hp, SCREEN_WIDTH - 780)
        draw_hearts(screen, blade_guy.hp, SCREEN_WIDTH - 120)
    else:
        draw_hearts(screen, player.hp, SCREEN_WIDTH - 120)

    # UI Elements
    if game_over:
        stop_game(win_state)
    elif win_state is None:
        score_text = font.render(f"SCORE: {score}", True, BLACK)
        temp_bubblesHolding = font.render(f"You are holding: {player.getBubblesHolding()} bubbles", True, BLACK)
        screen.blit(score_text, (10, 50))
        screen.blit(temp_bubblesHolding, (10, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
