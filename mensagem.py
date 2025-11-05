from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class Mensagem(ABC):
    def __init__(self, conteudo: str, data_envio: Optional[datetime] = None):
        self.__conteudo = conteudo
        self.__data_envio = data_envio if data_envio else datetime.now()
        self.__enviada = False

    @property
    def conteudo(self) -> str:
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("Conteúdo da mensagem deve ser uma string não vazia")
        self.__conteudo = valor

    @property
    def data_envio(self) -> datetime:
        return self.__data_envio

    @property
    def enviada(self) -> bool:
        return self.__enviada

    def marcar_como_enviada(self):
        self.__enviada = True

    @abstractmethod
    def formatar(self) -> dict:
        pass

    @abstractmethod
    def validar(self) -> bool:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.conteudo[:50]}..."


class MensagemTexto(Mensagem):
    def __init__(self, conteudo: str, data_envio: Optional[datetime] = None):
        super().__init__(conteudo, data_envio)

    def formatar(self) -> dict:
        return {
            'tipo': 'texto',
            'conteudo': self.conteudo,
            'data_envio': self.data_envio.isoformat()
        }

    def validar(self) -> bool:
        return bool(self.conteudo and len(self.conteudo.strip()) > 0)


class MensagemMidia(Mensagem):
    def __init__(self, conteudo: str, arquivo: str, formato: str,
                 data_envio: Optional[datetime] = None):
        super().__init__(conteudo, data_envio)
        self.__arquivo = arquivo
        self.__formato = formato.lower()

    @property
    def arquivo(self) -> str:
        return self.__arquivo

    @property
    def formato(self) -> str:
        return self.__formato

    def validar(self) -> bool:
        return (bool(self.conteudo) and
                bool(self.arquivo) and
                bool(self.formato))


class MensagemVideo(MensagemMidia):
    def __init__(self, conteudo: str, arquivo: str, formato: str,
                 duracao: int, data_envio: Optional[datetime] = None):
        super().__init__(conteudo, arquivo, formato, data_envio)
        self.__duracao = duracao

    @property
    def duracao(self) -> int:
        return self.__duracao

    def formatar(self) -> dict:
        return {
            'tipo': 'video',
            'conteudo': self.conteudo,
            'arquivo': self.arquivo,
            'formato': self.formato,
            'duracao': self.duracao,
            'data_envio': self.data_envio.isoformat()
        }

    def validar(self) -> bool:
        formatos_validos = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv']
        return (super().validar() and
                self.formato in formatos_validos and
                self.duracao > 0)


class MensagemFoto(MensagemMidia):
    def __init__(self, conteudo: str, arquivo: str, formato: str,
                 data_envio: Optional[datetime] = None):
        super().__init__(conteudo, arquivo, formato, data_envio)

    def formatar(self) -> dict:
        return {
            'tipo': 'foto',
            'conteudo': self.conteudo,
            'arquivo': self.arquivo,
            'formato': self.formato,
            'data_envio': self.data_envio.isoformat()
        }

    def validar(self) -> bool:
        formatos_validos = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']
        return super().validar() and self.formato in formatos_validos


class MensagemArquivo(MensagemMidia):
    def __init__(self, conteudo: str, arquivo: str, formato: str,
                 data_envio: Optional[datetime] = None):
        super().__init__(conteudo, arquivo, formato, data_envio)

    def formatar(self) -> dict:
        return {
            'tipo': 'arquivo',
            'conteudo': self.conteudo,
            'arquivo': self.arquivo,
            'formato': self.formato,
            'data_envio': self.data_envio.isoformat()
        }

    def validar(self) -> bool:
        formatos_validos = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt',
                           'zip', 'rar', 'csv', 'ppt', 'pptx']
        return super().validar() and self.formato in formatos_validos
