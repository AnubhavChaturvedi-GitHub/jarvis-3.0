import speedtest

def check_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping_speed = st.results.ping  # Ping in milliseconds

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping Speed: {ping_speed:.2f} ms")

if __name__ == "__main__":
    check_speed()
