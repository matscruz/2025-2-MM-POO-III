using System;

namespace ChatbotMessaging.Mensagens
{
    public abstract class Mensagem
    {
        private string _conteudo;
        private DateTime _dataEnvio;
        private bool _enviada;

        protected Mensagem(string conteudo, DateTime? dataEnvio = null)
        {
            _conteudo = conteudo ?? throw new ArgumentNullException(nameof(conteudo));
            _dataEnvio = dataEnvio ?? DateTime.Now;
            _enviada = false;
        }

        public string Conteudo
        {
            get => _conteudo;
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Conteúdo da mensagem não pode ser vazio", nameof(value));
                _conteudo = value;
            }
        }

        public DateTime DataEnvio => _dataEnvio;

        public bool Enviada => _enviada;

        public void MarcarComoEnviada()
        {
            _enviada = true;
        }

        public abstract object Formatar();

        public abstract bool Validar();

        public override string ToString()
        {
            var preview = Conteudo.Length > 50 ? Conteudo.Substring(0, 50) + "..." : Conteudo;
            return $"{GetType().Name}: {preview}";
        }
    }
}
