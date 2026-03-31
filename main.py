import webview
import sys
import threading
from pystray import Icon, Menu as TrayMenu, MenuItem as TrayMenuItem
from PIL import Image, ImageDraw

# আপনার লিঙ্ক
URL = 'https://raseledutools.github.io'

class RaselApp:
    def __init__(self):
        self.window = webview.create_window(
            'Rasel Workspace Hub', 
            URL,
            width=1280, 
            height=800,
            resizable=True
        )
        self.tray_icon = None

    # ট্রে আইকন তৈরি করার ফাংশন
    def create_tray_icon(self):
        # একটি সাধারণ আইকন তৈরি (আপনি চাইলে নিজের .png বা .ico ফাইল দিতে পারেন)
        image = Image.new('RGB', (64, 64), color=(73, 109, 137))
        d = ImageDraw.Draw(image)
        d.text((10, 10), "Ras", fill=(255, 255, 0))

        menu = TrayMenu(
            TrayMenuItem('Show App', self.show_window),
            TrayMenuItem('Exit', self.exit_app)
        )
        self.tray_icon = Icon("RaselApp", image, "Rasel Workspace Hub", menu)
        self.tray_icon.run()

    def show_window(self):
        self.window.show()

    def exit_app(self):
        self.tray_icon.stop()
        sys.exit()

    def run(self):
        # ট্রে আইকন আলাদা থ্রেডে চালানো
        tray_thread = threading.Thread(target=self.create_tray_icon, daemon=True)
        tray_thread.start()

        # নেটিভ মেনু (উইন্ডোর উপরে থাকবে)
        from webview.menu import Menu, MenuAction, MenuSeparator
        menu_items = [
            Menu('Navigation (Menu)', [
                MenuAction('🏠 Back to Home', lambda: self.window.load_url(URL)),
                MenuAction('⬅ Go Back', lambda: self.window.evaluate_js('window.history.back()')),
                MenuAction('➡ Go Forward', lambda: self.window.evaluate_js('window.history.forward()')),
                MenuSeparator(),
                MenuAction('🔄 Refresh Page', lambda: self.window.evaluate_js('window.location.reload()')),
                MenuSeparator(),
                MenuAction('❌ Hide to Tray', lambda: self.window.hide()),
                MenuAction('🔴 Fully Exit', self.exit_app)
            ])
        ]

        webview.start(menu=menu_items)

if __name__ == '__main__':
    app = RaselApp()
    app.run()
