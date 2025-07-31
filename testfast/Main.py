import speedtest
import sys

def vinibubumguloso():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        
        st.timeout = 10
        
        download = st.download()
        upload = st.upload()
        ping = st.results.ping

        return {
            "ping": ping,
            "download": download / 10**6, 
            "upload": upload / 10**6       
        }
    except Exception as e:
        return {"erro": str(e)}
