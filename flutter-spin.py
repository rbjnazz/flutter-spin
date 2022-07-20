# This is my first python program.
# Initially those class variables are global statements (they say globals are evil) so I put it inside class.
# Still don't know how to manipulate the values of a variable within different functions.
# Seems like class variables act like globals.

import random
import sys
from time import sleep, time
import os
from math import ceil


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')  # windows
    else:
        os.system('clear')


def error(tb, f, ext):
    message = f'''

            System message: {tb}

            missing or deleted file >>> {f}{ext}

            Press any key to exit...'''
    return message


# if something messed up
try:
    from misc import info, jack
except ModuleNotFoundError:
    clear_terminal()
    trace_back = sys.exc_info()[1]
    tb_list = str(trace_back).split(' ')
    file = tb_list[3].replace("'", '')
    input(error(trace_back, file, ' folder'))
    exit()
except ImportError:
    info = None
    jack = None
    if info or jack:
        from misc import info, jack
    else:
        clear_terminal()
        trace_back = sys.exc_info()[1]
        tb_list = str(trace_back).split(' ')
        file = tb_list[3].replace("'", '')
        input(error(trace_back, file, '.py'))
        exit()
else:
    pass

TIME = 1
SPACE_A = 21 * ' '  # just to save some time aligning things
SPACE_B = 13 * ' '
LINES = f'{SPACE_A}―――――――――――――'
INVALID = '\n\tInvalid command!'
PRESS_ENTER = '\n\n\t‹‹‹ "ENTER" to go back\n\t››› '


# here comes the clunky code! good luck reading it
class Bucks:
    self = 50
    spin_point = 0
    result_indicator = 0
    spin_loss = 0

    @staticmethod
    def add_bucks():
        gen = NumGenerator
        bet = UserBet.self
        if gen.num_a == gen.num_b == bet and bet != gen.num_c:
            Bucks.self += 30
            Bucks.result_indicator = 0
            Bucks.spin_point += 1
        elif gen.num_b == gen.num_c == bet and bet != gen.num_a:
            Bucks.self += 30
            Bucks.result_indicator = 1
            Bucks.spin_point += 1
        elif gen.num_c == gen.num_a == bet and bet != gen.num_b:
            Bucks.self += 60
            Bucks.result_indicator = 2
            Bucks.spin_point += 1
        elif gen.num_a == gen.num_b == gen.num_c == bet:
            Bucks.self += 110
            Bucks.result_indicator = 3
            Bucks.spin_point += 1
            sleep(1)
            jackpot()
        elif bet in (gen.num_a, gen.num_b, gen.num_c):
            Bucks.self += 10
            Bucks.result_indicator = 5
            Bucks.spin_point += 1
        else:
            Bucks.spin_loss += 1
            Bucks.result_indicator = 6


class UserBet:
    self = 0

    @staticmethod
    def set_bet():
        clear_terminal()
        user = input(f'\n\n\tCash ${Bucks.self}\n\tSelect a number'
                     f'\t{UserBet.pool_range_preview(UserNumRange.self)}'
                     f' 1 - {UserNumRange.self}{PRESS_ENTER.replace("to go back", "menu")}')
        # prompts when you bet
        try:
            if user == '':
                clear_menu()
            elif int(user) in range(1, 10):
                int_user = int(user)
                if int_user > UserNumRange.self:
                    print(f'\n\tPool range ceiling is "{UserNumRange.self}" please select a number accordingly.')
                    sleep(2)
                    UserBet.set_bet()
                UserBet.self = int_user
                print(f'\n\tPlacing "{int_user}" please wait...\n\n')
                sleep(1.5)
                clear_terminal()
                Bucks.self -= 10
                print(f'{SPACE_B + 3 * " "}Your cash is now ${Bucks.self}\n')
                sleep(1)
                if UserCountDown.self == 1:
                    UserCountDown.countdown()
                elif UserCountDown.self == 2:
                    NumGenerator.num_spinner()
            else:
                print(f'\n\t"{user}" is not part of the pool.')
                sleep(TIME)
                UserBet.set_bet()
        except ValueError:
            print(f'{INVALID} "{user}" expected a number.')
            sleep(TIME)
            UserBet.set_bet()

    @staticmethod
    def pool_range_preview(num_range):  # to update pool range preview
        sequence = [
            '│ ❶ │ ② │ ❸ │',
            '│ ❶ │ ② │ ❸ │ ④ │',
            '│ ❶ │ ② │ ❸ │ ④ │ ❺ │',
            '│ ❶ │ ② │ ❸ │ ④ │ ❺ │ ⑥ │',
            '│ ❶ │ ② │ ❸ │ ④ │ ❺ │ ⑥ │ ❼ │',
            '│ ❶ │ ② │ ❸ │ ④ │ ❺ │ ⑥ │ ❼ │ ⑧ │',
            '│ ❶ │ ② │ ❸ │ ④ │ ❺ │ ⑥ │ ❼ │ ⑧ │ ❾ │'
        ]
        if num_range < 3 or num_range > 9:  # if you try to modify the pool range inside settings.log
            print(f'\n\n\tInvalid pool range settings! "1 - {num_range}"')
            sleep(3)
            restart()
        else:
            return sequence[num_range - 3]


class NumGenerator:
    num_a, num_b, num_c, = 0, 0, 0
    spin_count = 0
    turn = 0
    random_time = 0.1

    @staticmethod
    def num_generator():  # this prints the random numbers
        gen = NumGenerator
        r = random.randint(0, 6)
        slot_a = random.randint(1, UserNumRange.self)
        slot_b = random.randint(1, UserNumRange.self)
        slot_c = random.randint(1, UserNumRange.self)
        colon_wing_l = gen.wing_colon(gen.spin_count, UserSpinRange.self, True)
        colon_wing_r = gen.wing_colon(gen.spin_count, UserSpinRange.self, False)
        arrow_wing_l = gen.wing_arrow(gen.spin_count, UserSpinRange.self, True)
        arrow_wing_r = gen.wing_arrow(gen.spin_count, UserSpinRange.self, False)
        # my initial approach is to print the numbers plainly.
        sequence = [  # but this can do some animation
            f'│ {slot_a} │ - │ - │', f'│ - │ {slot_b} │ - │', f'│ - │ - │ {slot_c} │',
            f'│ {slot_a} │ {slot_b} │ - │', f'│ - │ {slot_b} │ {slot_c} │', f'│ {slot_a} │ - │ {slot_c} │',
            f'│ {slot_a} │ {slot_b} │ {slot_c} │',
        ]
        print(f'{LINES}\n{SPACE_B}{arrow_wing_l}{colon_wing_l}'
              f'{sequence[r]}{colon_wing_r}{arrow_wing_r}\n{LINES}')
        gen.num_a, gen.num_b, gen.num_c = slot_a, slot_b, slot_c

    @staticmethod
    def num_spinner():  # spins here
        clear_terminal()
        spinner_count = 0
        spin_range = random.randint(1, UserSpinRange.self)
        while spinner_count != spin_range:
            random_time = random.uniform(0.1, 0.5)
            print(6 * '\n')
            if UserAnim.self == 1:
                print(UserAnim.loading_anim(NumGenerator.spin_count, spin_range))
            elif UserAnim.self == 2:
                print(UserAnim.loading_anim(NumGenerator.spin_count, spin_range))
            NumGenerator.num_generator()  # calling this function to print the numbers
            NumGenerator.random_time = random_time
            spinner_count += 1
            NumGenerator.spin_count = spinner_count
            if UserSpinDelay.self == -1:
                sleep(random_time)
            else:
                sleep(UserSpinDelay.self)
            clear_terminal()  # I had so much headache thinking how to animate the spin. Then a simple solution.
        NumGenerator.turn += 1
        NumGenerator.mark_hidden()
        ResultAnim.result()

    @staticmethod
    def mark_hidden():  # hides the number before it gets revealed
        sequence = [
            '│   │   │   │', '│ ? │   │   │', '│   │ ? │   │', '│   │   │ ? │',
            '│ ? │ ? │   │', '│   │ ? │ ? │', '│ ? │   │ ? │', '│ ? │ ? │ ? │'
        ]
        x = 4
        while x != 0:
            clear_terminal()
            r = random.randint(0, 7)
            print(8 * '\n' + f'{LINES}\n{SPACE_B + 3 * " "}:::::{sequence[r]}:::::\n{LINES}')
            sleep(0.1)
            x -= 1
        clear_terminal()
        print(8 * '\n' + f'{LINES}\n{SPACE_B + 3 * " "}:::::│ ? │ ? │ ? │:::::\n{LINES}')
        sleep(0.5)

    @staticmethod
    def wing_arrow(spin_count, duration, is_reversed):  # just for eye candy
        sequence = [
                       '   ', '›  ', ' › ', '  ›'
                   ] * ceil((duration + 1) / 4)
        sequence_reversed = [
                                '   ', '  ‹', ' ‹ ', '‹  '
                            ] * ceil((duration + 1) / 4)
        if not is_reversed:
            return sequence[spin_count]
        else:
            return sequence_reversed[spin_count]

    @staticmethod
    def wing_colon(spin_count, duration, is_reversed):  # more eye candy
        sequence = [
                       '     ', '     ', '     ', ':    ', '::   ', ':::  ', ':::: ', ':::::'
                   ] * ceil((duration + 1) / 8)
        sequence_reversed = [
                                '     ', '     ', '     ', '    :', '   ::', '  :::', ' ::::', ':::::'
                            ] * ceil((duration + 1) / 8)
        if not is_reversed:
            return sequence[spin_count]
        else:
            return sequence_reversed[spin_count]


class UserNumRange:
    self = 9

    @staticmethod
    def set_num_range():
        clear_terminal()
        user = input(f'{info.num_range_inst()}{PRESS_ENTER}')
        # I just realize that it will take forever to hit the JACKPOT so I can go lower to 3
        if user == '':
            advance_settings()
        elif user.isnumeric():
            int_user = int(user)
            if int_user >= 10:
                print(f'\n\tPool range must be 9 and below. got "{int_user}"')
                sleep(TIME)
                UserNumRange.set_num_range()
            elif int_user > 2:
                UserNumRange.self = int_user
                print(f'\n\tPool range is set to "{int_user}"')
                sleep_advance()
            elif int_user <= 2:
                print(f'\n\tPool range must be 3 and above. got "{int_user}"')
                sleep(TIME)
                UserNumRange.set_num_range()
        else:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            UserNumRange.set_num_range()


class UserSpinRange:
    self = 28

    @staticmethod
    def set_spin_range():
        clear_terminal()
        user = input(f'{info.spin_range_inst()}{PRESS_ENTER}')
        if user == '':
            advance_settings()
        elif user.isnumeric():
            int_spin_r = int(user)
            if int_spin_r <= 9:
                print(f'\n\tSpin range must be 10 and above. got "{int_spin_r}"')
                sleep(TIME)
                UserSpinRange.set_spin_range()
            elif int_spin_r > 28:
                user = input(f'{info.spin_range_prompt(int_spin_r)}')
                if user.upper() == 'Y':
                    UserSpinRange.self = int_spin_r
                    print(f'\n\tSpin range is set to "{int_spin_r}"')
                    sleep_advance()
                else:
                    UserSpinRange.set_spin_range()
            elif int_spin_r > 9:
                UserSpinRange.self = int_spin_r
                print(f'\n\tSpin range is set to "{int_spin_r}"')
                sleep_advance()
        else:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            UserSpinRange.set_spin_range()


class UserSpinDelay:
    self = -1

    @staticmethod
    def set_delay():  # best spin delay setting is 0.1
        clear_terminal()
        user = input(f'{info.spin_delay_inst()}{PRESS_ENTER}')
        if user == '':
            advance_settings()
        try:
            float_user = float(user)
            if float_user > 2:
                user = input(f'\n\t"{float_user}" seconds is time-consuming.'
                             f'\n\n\tProceed anyway? y/n\n\n\t››› ')
                if user.upper() == 'Y':
                    print(f'\n\tSpin delay is set to "{float_user}" sec')
                    UserSpinDelay.self = float_user
                    sleep_advance()
                else:
                    UserSpinDelay.set_delay()
            elif float_user == -1:
                print('\n\tSpin delay is set to default')
                UserSpinDelay.self = float_user
                sleep_advance()
            elif float_user < -1:
                print(f'{INVALID} "{user}"')
                sleep(TIME)
                UserSpinDelay.set_delay()
            elif float_user <= 2:
                print(f'\n\tSpin delay is set to "{float_user}" sec')
                UserSpinDelay.self = float_user
                sleep_advance()
            else:
                print(f'{INVALID} "{user}"')
                sleep(TIME)
                UserSpinDelay.set_delay()
        except ValueError:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            UserSpinDelay.set_delay()


class UserCountDown:
    self = 1

    @staticmethod
    def countdown():  # just trying to count
        clear_terminal()
        print(9 * '\n' + f'{SPACE_A} Starting in')
        sleep(1)
        count_start = 3
        clear_terminal()
        while count_start > 0:
            print(9 * '\n' + f'{SPACE_A + 6 * " "}{count_start}')
            count_start += - 1
            sleep(1)
            clear_terminal()
        NumGenerator.num_spinner()

    @staticmethod
    def set_countdown():
        prompt = '\n\n\tCountdown settings:\n\n\tType "1" to set the countdown timer ON or "2" OFF.'
        if_one = '\n\tCountdown ON.'
        if_two = '\n\tCountdown OFF.'
        UserCountDown.self = two_prompt(prompt, if_one, if_two, UserCountDown.set_countdown)
        sleep_advance()


class UserAnim:
    self = 1

    @staticmethod
    def set_load_anim():
        prompt = '\n\n\tLoading animation settings:\n\n\tType "1" disc or "2" box.'
        if_one = '\n\tLoading animation is set to disc'
        if_two = '\n\tLoading animation is set to box.'
        UserAnim.self = two_prompt(prompt, if_one, if_two, UserAnim.set_load_anim)
        sleep_advance()

    @staticmethod
    def loading_anim(spin_count, duration):  # the previous version of this is 17 lines of code
        disc = [
                   f'{SPACE_A}  ○ ○ ○ ○ ○', f'{SPACE_A}  ● ○ ○ ○ ○',
                   f'{SPACE_A}  ○ ● ○ ○ ○', f'{SPACE_A}  ○ ○ ● ○ ○',
                   f'{SPACE_A}  ○ ○ ○ ● ○', f'{SPACE_A}  ○ ○ ○ ○ ●'
               ] * ceil((duration + 1) / 6)  # just trying to match this to the length of spin range
        box = [
                  f'{SPACE_A}  □ □ □ □ □', f'{SPACE_A}  ▪ □ □ □ □',
                  f'{SPACE_A}  □ ▪ □ □ □', f'{SPACE_A}  □ □ ▪ □ □',
                  f'{SPACE_A}  □ □ □ ▪ □', f'{SPACE_A}  □ □ □ □ ▪'
              ] * ceil((duration + 1) / 6)
        if UserAnim.self == 1:
            return disc[spin_count]
        elif UserAnim.self == 2:
            return box[spin_count]
        else:
            pass


class ResultAnim:
    self = 0
    spin_indicator = 0

    @staticmethod
    def spin_result():
        gen = NumGenerator
        res = [' DOUBLE← ', ' DOUBLE→ ', 'TWIN↔SIDE', ' JACKPOT ', 'NOJACKPOT', 'ONE MATCH', '  NONE!  ']
        if gen.num_a == gen.num_b != gen.num_c:
            ResultAnim.spin_indicator = 0
            return f'{SPACE_B + 8 * " "}│ {res[0]} │\n{LINES}'
        elif gen.num_b == gen.num_c != gen.num_a:
            ResultAnim.spin_indicator = 1
            return f'{SPACE_B + 8 * " "}│ {res[1]} │\n{LINES}'
        elif gen.num_c == gen.num_a != gen.num_b:
            ResultAnim.spin_indicator = 2
            return f'{SPACE_B + 8 * " "}│ {res[2]} │\n{LINES}'
        elif gen.num_a == gen.num_b == gen.num_c == UserBet.self:
            ResultAnim.spin_indicator = 3
            return f'{SPACE_B + 8 * " "}│ {res[3]} │\n{LINES}'
        elif gen.num_a == gen.num_b == gen.num_c and UserBet.self not in (gen.num_a, gen.num_b, gen.num_c):
            ResultAnim.spin_indicator = 4
            return f'{SPACE_B + 8 * " "}│ {res[4]} │\n{LINES}'
        elif UserBet.self in (gen.num_a, gen.num_b, gen.num_c):
            ResultAnim.spin_indicator = 5
            return f'{SPACE_B + 8 * " "}│ {res[5]} │\n{LINES}'
        else:
            ResultAnim.spin_indicator = 6
            return f'{SPACE_B + 8 * " "}│ {res[6]} │\n{LINES}'

    @staticmethod
    def full_slot(bet, bet_result):
        wr = ResultAnim.wing_result
        wr_right = wr(False)
        wr_left = wr(True)
        wr_right_v2 = wr(False)
        wr_left_v2 = wr(True)
        slot = f'{SPACE_A[:-5]}{wr_left}│   {bet} GOT   │{wr_right}\n' \
               f'{SPACE_A[:-5]}{wr_left_v2}│ {bet_result} │{wr_right_v2}\n{LINES}'
        return slot

    @staticmethod
    def result():
        bet = UserBet.self
        gen = NumGenerator
        ResultAnim.self = 5  # prints the result 5 times just to show the glitch effect... lol
        while ResultAnim.self != 0:
            clear_terminal()
            spin_res = ResultAnim.spin_result()
            fs = ResultAnim.full_slot
            new_line = 8 * '\n'
            slots = f'{new_line}{LINES}\n{SPACE_B + 3 * " "}' \
                    f':::::│ {gen.num_a} │ {gen.num_b} │ {gen.num_c} │:::::\n{LINES}'
            res = [' DOUBLE← ', ' DOUBLE→ ', 'TWIN↔SIDE', ' JACKPOT ', 'NOJACKPOT', 'ONE MATCH', '  NONE!  ']
            if gen.num_a == gen.num_b == bet and bet != gen.num_c:
                print(f'{slots}\n{spin_res}\n{fs(bet, res[0])}')
            elif gen.num_b == gen.num_c == bet and bet != gen.num_a:
                print(f'{slots}\n{spin_res}\n{fs(bet, res[1])}')
            elif gen.num_c == gen.num_a == bet and bet != gen.num_b:
                print(f'{slots}\n{spin_res}\n{fs(bet, res[2])}')
            elif gen.num_a == gen.num_b == gen.num_c == bet:
                print(f'{slots}\n{spin_res}\n{fs(bet, res[3])}')
            elif gen.num_a == gen.num_b == gen.num_c and bet not in (gen.num_a, gen.num_b, gen.num_c):
                print(f'{slots}\n{spin_res}\n{fs(bet, res[6])}')
                Bucks.result_indicator = 4
            elif bet in (gen.num_a, gen.num_b, gen.num_c):
                print(f'{slots}\n{spin_res}\n{fs(bet, res[5])}')
            else:
                print(f'{slots}\n{spin_res}\n{fs(bet, res[6])}')
            sleep(random.uniform(0.0, 0.3))
            ResultAnim.self -= 1
        Bucks.add_bucks()
        LogReport.logs()
        quit_continue()

    @staticmethod
    def wing_result(is_reversed):  # some glitters
        if ResultAnim.self == 1:
            r = 0
        else:
            r = random.randint(0, 5)
        sequence = [
            '     ', '+    ', ' +   ', '  +  ', '   + ', '    +'
        ]
        sequence_reversed = [
            '     ', '     +', '   + ', '  +  ', ' +    ', '+   '
        ]
        if not is_reversed:
            return sequence[r]
        else:
            return sequence_reversed[r]


class LogReport:
    parts = 0  # divides logs by parts

    @staticmethod
    def logs():
        gen = NumGenerator
        if gen.turn == 1:
            LogReport.parts += 1
            with open('misc/logs.log', mode='w', encoding='utf-8') as log:
                log.write(f'\n\n\tSpin history:\n\n\t{26 * "―"}   PART {LogReport.parts:02}')
        else:
            pass
        res = [' DOUBLE← ', ' DOUBLE→ ', 'TWIN↔SIDE', ' JACKPOT ', 'NOJACKPOT', 'ONE MATCH', '  NONE!  ']
        div = ''
        wr = ''
        if Bucks.self >= 100:
            credit_space = 4 * ' '
        elif Bucks.self == 0:
            LogReport.parts += 1
            credit_space = 6 * ' '
            div = f'{26 * "―"}   PART {LogReport.parts:02}'
        else:
            credit_space = 5 * ' '
            div = ''
        if Bucks.self >= 1000:
            credit_space = 3 * ' '
            wr = 'World record!'
        if gen.turn >= 100:
            spin_dash = 16
        else:
            spin_dash = 17
        log_result = f'''
        \t{LINES[3:]}
        Spin {gen.turn:02} {spin_dash * "-"} │ {gen.num_a} │ {gen.num_b} │ {gen.num_c} │
        Selected number {9 * "-"} │     {UserBet.self}     │ 
        Spin result {13 * "-"} │ {res[ResultAnim.spin_indicator]} │
        Bet result {14 * "-"} │ {res[Bucks.result_indicator]} │
        Cash {20 * "-"} │   ${Bucks.self}{credit_space}│ {wr}
        \t{LINES[3:]}
        {div}'''
        with open('misc/logs.log', mode='a', encoding='utf-8') as logger:
            logger.write(log_result)


    @staticmethod
    def read_logs():
        clear_terminal()
        with open('misc/logs.log', mode='r', encoding='utf-8') as logger:
            log = logger.read()
            user = input(f'{log}{PRESS_ENTER}')
        if user == '':
            advance_settings()
        else:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            LogReport.read_logs()

    @staticmethod
    def status():
        clear_terminal()
        try:
            spin_total = Bucks.spin_point / (Bucks.spin_point + Bucks.spin_loss)
            win_rate = int(spin_total * 100)  # calculate win rate percentage. doesn't include interrupted spin.
        except ZeroDivisionError:
            win_rate = 0
            pass
        stats = info.status(
            Bucks.self, UserSpinRange.self, UserNumRange.self, UserSpinDelay.self,
            UserCountDown.self, UserAnim.self, win_rate, NumGenerator.turn
        )
        user = input(f'{stats}{PRESS_ENTER}')
        if user == '':
            advance_settings()
        else:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            LogReport.status()


def two_prompt(prompt_input, if_one, if_two, back_self):  # used by countdown() and loading_anim()
    clear_terminal()
    user = input(f'{prompt_input}{PRESS_ENTER}')
    if user == '':
        advance_settings()
    try:
        int_user = int(user)
        if int_user == 1:
            print(if_one)
            return int_user
        elif int_user == 2:
            print(if_two)
            return int_user
        else:
            print(f'{INVALID} "{user}"')
            sleep(TIME)
            return back_self()
    except ValueError:
        print(f'{INVALID} "{user}"')
        sleep(TIME)
        return back_self()


def main_menu():
    user_init = input(info.main_menu_inst())
    if user_init.upper() == 'Q':
        print('\n\tClosing...')
        sleep(1.5)
        exit()
    elif user_init == '':
        clear_terminal()
        UserBet.set_bet()
    elif user_init.upper() == 'H':
        instruction()
    elif user_init.upper() == 'A':
        advance_settings()
    elif user_init.upper() == 'R':
        user = input('\n\tRestart and reset? y/n\n\n\t››› ')
        if user.upper() == 'Y':
            restart()
        else:
            clear_menu()
    elif not user_init.isnumeric():
        print(f'{INVALID} "{user_init}"')
        sleep(TIME)
        clear_menu()
    else:
        print('\n\tPress "ENTER" before you bet.')
        sleep(TIME)
        clear_menu()


def clear_menu():
    clear_terminal()
    main_menu()


def sleep_advance():
    sleep(TIME)
    advance_settings()


def advance_settings():  # previous version is 23 lines of code using if statements
    clear_terminal()
    user = input(f'{info.advance_setting_inst()}{PRESS_ENTER}')
    keys = {
        '': clear_menu, 'D': UserSpinDelay.set_delay, 'R': UserSpinRange.set_spin_range,
        'P': UserNumRange.set_num_range, 'C': UserCountDown.set_countdown, 'A': UserAnim.set_load_anim,
        'S': save_settings, 'T': LogReport.status, 'L': LogReport.read_logs
    }
    try:
        func = keys.get(user.upper())
        return func()
    except TypeError:
        print(f'{INVALID} "{user}"')
        sleep_advance()


def typing_anim(load):
    string = load
    default_delay = NumGenerator.random_time  # sys.stdout ignore the 20 digit float
    user_delay = UserSpinDelay.self

    for char in string:
        if UserSpinDelay.self == -1:
            sleep(default_delay)
            print(string)
        else:
            sleep(user_delay)
            print(string)


def instruction():
    clear_terminal()
    print(info.instruction(Bucks.self, UserNumRange.self))
    user = input(PRESS_ENTER)
    if user == '':
        clear_menu()
    else:
        print(f'{INVALID} "{user}"')
        sleep(TIME)
        clear_terminal()
        instruction_loop()


def instruction_loop():
    clear_terminal()
    print(info.instruction(Bucks.self, UserNumRange.self))
    user = input(PRESS_ENTER)
    if user == '':
        clear_menu()
    else:
        print(f'{INVALID} "{user}"')
        sleep(TIME)
        clear_terminal()
        instruction_loop()


def save_settings():  # user settings
    settings = f'range\n{UserNumRange.self}\ndelay\n{UserSpinDelay.self}\n' \
               f'countdown\n{UserCountDown.self}\nanimation\n{UserAnim.self}\n' \
               f'earned\n{Bucks.self}\nspin\n{UserSpinRange.self}\n\n{info.warning()}'
    with open('misc/settings.log', mode='w', encoding='utf-8') as log:
        log.write(settings)
    print('\n\tSaving...')
    sleep(1.5)
    clear_terminal()
    advance_settings()


def load_settings():  # this will always load saved user settings
    try:
        with open('misc/settings.log', mode='r', encoding='utf-8') as setting:
            set_to_line = setting.readlines()
            UserNumRange.self = int(set_to_line[1])
            UserSpinDelay.self = float(set_to_line[3])
            UserCountDown.self = int(set_to_line[5])
            UserAnim.self = int(set_to_line[7])
            Bucks.self = int(set_to_line[9])
            UserSpinRange.self = int(set_to_line[11])
            print('\n\n\tLoading settings...')
            sleep(1)
            clear_terminal()
    except FileNotFoundError:  # if you try to delete settings.log it will create a new one via restart function :p
        print('\n\n\tUser setting is missing or had been deleted')
        sleep(2)
        clear_terminal()
        typing_anim('\n\n\t..........')
        clear_terminal()
        restart()
    with open('misc/logs.log', mode='w', encoding='utf-8') as log:
        log.write(f'\n\n\tSpin history: empty\n\t{39 * "―"}')


def restart():  # Initializes all default values.
    clear_terminal()
    UserNumRange.self = 9
    UserSpinDelay.self = -1
    UserSpinRange.self = 28
    UserCountDown.self = 1
    UserAnim.self = 1
    Bucks.self = 50
    Bucks.result_indicator = 0
    Bucks.spin_point = 0
    Bucks.spin_loss = 0
    ResultAnim.spin_indicator = 0
    NumGenerator.turn = 0
    settings = f'range\n{UserNumRange.self}\ndelay\n{UserSpinDelay.self}\n' \
               f'countdown\n{UserCountDown.self}\nanimation\n{UserAnim.self}\n' \
               f'earned\n{Bucks.self}\nspin\n{UserSpinRange.self}\n\n{info.warning()}'
    with open('misc/settings.log', mode='w', encoding='utf-8') as log:
        log.write(settings)
    with open('misc/logs.log', mode='w', encoding='utf-8') as log:
        log.write(f'\n\n\tSpin history: empty\n\t{39 * "―"}')
    print('\n\n\tReverting all settings to default...')
    sleep(3)
    clear_terminal()
    print('\n\n\tWelcome to Flutter Spin!')
    main_menu()


def quit_continue():
    NumGenerator.spin_count = 0  # Refresh the loading animation
    # offering some random cash even the game is over
    if Bucks.self == 0:
        print(f'\n\n{SPACE_A[:-3]}You have $0 cash!')
        sleep(1)
        print(f'{SPACE_A}  GAME OVER')
        user = input('\n\tNeed more cash? y/n\n\t››› ')
        if user.upper() == "Y":
            Bucks.self = random.randrange(10, 200, 10)
            if Bucks.self >= 100:
                clear_terminal()
                print(f'\n\n\t${Bucks.self} should be a great start right? Go on and play more!')
                sleep(1)
            else:
                clear_terminal()
                print(f'\n\n\tJust ${Bucks.self} for now. I\'ll give you more later.')
                sleep(1)
        elif user.upper() == 'N':
            print(f'{SPACE_A}Offer rejected')
            sleep(1)
            print(f'{SPACE_A}  GAME OVER')
            sleep(TIME)
            exit()
        else:
            print(f'{INVALID} "{user}"\n')
            sleep(TIME)
            clear_terminal()
            quit_continue()
    user = input(info.quit_continue_inst())
    if user.upper() == 'Q':
        quit_prompt()
    elif user == '':
        clear_terminal()
        UserBet.set_bet()
    else:
        print(f'{INVALID} "{user}"')
        sleep(TIME)
        clear_terminal()
        quit_continue()


def quit_prompt():
    clear_terminal()
    user = input('\n\n\tProceed? y/n\n\n\t››› ')
    if user.upper() == 'Y':
        clear_terminal()
        print('\n\n\tIf you\'re bored just play this game again.')
        sleep(TIME)
        print('\n\tThank you\n')
        sleep(1)
        exit()
    elif user.upper() == 'N':
        UserBet.set_bet()
    else:
        print(f'{INVALID} "{user}"')
        sleep(TIME)
        quit_continue()


def jackpot():  # when you hit it. This is the message :D
    sleep(TIME)
    typing_anim(jack.jackpot())
    quit_continue()


clear_terminal()
load_settings()
print('\n\n\tWelcome to Flutter Spin!')
main_menu()
