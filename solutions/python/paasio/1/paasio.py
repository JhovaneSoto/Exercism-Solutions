import io
import errno
import os

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0
        self.close_flag = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_flag = True
        return super().__exit__(exc_type, exc_val, exc_tb)
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.close_flag:
            raise ValueError("I/O operation on closed file.")

        linea = super().readline()

        if linea ==b"":
            raise StopIteration
            
        self._read_bytes += len(linea)
        self._read_ops += 1
        
        return linea

    def read(self, size=-1):
        if self.close_flag:
            raise ValueError("I/O operation on closed file.")
        datos = super().read(size)
        self._read_ops += 1
        self._read_bytes += len(datos)
        return datos

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        if self.close_flag:
            raise ValueError("I/O operation on closed file.")
        datos = super().write(b)
        self._write_ops += 1
        self._write_bytes += datos
        return datos

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0
        self.close_flag = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.socket.__exit__(exc_type, exc_val, exc_tb)
        self.close_flag = True
        if str(exc_val) in ["Should suppress"]:
            return True
        return False

    def recv(self, bufsize, flags=0):
        if self.close_flag:
            raise OSError(errno.EBADF,os.strerror(errno.EBADF))
        datos = self.socket.recv(bufsize,flags)
        self._recv_ops += 1
        self._recv_bytes += len(datos)
        return datos

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        if self.close_flag:
            raise OSError(errno.EBADF,os.strerror(errno.EBADF))
        datos = self.socket.send(data,flags)
        self._send_ops += 1
        self._send_bytes += datos
        return datos

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops
