from msvcrt import getch
while True:
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        print("Enter")
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            print("down")
        elif key == 72: #Up arrow
            print("up")

#Those are examples. It is not the final module.
#It seems we'll need the ASCII table or something like it for decoding DEC input as keypresses.
#Oh and, yea, now you're unable to kill me.