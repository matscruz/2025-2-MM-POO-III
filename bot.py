from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class InvalidRecipientError(Exception):
    pass


class UnsupportedMessageError(Exception):
    pass


@dataclass
class Message(ABC):
    _text: str
    _send_date: Optional[datetime] = None

    def __post_init__(self):
        if self._send_date is None:
            self._send_date = datetime.now()

    @property
    def text(self) -> str:
        return self._text

    @property
    def send_date(self) -> datetime:
        return self._send_date

    @abstractmethod
    def metadata(self) -> dict:
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(text={self.text!r}, send_date={self.send_date})"


@dataclass
class TextMessage(Message):
    def metadata(self) -> dict:
        return {"type": "text", "text": self.text}


class MediaMessage(Message, ABC):
    def __init__(self, message: str, file_path: str, format: str, duration_seconds: Optional[int] = None):
        super().__init__(message)
        self._file_path = file_path
        self._format = format
        self._duration_seconds = duration_seconds

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def format(self) -> str:
        return self._format

    @property
    def duration_seconds(self) -> Optional[int]:
        return self._duration_seconds

    def metadata(self) -> dict:
        meta = {
            "type": "media",
            "text": self.text,
            "file_path": self.file_path,
            "format": self.format,
        }
        if self.duration_seconds is not None:
            meta["duration_seconds"] = self.duration_seconds
        return meta


class PhotoMessage(MediaMessage):
    def __init__(self, message: str, file_path: str, format: str):
        super().__init__(message, file_path, format, duration_seconds=None)

    def metadata(self) -> dict:
        meta = super().metadata()
        meta["type"] = "photo"
        meta.pop("duration_seconds", None)
        return meta


class FileMessage(MediaMessage):
    def __init__(self, message: str, file_path: str, format: str):
        super().__init__(message, file_path, format, duration_seconds=None)

    def metadata(self) -> dict:
        meta = super().metadata()
        meta["type"] = "file"
        meta.pop("duration_seconds", None)
        return meta


class Channel(ABC):
    @abstractmethod
    def send(self, message: Message, recipient: str) -> None:
        pass


class PhoneChannel(Channel, ABC):
    def _validate_phone(self, recipient: str) -> None:
        r = recipient.strip()
        if r.startswith("+"):
            r = r[1:]
        if not r.isdigit() or not (8 <= len(r) <= 15):
            raise InvalidRecipientError(f"Telefone inválido: {recipient!r}")


class UserChannel(Channel, ABC):
    def _validate_username(self, recipient: str) -> None:
        r = recipient.strip()
        if not r or len(r) > 50:
            raise InvalidRecipientError(f"Usuário inválido: {recipient!r}")


class WhatsAppChannel(PhoneChannel):
    def send(self, message: Message, recipient: str) -> None:
        self._validate_phone(recipient)
        meta = message.metadata()
        print(f"[WhatsApp] Enviando para {recipient} -> tipo: {meta['type']}, texto: {meta.get('text')}")
        if meta["type"] != "text":
            print(f"  arquivo: {meta.get('file_path')} ({meta.get('format')})")
        print("  -> Enviado via WhatsApp.")


class TelegramChannel(PhoneChannel, UserChannel):
    def send(self, message: Message, recipient: str) -> None:
        r = recipient.strip()
        if r.startswith("@") or (not r.startswith("+") and not r.replace("+", "").isdigit()):
            self._validate_username(r)
        else:
            self._validate_phone(r)

        meta = message.metadata()
        print(f"[Telegram] Enviando para {recipient} -> tipo: {meta['type']}, texto: {meta.get('text')}")
        if meta["type"] != "text":
            print(f"  arquivo: {meta.get('file_path')} ({meta.get('format')})")
        print("  -> Enviado via Telegram.")


class FacebookChannel(UserChannel):
    def send(self, message: Message, recipient: str) -> None:
        self._validate_username(recipient)
        meta = message.metadata()
        print(f"[Facebook] Enviando para {recipient} -> tipo: {meta['type']}, texto: {meta.get('text')}")
        if meta["type"] != "text":
            print(f"  arquivo: {meta.get('file_path')} ({meta.get('format')})")
        print("  -> Enviado via Facebook.")


class InstagramChannel(UserChannel):
    def send(self, message: Message, recipient: str) -> None:
        self._validate_username(recipient)
        meta = message.metadata()
        print(f"[Instagram] Enviando para {recipient} -> tipo: {meta['type']}, texto: {meta.get('text')}")
        if meta["type"] != "text":
            print(f"  arquivo: {meta.get('file_path')} ({meta.get('format')})")
        print("  -> Enviado via Instagram.")


def send_message_to_channel(channel: Channel, message: Message, recipient: str) -> None:
    try:
        channel.send(message, recipient)
    except InvalidRecipientError as e:
        print(f"[Erro] destinatário inválido: {e}")
    except UnsupportedMessageError as e:
        print(f"[Erro] mensagem não suportada: {e}")
    except Exception as e:
        print(f"[Erro inesperado] {e}")


def main():
    wa = WhatsAppChannel()
    tg = TelegramChannel()
    fb = FacebookChannel()
    ig = InstagramChannel()

    txt = TextMessage("Mensagem de texto")
    photo = PhotoMessage("Foto legal", "/tmp/foto.jpg", "jpg")
    filemsg = FileMessage("Documento enviado", "/tmp/doc.pdf", "pdf")

    send_message_to_channel(wa, txt, "+5511999999999")
    send_message_to_channel(ig, photo, "@usuario")
    send_message_to_channel(fb, filemsg, "@pagina")


if __name__ == "__main__":
    main()
