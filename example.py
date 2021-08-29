import os
import sys

from PyQt5 import QtCore, QtMultimedia



def main():
    filename = 'Eye_sound.mp3'

    app = QtCore.QCoreApplication(sys.argv)

    player = QtMultimedia.QMediaPlayer()

    def handle_state_changed(state):
        if state == QtMultimedia.QMediaPlayer.PlayingState:
            print("started")
        elif state == QtMultimedia.QMediaPlayer.StoppedState:
            print("finished")
            player.stop()

    player.stateChanged.connect(handle_state_changed)

    url = QtCore.QUrl.fromLocalFile(filename)
    player.setMedia(QtMultimedia.QMediaContent(url))
    player.play()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()