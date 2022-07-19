def instruction(credit, num_range):
    res = 'the result is a'
    message = f'''
        
        Bet and spin to hit a satisfying DOUBLE, TWIN SIDE and JACKPOT!
        
        Rules:
        Select or bet a number 1 - {num_range}.
        You have ${credit} to play.
        Every turn, your cash will get deducted by $10.
        Last printed numbers in the pool is the result
        Two result indicator are provided.
        Spin result and bet result.
        If your cash goes $0, the game is over,
        and new starting cash will be offered.
        
        Rewards:
        NONE      \t- rewards you nothing.
        ONE MATCH \t- returns back your $10.
        DOUBLE    \t- 2x your bet, plus $10 return.
        TWIN SIDE \t- 5x your bet, plus $10 return.
        JACKPOT   \t- 10x your bet, plus $10 return.
        
        Results:
        NONE      \t- none of the numbers match your bet.
        ONE MATCH \t- single number that matches your bet.
        DOUBLE→   \t- {res} pair of number on right side.
        DOUBLE←   \t- {res} pair of number on left side.
        TWIN↔SIDE \t- {res} pair of number on both side.
        JACKPOT   \t- {res} triple match number.
        NOJACKPOT \t- {res} triple match number but didn't match your bet.
        
        Notes:
        Cash and pool range will auto update based on user settings.
        You can interrupt the spin by hitting any key in the keyboard.
        For more info, you can read current status and logs in advance settings.

        Have fun!'''
    return message


def main_menu_inst():
    message = '''
        
        Menu:
        
        "ENTER" start
        "Q" exit
        "H" help
        "A" advance settings
        "R" restart/reset all settings to default
        
        ››› '''
    return message


def spin_delay_inst():
    message = '''
        
        Spin delay settings:
        
        By default, spin delay is dynamic or random.
        You can set a static delay in seconds or milliseconds.
        To restore default spin delay, set it to "-1".
        (Spin delay example 0.1, 0.3, 0.7, 1 etc.)'''
    return message


def spin_range_inst():
    message = '''
        
        Spin range settings:
        
        Spin range default is "28".
        High value can cause a higher chance of long spin duration.'''
    return message


def spin_range_prompt(spin_range):
    message = f'''
        Spin range must be 28 and below.
        Spin range ceiling "{spin_range}" can cause a higher chance of long spin duration.
        
        Proceed anyway? y/n
        
        ››› '''
    return message


def num_range_inst():
    message = '''
        
        Pool range settings:
        
        Type a number range 3 - 9.
        (Example: "5"). Now, numbers 1 - 5 will be in the pool.'''
    return message


def advance_setting_inst():
    message = '''
        
        Advance settings:
        
        "D" spin delay
        "R" spin range
        "P" pool range
        "C" countdown
        "A" loading animation
        "T" read status
        "L" read logs
        "S" save cash and settings'''
    return message


def quit_continue_inst():
    message = '''
        
        "ENTER" continue "Q" exit.
        
        ››› '''
    return message


def status(credit, spin_range, pool, delay, countdown, animation, win_rate, total_spin):
    time = ' sec'
    if delay == -1:
        def_val = 'default'
        delay = ''
        time = ''
    else:
        def_val = ''
    if countdown == 1:
        cd_stat = 'ON'
    else:
        cd_stat = 'OFF'
    if animation == 1:
        anim_stat = 'Disc'
    else:
        anim_stat = 'Box'

    message = f'''
        
        Status:
        
        Cash:             \t${credit}
        Spin range:       \t1 - {spin_range} ticks
        Spin delay:       \t{delay}{time}{def_val}
        Pool range:       \tnumbers 1 - {pool}
        Countdown:        \t{cd_stat}
        Loading animation:\t{anim_stat}
        Total spin:       \t{total_spin}
        Win rate:         \t{win_rate}%'''
    return message


def warning():
    message = '----------------------------------------------------------------------\n' \
              'Modifying this file can cause an error when opening Flutter-Spin.py\n' \
              'So don\'t modify this unless you know what this thing is...      :p\n'
    return message
