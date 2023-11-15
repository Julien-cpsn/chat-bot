#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to test dialogue and media"""

import qi
import time
import sys
import argparse


class Main:
    def __init__(self, session):
        """
        This example uses the showImage method.
        To Test ALTabletService, you need to run the script ON the robot.
        """
        # Get the service ALTabletService.

        try:
            ### Services ###

            self.tablet_service = session.service("ALTabletService")
            self.memory = session.service("ALMemory")

            ### Subscribers ###

            self.play_sfr_subscriber = self.memory.subscriber("play_sfr")
            self.play_sfr_subscriber.signal.connect(self.play_sfr)

            ### Settings ###

            self.tablet_service.setBrightness(1.0)
            self.tablet_service.setVolume(10)

            ### Web view ###

            self.tablet_service.showWebview("http://198.18.0.1/apps/chat_bot/index.html")

        except Exception, e:
            print "Error was: ", e

    def run(self):
        while True:
            time.sleep(2)

    def play_sfr(self, _):
        print "Clicked on SFR"
        self.tablet_service.playVideo("http://198.18.0.1/apps/chat_bot/SFR.mp4")
        time.sleep(4)
        self.tablet_service.stopVideo()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    qi_session = qi.Session()
    try:
        qi_session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print (
                "Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                               "Please check your script arguments. Run with -h option for help."
        )
        sys.exit(1)

    app = Main(qi_session)
    app.run()
