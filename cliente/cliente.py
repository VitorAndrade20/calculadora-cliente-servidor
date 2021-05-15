import socket

class Cliente():
    """
    Classe Cliente - Calculadora Remota - API Socket
    """
    def __init__(self,server_ip,port):
        """
        Construtor da classe Cliente
        :param server_ip: ip do servidor
        :param port: porta do serviço
        """
        self.__server_ip = server_ip
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def start(self):
        """
        Método que inicializa a execução do cliente
        """
        endpoint = (self.__server_ip,self.__port)

        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso")
            self.__method()
        except Exception as e:
            print("Erro na conexão com o servidor",e.args)
    
    def __method(self):
        """
        Método que interpreta as requisições do cliente e a IHM
        """
        try:
            msg = ''
            while msg != 'x':
                msg = input("Digite a operação desejada (x para sair): ")
                if msg == '':
                    continue
                elif msg == 'x':
                    break
                self.__tcp.send(bytes(msg,'ascii'))
                resp = self.__tcp.recv(1024)
                print("= ",resp.decode('ascii'))
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar a comunicação com o servidor. ",e.args)
