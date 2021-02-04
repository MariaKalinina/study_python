from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        def out_red(text):
            print("\033[31m {}".format(text))

        def out_yellow(text):
            print("\033[33m {}".format(text))

        def out_green(text):
            print("\033[32m {}".format(text))

        while True:
            out_red("Traffic light is red")
            sleep(7)
            out_yellow("Traffic light is yellow")
            sleep(2)
            out_green("Traffic light is green")
            sleep(7)
            out_yellow("Traffic light is yellow")
            sleep(2)


light_1 = TrafficLight()
light_1.running()
