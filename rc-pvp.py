import datetime
from common import *
from imagesearch import *

IMAGES_PRIO_SORTED = [
    'resources/pvp_start.png',  # rumble
    'resources/victory.png',  # lol win
    'resources/cont.png',  # continue
    'resources/ok.png',  # error
    'resources/lvlup.png',  # level up
    'resources/claim_big.png',  # claim big lvlup
    'resources/pvp.png',  # rumble
]


def main():
    if not validate_resources(IMAGES_PRIO_SORTED):
        return -1

    stats = {}
    time_start = datetime.datetime.now()
    last = 'last'
    while True:
        wait_random()
        elapsed = datetime.datetime.now() - time_start
        res = find_prio_click(IMAGES_PRIO_SORTED)
        btn = 'none'
        if 'btn' in res.keys():
            btn = res['btn']

        in_game = in_active_game()

        if in_game:
            drag()

        if 'loc' in res.keys():
            if btn in stats.keys():
                if last != btn:
                    stats[btn] = stats[btn] + 1
            else:
                stats[btn] = 1

            if btn == 'pvp_start.png':
                rnd = random.randint(0, 2)
                offset = [0, 0, 0]
                location = [res['loc'][0] - offset[rnd], res['loc'][1] - 200]
                click(location)
                wait_random()
                click(res['loc'])
            else:
                click(res['loc'])

        played = get_stat('pvp_start.png', stats)
        level_ups = get_stat('lvlup.png', stats)
        errors = get_stat('ok.png', stats)
        win = get_stat('victory.png', stats)

        print(f'({str(in_game)[0]}) played: {played} elapsed: {pretty_print(elapsed)} '
              f' win: {win} lvl: {level_ups} e: {errors} '
              f'btn: {btn}', end='\r')

        last = btn


def no_more_quests():
    return imagesearch('resources/quest_block.png')[0] > 0


def get_stat(key, stats):
    if key in stats.keys():
        return stats[key]
    return 0


def pretty_print(elapsed):
    return str(datetime.timedelta(seconds=elapsed.total_seconds()))


def in_active_game():
    return imagesearch('resources/game_border.png')[0] > 0


def find_gold():
    # prio 1 gold units :)
    loc = imagesearch(f'resources/1_gold.png')
    if found(loc):
        return loc

    cnt = 0
    while True:
        cnt = cnt + 1
        i = random.randint(2, 5)
        loc = imagesearch(f'resources/{i}_gold.png')
        if found(loc):
            return loc
        if cnt > 100:
            return [10, 10]


def drag():
    gold_loc = find_gold()
    if gold_loc[0] == 10 and gold_loc[1] == 10:
        return
    drag_offset_x = random.randint(-100, 0)
    drag_offset_y = random.randint(-200, 100)
    pyautogui.moveTo(gold_loc[0], gold_loc[1] - 20)
    drag_time = random.randint(50, 100) / 100
    pyautogui.dragRel(drag_offset_x, drag_offset_y - 500, drag_time)


def wait_random():
    sec = random.randint(50, 300) / 100
    time.sleep(sec)


def click(location):
    pyautogui.leftClick(location[0] + 40, location[1] + 40)


if __name__ == "__main__":
    main()
