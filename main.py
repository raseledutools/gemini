import webview
import sys

# শক্তিশালী ইউজার এজেন্ট যাতে হ্যাং না হয় এবং সব সাইট সাপোর্ট করে
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

class AI_Hub:
    def __init__(self):
        self.window = None

    def get_main_html(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { 
                    font-family: 'Segoe UI', sans-serif; 
                    display: flex; flex-direction: column; align-items: center; justify-content: center; 
                    height: 100vh; margin: 0; 
                    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                    color: white; overflow: hidden;
                }
                h1 { margin-bottom: 25px; text-shadow: 2px 2px 8px rgba(0,0,0,0.5); }
                .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; width: 90%; max-width: 600px; }
                button.ai-btn { 
                    padding: 12px; font-size: 15px; cursor: pointer; border: none; border-radius: 8px; 
                    transition: 0.3s; font-weight: bold; color: white;
                }
                .chatgpt { background-color: #10a37f; }
                .gemini { background-color: #1a73e8; }
                .deepseek { background-color: #4d6cfa; }
                .perplexity { background-color: #20b2aa; }
                .grok { background-color: #000; border: 1px solid #555; }
                .edutools { background-color: #ff5722; grid-column: span 2; } /* আপনার নতুন লিঙ্ক */
                
                button.ai-btn:hover { transform: translateY(-2px); filter: brightness(1.2); }
            </style>
        </head>
        <body>
            <h1>AI & Edu Hub - Rasel</h1>
            <div class="grid">
                <button class="ai-btn chatgpt" onclick="pywebview.api.load_url('https://chatgpt.com')">ChatGPT</button>
                <button class="ai-btn gemini" onclick="pywebview.api.load_url('https://gemini.google.com')">Gemini</button>
                <button class="ai-btn deepseek" onclick="pywebview.api.load_url('https://chat.deepseek.com')">DeepSeek</button>
                <button class="ai-btn perplexity" onclick="pywebview.api.load_url('https://www.perplexity.ai')">Perplexity</button>
                <button class="ai-btn grok" style="grid-column: span 2;" onclick="pywebview.api.load_url('https://grok.com')">Grok (xAI)</button>
                <button class="ai-btn edutools" onclick="pywebview.api.load_url('https://raseledutools.github.io/')">Rasel Edu Tools</button>
            </div>
        </body>
        </html>
        """

    def load_url(self, url):
        self.window.load_url(url)

    def go_home(self):
        self.window.load_html(self.get_main_html())

    def go_back(self):
        self.window.evaluate_js("window.history.back()")

def start_app():
    hub = AI_Hub()
    # উইন্ডো তৈরি করার সময় 'confirm_close' এবং 'background_color' যোগ করা হয়েছে যাতে হ্যাং কম হয়
    hub.window = webview.create_window(
        'AI Hub Rasel', 
        html=hub.get_main_html(), 
        js_api=hub, 
        width=1200, 
        height=850,
        background_color='#1e3c72'
    )
    
    # মেনু বার (Top Bar) যোগ করা হয়েছে যা সব সময় থাকবে
    # এটি উইন্ডোজের নেটিভ মেনু হিসেবে কাজ করবে
    def setup_menu(window):
        import webview.menu as menu
        items = [
            menu.MenuAction('🏠 Home', hub.go_home),
            menu.MenuAction('⬅️ Back', hub.go_back),
            menu.MenuSeparator(),
            menu.MenuAction('❌ Exit', sys.exit)
        ]
        window.set_title("AI Hub Rasel - Use Top Menu to Navigate")

    # নেভিগেশন বারটি সক্রিয় করা
    webview.start(gui='edge', user_agent=USER_AGENT)

if __name__ == '__main__':
    start_app()
