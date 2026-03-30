import webview
import sys

# তোমার SAE Book ওয়েবসাইটের লিঙ্ক
URL = 'https://raseledutools.github.io/sae-book/'

def create_app():
    # ১. মেনু আইটেমগুলো তৈরি করা (ছবির মতো)
    menu_items = [
        webview.Menu(
            'Navigation (Menu)', # মেইন মেনু নাম
            [
                webview.MenuAction('🏠 Back to Home', lambda: window.load_url(URL)),
                webview.MenuAction('⬅ Go Back', lambda: window.evaluate_js('window.history.back()')),
                webview.MenuAction('➡ Go Forward', lambda: window.evaluate_js('window.history.forward()')),
                webview.MenuSeparator(), # মাঝখানের দাগ
                webview.MenuAction('🔄 Refresh Page', lambda: window.evaluate_js('window.location.reload()')),
            ]
        )
    ]

    # ২. উইন্ডো তৈরি করা এবং মেনু সেট করা
    window = webview.create_window(
        'SAE Book Hub - Rasel Mia', 
        URL,
        width=1280, 
        height=800,
        resizable=True,
        confirm_close=True
    )

    # ৩. অ্যাপ শুরু করা (মেনু লিস্ট সহ)
    webview.start(menu=menu_items)

if __name__ == '__main__':
    create_app()
