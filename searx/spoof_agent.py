import random

def generate_fake_user_agent():
    chrome_version = f"Chrome/{random.randint(80, 90)}.0.{random.randint(1000, 5000)}.{random.randint(100, 999)}"
    firefox_version = f"Firefox/{random.randint(80, 90)}.0"
    edge_version = f"Edg/{random.randint(80, 90)}.0.{random.randint(1000, 5000)}.{random.randint(100, 999)}"
    opera_version = f"OPR/{random.randint(70, 80)}.0.{random.randint(3000, 4000)}.{random.randint(100, 999)}"
    
    browsers = [
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {chrome_version} Safari/537.36",
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{firefox_version}) Gecko/{random.randint(20100101, 20220101)} Firefox/{firefox_version}",
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {edge_version} Safari/537.36",
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {opera_version} Safari/537.36"
    ]
    
    return random.choice(browsers)