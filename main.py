import webview
import webview.menu as wm
import os
import sys

# ইউজার এজেন্ট যাতে সাইটগুলো ব্লক না করে
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

# PyInstaller দিয়ে বিল্ড করার পর ফাইলের সঠিক লোকেশন বের করার ফাংশন
def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(__file__), filename)

class Api:
    def __init__(self):
        self.window = None

    def load_url(self, url):
        # HTML থেকে কল করলে এই ফাংশন অ্যাপের ভেতরেই URL লোড করবে
        self.window.load_url(url)

def start_app():
    api = Api()
    html_file = get_asset_path('link.html')
    
    # অ্যাপের একেবারে উপরে একটি স্থায়ী মেনুবার তৈরি করা হচ্ছে (এটি কখনো মুছবে না)
    menu_items = [
        wm.Menu(
            'Navigation (Menu)',
            [
                wm.MenuAction('🏠 Back to Home', lambda: api.window.load_url(f'file://{html_file}')),
                wm.MenuAction('⬅️ Go Back', lambda: api.window.evaluate_js('window.history.back()')),
                wm.MenuAction('➡️ Go Forward', lambda: api.window.evaluate_js('window.history.forward()')),
                wm.MenuSeparator(),
                wm.MenuAction('🔄 Refresh Page', lambda: api.window.evaluate_js('window.location.reload()')),
            ]
        )
    ]

    api.window = webview.create_window(
        'My Workspace Hub',
        url=f'file://{html_file}', # সরাসরি ফাইল লোড করা হচ্ছে
        js_api=api,
        width=1280,
        height=850,
        confirm_close=True
    )

    # gui='edge' এবং মেনুবার সহ অ্যাপ চালু করা
    webview.start(gui='edge', menu=menu_items, user_agent=USER_AGENT)

if __name__ == '__main__':
    start_app()
