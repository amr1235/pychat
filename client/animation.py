from lib import simulate_delay

def clear_line():
    """Removes current line in the console.
    """    
    print("\033[2K\033[1G", flush=True, end="")

def animate_typing():
    """Animate loading using 3 dots.
    """    
    for _ in range (0,3):  
        simulate_delay(0.3)
        print('.', end="", flush=True)
    simulate_delay(0.3)
    clear_line()
