using System;
using System.Collections.Generic;

abstract class Mensagem
{
    public string Conteudo { get; set; }
    public DateTime DataEnvio { get; set; }

    public abstract void Enviar(Canal canal);
}

class MensagemTexto : Mensagem
{
    public override void Enviar(Canal canal)
    {
        canal.EnviarMensagem($"Texto: {Conteudo} | Enviado em: {DataEnvio}");
    }
}

class MensagemVideo : Mensagem
{
    public string Arquivo { get; set; }
    public string Formato { get; set; }
    public int DuracaoSegundos { get; set; }

    public override void Enviar(Canal canal)
    {
        canal.EnviarMensagem($"Vídeo: {Conteudo} | Arquivo: {Arquivo}.{Formato} | Duração: {DuracaoSegundos}s");
    }
}

class MensagemFoto : Mensagem
{
    public string Arquivo { get; set; }
    public string Formato { get; set; }

    public override void Enviar(Canal canal)
    {
        canal.EnviarMensagem($"Foto: {Conteudo} | Arquivo: {Arquivo}.{Formato}");
    }
}

class MensagemArquivo : Mensagem
{
    public string Arquivo { get; set; }
    public string Formato { get; set; }

    public override void Enviar(Canal canal)
    {
        canal.EnviarMensagem($"Arquivo: {Conteudo} | Arquivo: {Arquivo}.{Formato}");
    }
}

abstract class Canal
{
    public abstract void EnviarMensagem(string mensagem);
}


class CanalWhatsApp : Canal
{
    private string NumeroTelefone;

    public CanalWhatsApp(string numero)
    {
        NumeroTelefone = numero;
    }

    public override void EnviarMensagem(string mensagem)
    {
        Console.WriteLine($"[WhatsApp para {NumeroTelefone}] {mensagem}");
    }
}


class CanalTelegram : Canal
{
    private string Usuario;
    private string NumeroTelefone;

    public CanalTelegram(string usuario = null, string numero = null)
    {
        Usuario = usuario;
        NumeroTelefone = numero;
    }

    public override void EnviarMensagem(string mensagem)
    {
        string destino = Usuario ?? NumeroTelefone;
        Console.WriteLine($"[Telegram para {destino}] {mensagem}");
    }
}


class CanalFacebook : Canal
{
    private string Usuario;

    public CanalFacebook(string usuario)
    {
        Usuario = usuario;
    }

    public override void EnviarMensagem(string mensagem)
    {
        Console.WriteLine($"[Facebook para {Usuario}] {mensagem}");
    }
}


class CanalInstagram : Canal
{
    private string Usuario;

    public CanalInstagram(string usuario)
    {
        Usuario = usuario;
    }

    public override void EnviarMensagem(string mensagem)
    {
        Console.WriteLine($"[Instagram para {Usuario}] {mensagem}");
    }
}