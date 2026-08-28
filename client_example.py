import requests

BASE_URL = "https://api1.api.cbtraderbd.xyz"

def get_iqoption_live_price(asset="EURUSD"):
    try:
        response = requests.get(f"{BASE_URL}/api/iqoption/price", params={"asset": asset})
        print(f"[{asset}] Live Price:", response.json())
    except Exception as e:
        print("Error fetching price:", e)

if __name__ == "__main__":
    print("Connecting to IQ Option REST Stream via CB Traders BD API...")
    get_iqoption_live_price("EURUSD")
