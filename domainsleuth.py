import socket
import ssl
import sys

def get_sni_info(domain: str) -> None:
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=domain
        )

        conn.connect((domain, 443))
        cert = conn.getpeercert()

        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']

        san = cert['subjectAltName']
        alternative_names = [item[1] for item in san if item[0] == 'DNS']

        print(f"Certificado emitido para: {issued_to}")
        print("Nomes alternativos do certificado:")
        for name in alternative_names:
            print(f"- {name}")

    except Exception as e:
        print(f"Erro ao obter informações SNI para {domain}: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    get_sni_info(domain)
