import thread

POLL_FREQUENCY = 5

class Switch:
    def __init__(self, pin, callback):
        self.callback = callback
        self.start(pin, callback)

    def start(self, callback):
        try:
            thread.start_new_thread(self.poll, (POLL_FREQUENCY))
        except:
            print "Error creating thread"

    def poll(self, frequency):
        while True:
            time.sleep(frequency)
            # actually poll switch
            val = False
            if val:
                self.callback(self, val)


