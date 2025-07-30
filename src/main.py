import requests

def verificar_site(url):
    """Tenta acessar uma URL e retorna seu status."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {url} está ONLINE!")
        else:
            print(f"❌ {url} retornou status {response.status_code}.")
    except requests.RequestException:
        print(f"🔥 {url} parece estar OFFLINE ou não existe.")

def main():
    """Função principal que lê os sites e os verifica."""
    print("--- Verificador de Status de Sites ---")
    sites = [
        "https://google.com",
        "https://github.com",
        "https://umsitequenaoexiste12345.com"
    ]
    for site in sites:
        verificar_site(site)

if __name__ == "__main__":
    main()