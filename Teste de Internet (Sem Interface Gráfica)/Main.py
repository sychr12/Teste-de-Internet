import speedtest

def vinibubumguloso():
    st = speedtest.Speedtest()

    print("🔍 Buscando melhor servidor...")
    st.get_best_server()

    print("⬇️ Testando download...")
    preguiça_pra_da_nome = st.download()

    print("⬆️ Testando upload...")
    seila_qualquer_nome = st.upload()

    print(f"📶 Ping: {st.results.ping} ms")
    print(f"⬇️ Velocidade de download: {preguiça_pra_da_nome / 10**6:.2f} Mbps")
    print(f"⬆️ Velocidade de upload: {seila_qualquer_nome / 10**6:.2f} Mbps")

    input("\nPressione Enter para fechar...")

vinibubumguloso()

