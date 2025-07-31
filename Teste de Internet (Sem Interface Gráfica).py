import speedtest

def vinibubumguloso():
    st = speedtest.Speedtest()
    
    # esse parte busca o melhor server
    print("🔍 Buscando melhor servidor...")
    print("Por favor, aguarde.")
    st.get_best_server()
    
    # esse parte testa o download
    print("⬇️ Testando download...")
    print("Por favor, aguarde.")
    preguiça_pra_da_nome = st.download()
    
    # esse aqui testa o upload
    print("⬆️ Testando upload...")
    print("Por favor, aguarde.")
    seila_qualquer_nome = st.upload()
    

    #Resultado de tudo
    print("📶 Ping:", st.results.ping, "ms")
    print("⬇️ Velocidade de download: {:.2f} Mbps".format(preguiça_pra_da_nome / 10**6))
    print("⬆️ Velocidade de upload: {:.2f} Mbps".format(seila_qualquer_nome / 10**6))

vinibubumguloso()
