import thread

POLL_FREQUENCY = 5

class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.should_spin = False
        start()

    def start():
        try:
            thread.start_new_thread(self.run ())
        except:
            print "Error creating thread"

    def run():
        while True:
            time.sleep(POLL_FREQUENCY)
            # push the correct voltage
            if self.should_spin:
                pass
            else:
                pass

    def spin():
        self.should_spin = True

    def stop():
        self.should_spin = False


