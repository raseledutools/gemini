import webview
import sys

# শক্তিশালী ইউজার এজেন্ট
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
                .nav-bar {
                    position: fixed; top: 0; left: 0; width: 100%; height: 40px;
                    background: #333; display: flex; align-items: center; padding-left: 10px;
                    z-index: 9999; border-bottom: 1px solid #444;
                }
                .nav-btn {
                    background: #555; color: white; border: none; padding: 5px 15px;
                    margin-right: 10px; cursor: pointer; border-radius: 4px; font-size: 12px;
                }
                .nav-btn:hover { background: #777; }
                .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 50px; }
                button.ai-btn { 
                    padding: 15px 25px; font-size: 16px; cursor: pointer; border: none; border-radius: 12px; 
                    transition: 0.3s; font-weight: bold; color: white; min-width: 150px;
                }
                .chatgpt { background-color: #10a37f; }
                .gemini { background-color: #1a73e8; }
                .deepseek { background-color: #4d6cfa; }
                .perplexity { background-color: #20b2aa; }
                .grok { background-color: #000; border: 1px solid #555; }
                button.ai-btn:hover { transform: scale(1.05); filter: brightness(1.2); }
            </style>
        </head>
        <body>
            <div class="nav-bar">
                <button class="nav-btn" onclick="pywebview.api.go_home()">🏠 Home</button>
                <button class="nav-btn" onclick="pywebview.api.go_back()">⬅️ Back</button>
            </div>
            <h1>AI Super Hub - Rasel</h1>
            <div class="grid">
                <button class="ai-btn chatgpt" onclick="pywebview.api.load_url('https://chatgpt.com')">ChatGPT</button>
                <button class="ai-btn gemini" onclick="pywebview.api.load_url('https://gemini.google.com')">Gemini</button>
                <button class="ai-btn deepseek" onclick="pywebview.api.load_url('https://chat.deepseek.com')">DeepSeek</button>
                <button class="ai-btn perplexity" onclick="pywebview.api.load_url('https://www.perplexity.ai')">Perplexity</button>
                <button class="ai-btn grok" style="grid-column: span 2;" onclick="pywebview.api.load_url('https://grok.com')">Grok (xAI)</button>
            </div>
        </body>
        </html>
        """

    def load_url(self, url):
        # সাইট লোড করার সময় উপরে একটি ছোট নেভিগেশন বার ইনজেক্ট করা হবে
        self.window.load_url(url)

    def go_home(self):
        self.window.load_html(self.get_main_html())

    def go_back(self):
        # ব্রাউজারের হিস্টোরি অনুযায়ী পেছনে যাওয়া
        self.window.evaluate_js("window.history.back()")

def start_app():
    hub = AI_Hub()
    hub.window = webview.create_window(
        'AI Hub Rasel', 
        html=hub.get_main_html(), 
        js_api=hub, 
        width=1200, 
        height=850
    )
    
    # ইউজার এজেন্ট দিয়ে স্টার্ট করা
    webview.start(gui='edge', user_agent=USER_AGENT)

if __name__ == '__main__':
    start_app()
