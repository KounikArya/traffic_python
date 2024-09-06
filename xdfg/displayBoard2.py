import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 60)

# Function to generate traffic data for one lane
def generate_traffic_data():
    return random.randint(10, 100)  # Random number of cars between 10 and 100

# Function to display traffic status
def display_traffic_status(num_cars):
    screen.fill(WHITE)  # Clear the screen with a white background
    
    # Determine traffic status
    if num_cars > 50:
        status = "Jam Ahead"
        color = RED
    else:
        status = "No Traffic"
        color = GREEN

    # Render the text and display it on the screen
    text = font.render(f"{status} ({num_cars} cars)", True, color)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    last_update_time = time.time()
    update_interval = 2  # Update every 5 seconds

    # Initial traffic data
    num_cars = generate_traffic_data()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update traffic data every 5 seconds
        if time.time() - last_update_time >= update_interval:
            num_cars = generate_traffic_data()
            last_update_time = time.time()

        # Display the current traffic status
        display_traffic_status(num_cars)

        # Limit to 30 frames per second
        clock.tick(30)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
