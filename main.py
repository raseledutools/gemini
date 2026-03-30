import webview
import sys

def create_app():
    # তোমার SAE Book ওয়েবসাইটের লিঙ্ক
    url = 'https://raseledutools.github.io/sae-book/'
    
    # উইন্ডো তৈরি করা
    window = webview.create_window(
        'Helper tools - Rasel Mia', 
        url,
        width=1280, 
        height=800,
        resizable=True,
        min_size=(800, 600),
        confirm_close=True
    )
    
    # অ্যাপ শুরু করা
    webview.start()

if __name__ == '__main__':
    create_app()
