using System;
using System.Collections.Generic;
using System.Linq;
using ChatbotMessaging.Mensagens;
using ChatbotMessaging.Canais;

namespace ChatbotMessaging
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            
            Console.WriteLine();
            Console.WriteLine("╔" + new string('=', 68) + "╗");
            Console.WriteLine("║" + CentralizarTexto("SISTEMA DE CHATBOT MULTI-CANAL", 68) + "║");
            Console.WriteLine("║" + CentralizarTexto("Demonstração de Programação Orientada a Objetos", 68) + "║");
            Console.WriteLine("╚" + new string('=', 68) + "╝");

            ExemploMensagemTexto();
            ExemploMensagemVideo();
            ExemploMensagemFoto();
            ExemploMensagemArquivo();
            ExemploPolimorfismo();
            ExemploEncapsulamento();
            ExemploValidacoes();
            ExemploHeranca();

            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("DEMONSTRAÇÃO CONCLUÍDA");
            Console.WriteLine(new string('=', 70));
            Console.WriteLine("\nConceitos de POO demonstrados:");
            Console.WriteLine("  ✓ Herança: Classes derivadas de classes base");
            Console.WriteLine("  ✓ Encapsulamento: Propriedades e campos privados");
            Console.WriteLine("  ✓ Polimorfismo: Mesma interface, comportamentos diferentes");
            Console.WriteLine("  ✓ Abstração: Classes abstratas e métodos abstratos");
            Console.WriteLine();
        }

        static string CentralizarTexto(string texto, int largura)
        {
            int espacos = (largura - texto.Length) / 2;
            return new string(' ', espacos) + texto + new string(' ', largura - espacos - texto.Length);
        }

        static void ExemploMensagemTexto()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 1: MENSAGENS DE TEXTO");
            Console.WriteLine(new string('=', 70));

            var mensagem = new MensagemTexto(
                "Olá! Esta é uma mensagem de teste do nosso chatbot.",
                DateTime.Now
            );

            var whatsapp = new WhatsApp();
            whatsapp.Enviar(mensagem, "+5511999887766");

            var telegramTel = new TelegramTelefone();
            telegramTel.Enviar(mensagem, "5511999887766");

            var facebook = new Facebook();
            facebook.Enviar(mensagem, "@joao.silva");

            var instagram = new Instagram();
            instagram.Enviar(mensagem, "maria_santos");

            var telegramUser = new TelegramUsuario();
            telegramUser.Enviar(mensagem, "@pedro_oliveira");
        }

        static void ExemploMensagemVideo()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 2: MENSAGENS DE VÍDEO");
            Console.WriteLine(new string('=', 70));

            var mensagem = new MensagemVideo(
                "Confira este vídeo promocional!",
                "/videos/promocao.mp4",
                "mp4",
                120
            );

            var whatsapp = new WhatsApp();
            whatsapp.Enviar(mensagem, "+5511988776655");

            var instagram = new Instagram();
            instagram.Enviar(mensagem, "@empresa_oficial");
        }

        static void ExemploMensagemFoto()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 3: MENSAGENS DE FOTO");
            Console.WriteLine(new string('=', 70));

            var mensagem = new MensagemFoto(
                "Veja nossa nova coleção!",
                "/imagens/colecao_verao.jpg",
                "jpg"
            );

            var instagram = new Instagram();
            instagram.Enviar(mensagem, "@cliente_vip");

            var facebook = new Facebook();
            facebook.Enviar(mensagem, "@loja.oficial");
        }

        static void ExemploMensagemArquivo()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 4: MENSAGENS DE ARQUIVO");
            Console.WriteLine(new string('=', 70));

            var mensagem = new MensagemArquivo(
                "Segue o relatório mensal em anexo.",
                "/documentos/relatorio_mensal.pdf",
                "pdf"
            );

            var whatsapp = new WhatsApp();
            whatsapp.Enviar(mensagem, "+5511977665544");

            var telegramUser = new TelegramUsuario();
            telegramUser.Enviar(mensagem, "@gerente_vendas");
        }

        static void ExemploPolimorfismo()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 5: POLIMORFISMO EM AÇÃO");
            Console.WriteLine(new string('=', 70));

            var canais = new List<CanalComunicacao>
            {
                new WhatsApp(),
                new TelegramTelefone(),
                new TelegramUsuario(),
                new Facebook(),
                new Instagram()
            };

            var mensagens = new List<Mensagem>
            {
                new MensagemTexto("Mensagem de texto simples"),
                new MensagemFoto("Foto anexada", "/fotos/imagem.jpg", "jpg"),
                new MensagemVideo("Vídeo anexado", "/videos/video.mp4", "mp4", 60),
                new MensagemArquivo("Documento anexado", "/docs/arquivo.pdf", "pdf")
            };

            Console.WriteLine("\nDemonstrando polimorfismo: mesma interface, comportamentos diferentes\n");

            for (int i = 0; i < canais.Count; i++)
            {
                var canal = canais[i];
                var mensagem = mensagens[i % mensagens.Count];
                
                Console.WriteLine($"\nCanal {i + 1}: {canal}");
                Console.WriteLine($"Tipo de mensagem: {mensagem.GetType().Name}");
                Console.WriteLine($"Dados formatados: {FormatarDicionario(mensagem.Formatar())}");
            }
        }

        static void ExemploEncapsulamento()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 6: ENCAPSULAMENTO");
            Console.WriteLine(new string('=', 70));

            var whatsapp = new WhatsApp();

            Console.WriteLine($"\nNome do canal: {whatsapp.Nome}");
            Console.WriteLine($"Status: {(whatsapp.Ativo ? "Ativo" : "Inativo")}");

            var msg1 = new MensagemTexto("Primeira mensagem");
            var msg2 = new MensagemTexto("Segunda mensagem");

            whatsapp.Enviar(msg1, "+5511999888777");
            whatsapp.Enviar(msg2, "+5511999888777");

            var historico = whatsapp.HistoricoMensagens;
            Console.WriteLine($"\nTotal de mensagens no histórico: {historico.Count}");

            whatsapp.Desativar();
            Console.WriteLine($"\nStatus após desativar: {(whatsapp.Ativo ? "Ativo" : "Inativo")}");

            var msg3 = new MensagemTexto("Terceira mensagem");
            whatsapp.Enviar(msg3, "+5511999888777");
        }

        static void ExemploValidacoes()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 7: VALIDAÇÕES");
            Console.WriteLine(new string('=', 70));

            var whatsapp = new WhatsApp();
            var facebook = new Facebook();

            Console.WriteLine("\n--- Testando validação de destinatários ---");

            var telefones = new[] { "+5511999888777", "11999888777", "123", "" };
            foreach (var tel in telefones)
            {
                bool valido = whatsapp.ValidarDestinatario(tel);
                Console.WriteLine($"Telefone '{tel}': {(valido ? "✓ Válido" : "✗ Inválido")}");
            }

            Console.WriteLine("\n--- Testando validação de usuários ---");

            var usuarios = new[] { "@joao_silva", "maria.santos", "ab", "usuario@invalido!", "" };
            foreach (var user in usuarios)
            {
                bool valido = facebook.ValidarDestinatario(user);
                Console.WriteLine($"Usuário '{user}': {(valido ? "✓ Válido" : "✗ Inválido")}");
            }

            Console.WriteLine("\n--- Testando validação de mensagens ---");

            var msgValida = new MensagemTexto("Mensagem válida");
            Console.WriteLine($"Mensagem de texto: {(msgValida.Validar() ? "✓ Válida" : "✗ Inválida")}");

            var msgVideoValida = new MensagemVideo("Vídeo", "/video.mp4", "mp4", 60);
            Console.WriteLine($"Vídeo (mp4, 60s): {(msgVideoValida.Validar() ? "✓ Válido" : "✗ Inválido")}");

            var msgVideoInvalida = new MensagemVideo("Vídeo", "/video.xyz", "xyz", 60);
            Console.WriteLine($"Vídeo (xyz, 60s): {(msgVideoInvalida.Validar() ? "✓ Válido" : "✗ Inválido")}");
        }

        static void ExemploHeranca()
        {
            Console.WriteLine("\n" + new string('=', 70));
            Console.WriteLine("EXEMPLO 8: HIERARQUIA DE HERANÇA");
            Console.WriteLine(new string('=', 70));

            var msgTexto = new MensagemTexto("Texto");
            var msgFoto = new MensagemFoto("Foto", "/foto.jpg", "jpg");
            var msgVideo = new MensagemVideo("Vídeo", "/video.mp4", "mp4", 60);
            var msgArquivo = new MensagemArquivo("Arquivo", "/doc.pdf", "pdf");

            var whatsapp = new WhatsApp();
            var telegramTel = new TelegramTelefone();
            var facebook = new Facebook();
            var instagram = new Instagram();

            Console.WriteLine("\n--- Hierarquia de Mensagens ---");
            var mensagens = new Mensagem[] { msgTexto, msgFoto, msgVideo, msgArquivo };
            foreach (var msg in mensagens)
            {
                Console.WriteLine($"\n{msg.GetType().Name}");
                var baseType = msg.GetType().BaseType;
                if (baseType != null)
                {
                    Console.WriteLine($"  └─ Herda de: {baseType.Name}");
                    if (baseType.BaseType != null && baseType.BaseType != typeof(object))
                    {
                        Console.WriteLine($"     └─ Herda de: {baseType.BaseType.Name}");
                    }
                }
            }

            Console.WriteLine("\n--- Hierarquia de Canais ---");
            var canais = new CanalComunicacao[] { whatsapp, telegramTel, facebook, instagram };
            foreach (var canal in canais)
            {
                Console.WriteLine($"\n{canal.GetType().Name}");
                var baseType = canal.GetType().BaseType;
                if (baseType != null)
                {
                    Console.WriteLine($"  └─ Herda de: {baseType.Name}");
                    if (baseType.BaseType != null && baseType.BaseType != typeof(object))
                    {
                        Console.WriteLine($"     └─ Herda de: {baseType.BaseType.Name}");
                    }
                }
            }
        }

        static string FormatarDicionario(object obj)
        {
            if (obj is Dictionary<string, object> dict)
            {
                var items = dict.Select(kvp => $"{kvp.Key}: {kvp.Value}");
                return "{" + string.Join(", ", items) + "}";
            }
            return obj?.ToString() ?? "null";
        }
    }
}
