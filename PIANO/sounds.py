from pygame import mixer

def load_sound(keys):
    sounds ={}
    for ket, filename in keys.item():
        sounds[key] = mixer.Sound(f"assets/sound/{filename}")
    return sounds