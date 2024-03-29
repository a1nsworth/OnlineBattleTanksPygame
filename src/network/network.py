import socket
import logging
from abc import ABCMeta, abstractmethod
from sys import stdout
from threading import Thread


class BaseTcpObject(metaclass=ABCMeta):
    def __init__(self, ipv4: str, port: int):
        self._socket: socket.socket
        self._ip = ipv4
        self._port = port

    @property
    def ip(self) -> str:
        return self._ip

    @property
    def port(self) -> int:
        return self._port


class TcpServer(BaseTcpObject, metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def _handle_requests(self, handle_socket: socket.socket):
        pass


class TcpClient(BaseTcpObject, metaclass=ABCMeta):
    pass


class Client(TcpClient):
    def __init__(self, ipv4: str, port: int):
        super().__init__(ipv4, port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self._socket.connect((ipv4, port))

    def close(self) -> None:
        self._socket.close()


class Server(TcpServer):
    MAX_CONNECTION_SAMETIME: int = 5
    MAX_PLAYERS: int = 2

    def __init__(self, ipv4: str, port: int):
        super().__init__(ipv4, port)
        self.logger = logging.getLogger(__name__)

        self.logger.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter(
            "%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
        console_handler = logging.StreamHandler(stdout)
        console_handler.setFormatter(log_formatter)
        self.logger.addHandler(console_handler)
        self.logger.info("created logger")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self._socket.bind((ipv4, port))
        self._socket.setblocking(False)
        self._socket.listen(Server.MAX_CONNECTION_SAMETIME)
        self._clients: list[socket] = []

    def run(self):
        while True:
            try:
                new_socket, ip_port = self._socket.accept()
                new_socket.setblocking(False)
            except BlockingIOError:
                pass
            else:
                print("New connection from {}".format(ip_port))
                self._clients.append(new_socket)
                self.logger.info("New connection from {}".format(ip_port))
                Thread(target=self._handle_requests, args=(new_socket,)).start()

    def _handle_requests(self, handle_socket: socket.socket):
        while True:
            pass
