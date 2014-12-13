import thread

POLL_FREQUENCY = 5

class Switch:
    def __init__(self, pin, callback):
        self.callback = callback
        self.pin = pin
        self.start(pin, callback)

    def start(self, callback):
        try:
            thread.start_new_thread(self.poll, ())
        except:
            print "Error creating thread"

    def poll(self):
        while True:
            time.sleep(POLL_FREQUENCY)
            # actually poll switch
            val = False
            self.callback(self, val)


