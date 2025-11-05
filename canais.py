from abc import ABC, abstractmethod
from typing import List
from mensagem import Mensagem


class CanalComunicacao(ABC):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__historico_mensagens: List[Mensagem] = []
        self.__ativo = True

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def ativo(self) -> bool:
        return self.__ativo

    @property
    def historico_mensagens(self) -> List[Mensagem]:
        return self.__historico_mensagens.copy()

    def ativar(self):
        self.__ativo = True

    def desativar(self):
        self.__ativo = False

    def _adicionar_ao_historico(self, mensagem: Mensagem):
        self.__historico_mensagens.append(mensagem)

    @abstractmethod
    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        pass

    @abstractmethod
    def validar_destinatario(self, destinatario: str) -> bool:
        pass

    def _processar_envio(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self.ativo:
            print(f"[{self.nome}] Canal inativo. Não é possível enviar mensagens.")
            return False

        if not self.validar_destinatario(destinatario):
            print(f"[{self.nome}] Destinatário inválido: {destinatario}")
            return False

        if not mensagem.validar():
            print(f"[{self.nome}] Mensagem inválida.")
            return False

        return True

    def __str__(self) -> str:
        status = "Ativo" if self.ativo else "Inativo"
        return f"{self.__class__.__name__} - {self.nome} ({status})"


class CanalTelefone(CanalComunicacao):
    def __init__(self, nome: str):
        super().__init__(nome)

    def validar_destinatario(self, destinatario: str) -> bool:
        numeros = ''.join(filter(str.isdigit, destinatario))
        return 10 <= len(numeros) <= 15

    def _formatar_telefone(self, telefone: str) -> str:
        numeros = ''.join(filter(str.isdigit, telefone))
        return f"+{numeros}"


class WhatsApp(CanalTelefone):
    def __init__(self):
        super().__init__("WhatsApp")

    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self._processar_envio(mensagem, destinatario):
            return False

        telefone_formatado = self._formatar_telefone(destinatario)
        dados_mensagem = mensagem.formatar()

        print(f"\n[WhatsApp] Enviando para {telefone_formatado}")
        print(f"  Tipo: {dados_mensagem['tipo']}")
        print(f"  Conteúdo: {dados_mensagem['conteudo']}")

        if 'arquivo' in dados_mensagem:
            print(f"  Arquivo: {dados_mensagem['arquivo']}")
            print(f"  Formato: {dados_mensagem['formato']}")

        if 'duracao' in dados_mensagem:
            print(f"  Duração: {dados_mensagem['duracao']}s")

        mensagem.marcar_como_enviada()
        self._adicionar_ao_historico(mensagem)
        print(f"[WhatsApp] ✓ Mensagem enviada com sucesso!")
        return True


class TelegramTelefone(CanalTelefone):
    def __init__(self):
        super().__init__("Telegram (Telefone)")

    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self._processar_envio(mensagem, destinatario):
            return False

        telefone_formatado = self._formatar_telefone(destinatario)
        dados_mensagem = mensagem.formatar()

        print(f"\n[Telegram] Enviando para {telefone_formatado}")
        print(f"  Tipo: {dados_mensagem['tipo']}")
        print(f"  Conteúdo: {dados_mensagem['conteudo']}")

        if 'arquivo' in dados_mensagem:
            print(f"  Arquivo: {dados_mensagem['arquivo']}")
            print(f"  Formato: {dados_mensagem['formato']}")

        if 'duracao' in dados_mensagem:
            print(f"  Duração: {dados_mensagem['duracao']}s")

        mensagem.marcar_como_enviada()
        self._adicionar_ao_historico(mensagem)
        print(f"[Telegram] ✓ Mensagem enviada com sucesso!")
        return True


class CanalUsuario(CanalComunicacao):
    def __init__(self, nome: str):
        super().__init__(nome)

    def validar_destinatario(self, destinatario: str) -> bool:
        if not destinatario:
            return False
        usuario = destinatario.lstrip('@')
        if not (3 <= len(usuario) <= 30):
            return False
        return all(c.isalnum() or c in ['_', '.'] for c in usuario)

    def _formatar_usuario(self, usuario: str) -> str:
        return f"@{usuario.lstrip('@')}"


class Facebook(CanalUsuario):
    def __init__(self):
        super().__init__("Facebook")

    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self._processar_envio(mensagem, destinatario):
            return False

        usuario_formatado = self._formatar_usuario(destinatario)
        dados_mensagem = mensagem.formatar()

        print(f"\n[Facebook] Enviando para {usuario_formatado}")
        print(f"  Tipo: {dados_mensagem['tipo']}")
        print(f"  Conteúdo: {dados_mensagem['conteudo']}")

        if 'arquivo' in dados_mensagem:
            print(f"  Arquivo: {dados_mensagem['arquivo']}")
            print(f"  Formato: {dados_mensagem['formato']}")

        if 'duracao' in dados_mensagem:
            print(f"  Duração: {dados_mensagem['duracao']}s")

        mensagem.marcar_como_enviada()
        self._adicionar_ao_historico(mensagem)
        print(f"[Facebook] ✓ Mensagem enviada com sucesso!")
        return True


class Instagram(CanalUsuario):
    def __init__(self):
        super().__init__("Instagram")

    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self._processar_envio(mensagem, destinatario):
            return False

        usuario_formatado = self._formatar_usuario(destinatario)
        dados_mensagem = mensagem.formatar()

        print(f"\n[Instagram] Enviando para {usuario_formatado}")
        print(f"  Tipo: {dados_mensagem['tipo']}")
        print(f"  Conteúdo: {dados_mensagem['conteudo']}")

        if 'arquivo' in dados_mensagem:
            print(f"  Arquivo: {dados_mensagem['arquivo']}")
            print(f"  Formato: {dados_mensagem['formato']}")

        if 'duracao' in dados_mensagem:
            print(f"  Duração: {dados_mensagem['duracao']}s")

        mensagem.marcar_como_enviada()
        self._adicionar_ao_historico(mensagem)
        print(f"[Instagram] ✓ Mensagem enviada com sucesso!")
        return True


class TelegramUsuario(CanalUsuario):
    def __init__(self):
        super().__init__("Telegram (Usuário)")

    def enviar(self, mensagem: Mensagem, destinatario: str) -> bool:
        if not self._processar_envio(mensagem, destinatario):
            return False

        usuario_formatado = self._formatar_usuario(destinatario)
        dados_mensagem = mensagem.formatar()

        print(f"\n[Telegram] Enviando para {usuario_formatado}")
        print(f"  Tipo: {dados_mensagem['tipo']}")
        print(f"  Conteúdo: {dados_mensagem['conteudo']}")

        if 'arquivo' in dados_mensagem:
            print(f"  Arquivo: {dados_mensagem['arquivo']}")
            print(f"  Formato: {dados_mensagem['formato']}")

        if 'duracao' in dados_mensagem:
            print(f"  Duração: {dados_mensagem['duracao']}s")

        mensagem.marcar_como_enviada()
        self._adicionar_ao_historico(mensagem)
        print(f"[Telegram] ✓ Mensagem enviada com sucesso!")
        return True
