import socketio

sio = socketio.Client()

class Socket:
    def __init__(self, server):
        self.server = server
    
    def listen(self, query):
        sio.connect(self.server)
        sio.emit(query)
        sio.wait()

    def close():
        sio.disconnect()

    @sio.on('transactions')
    def tx(data):
        print(data)

    @sio.on('blocks')
    def blocs(data):
        print(data)
