"""
Provides features for in-app communications
"""
from PyQt5.QtCore import QObject, pyqtSignal


class MessageHub(QObject):
    """
    Responsible of collecting all messages and dispatching to whoever wants to listen to them.

    Any object can register, as soon as it has a on_message(str) function
    """
    message_signal = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)

    def _dispatch_message(self, message: str):

        self.message_signal.emit(message)

    def dispatch_info(self, message: str):

        self._dispatch_message(message)

    def dispatch_warning(self, message: str):

        self._dispatch_message(message)

    def dispatch_error(self, message: str):

        self._dispatch_message(message)

    def add_receiver(self, receiver):
        """
        Connects  message signal to a receiver

        :param receiver: the receiver
        :type receiver: any. It must have a on_message(str) function.
        """
        self.message_signal[str].connect(receiver.on_message)


MESSAGE_HUB = MessageHub()
