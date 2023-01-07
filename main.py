import pgzrun
import random
import math


""" CONFIGURATION """

WIDTH = 1200
HEIGHT = 1200

MARGIN = 20
NEW_UFO_PROBABILITY = 0.01
UFO_DIRECTION_CHANGE_PROBABILITY = 0.05

""" VARIABLES """

player = Actor("ship1")
player.x = WIDTH / 2
player.y = HEIGHT - 60
player.v = 2
player.va = 2
player.ac = 0.2
player.maxv = 8
player.angle = 0
player.lifes = 3
player.points = 0

ufos_list = []

player_lasers_list = []

explosions_list = []

player_lifes_list = []


""" DRAW """


def draw():
    screen.fill((0, 0, 0))

    draw_actors_list(explosions_list)
    draw_actors_list(ufos_list)
    draw_actors_list(player_lasers_list)
    draw_actors_list(player_lifes_list)

    player.draw()

    if player.lifes < 1:
        screen.draw.text("GAME OVER", center=(
            WIDTH / 2, HEIGHT / 2), fontsize=100, color="red")

    screen.draw.text(str(player.points), center=(
        WIDTH / 2, 40), fontsize=80, color="yellow")


def draw_actors_list(actors_list):
    for actor in actors_list:
        actor.draw()


""" UPDATE """


def update():
    if player.lifes < 1:
        return

    if random.random() <= NEW_UFO_PROBABILITY:
        add_ufo()

    update_player()
    update_ufos()
    update_lasers()
    update_hits()
    update_collisions()
    update_explosions()


def update_explosions():
    for explosion in explosions_list[:]:
        explosion.time -= 1

        if explosion.time == 0:
            explosion.number += 1
            explosion.time = 5

        if explosion.number > 9:
            explosions_list.remove(explosion)
            continue

        explosion.image = "explosion" + str(explosion.number)


def update_player():
    update_player_moves()
    move_actor(player)
    move_to_bounds(player)


def update_player_moves():
    if keyboard.A:
        player.angle += player.va

    if keyboard.D:
        player.angle -= player.va

    if keyboard.W:
        player.v += player.ac
        if player.v > player.maxv:
            player.v = player.maxv

    if keyboard.S:
        player.v -= player.ac
        if player.v < 0:
            player.v = 0


def update_ufos():
    for ufo in ufos_list:
        move_actor(ufo)
        move_to_bounds(ufo)
        update_ufo_angle(ufo)


def update_ufo_angle(ufo):
    if random.random() <= UFO_DIRECTION_CHANGE_PROBABILITY:
        ufo.desired_angle = random.randint(1, 360)

    if ufo.angle < ufo.desired_angle:
        ufo.angle += 1
    elif ufo.angle > ufo.desired_angle:
        ufo.angle -= 1


def update_lasers():
    for laser in player_lasers_list:
        move_actor(laser)

        if laser.x > WIDTH + MARGIN or laser.x < -MARGIN:
            player_lasers_list.remove(laser)

        if laser.y > HEIGHT + MARGIN or laser.y < -MARGIN:
            player_lasers_list.remove(laser)


def update_hits():
    update_player_lasers_hits(ufos_list)


def update_player_lasers_hits(enemy_list):
    for laser in player_lasers_list[:]:
        for enemy in enemy_list[:]:
            if enemy.colliderect(laser):
                add_explosion(enemy.x, enemy.y)
                enemy_list.remove(enemy)
                player_lasers_list.remove(laser)
                sounds.explosion.play()
                player.points += 10
                break


def update_collisions():
    for ufo in ufos_list[:]:
        if player.collidepoint(ufo.pos):
            ufos_list.remove(ufo)
            add_explosion(ufo.x, ufo.y)
            player.lifes -= 1
            player_lifes_list.pop()
            if player.lifes == 0:
                sounds.game_over.play()
                return
            
            sounds.shield.play()


""" EVENTS """


def on_key_down(key):
    if key == keys.SPACE:
        add_player_laser()
        sounds.laser.play()


""" HELPERS """


def move_actor(actor):
    actor.x += math.sin(math.radians(actor.angle - 180)) * actor.v
    actor.y += math.cos(math.radians(actor.angle - 180)) * actor.v


def move_to_bounds(actor):
    if actor.x > WIDTH + MARGIN:
        actor.x = -MARGIN

    if actor.x < -MARGIN:
        actor.x = WIDTH + MARGIN

    if actor.y < -MARGIN:
        actor.y = HEIGHT + MARGIN

    if actor.y > HEIGHT + MARGIN:
        actor.y = -MARGIN


def add_player_laser():
    laser = Actor("laser2")
    laser.angle = player.angle
    laser.x = player.x
    laser.y = player.y
    laser.v = 10
    player_lasers_list.append(laser)


def add_ufo():
    image = random.choice(["ufo1", "ufo2", "ufo3", "ufo4"])
    ufo = Actor(image)

    side = random.randint(1, 2)

    if side == 1:
        ufo.x = random.choice([-MARGIN, WIDTH + MARGIN])
        ufo.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        ufo.x = random.randint(MARGIN, WIDTH - MARGIN)
        ufo.y = random.choice([-MARGIN, HEIGHT + MARGIN])

    ufo.v = random.randint(2, 10)
    ufo.angle = random.randint(0, 360)
    ufo.desired_angle = ufo.angle
    ufos_list.append(ufo)


def add_explosion(x, y):
    explosion = Actor("explosion1")
    explosion.number = 1
    explosion.time = 5
    explosion.x = x
    explosion.y = y
    explosions_list.append(explosion)


""" INITIALIZATION """


def init():
    init_player_lifes()


def init_player_lifes():
    for i in range(player.lifes):
        life = Actor("life")
        life.x = MARGIN + i * 2 * MARGIN
        life.y = MARGIN
        player_lifes_list.append(life)


init()
pgzrun.go()
