def celebration():
    ev3.light.on(Color.RED)
    wait(70)
    ev3.light.on(Color.BLUE)
    wait(70)
    ev3.light.on(Color.YELLOW)
    wait(70)
    ev3.light.on(Color.GREEN)
    wait(70)

    ev3.speaker.set_volume(1000)
    ev3.speaker.play_file("FinalNyanCat.wav")

celebration()
