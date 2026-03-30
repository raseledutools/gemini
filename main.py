import webview
import sys

# শক্তিশালী ইউজার এজেন্ট যাতে কোনো এআই ব্লক না করে
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

class AI_Hub:
    def __init__(self):
        self.main_window = None

    def load_url(self, title, url):
        # বর্তমান উইন্ডোতেই নতুন URL লোড করা এবং টাইটেল পরিবর্তন করা
        self.main_window.load_url(url)
        self.main_window.set_title(f"{title} - AI Hub Rasel")

    def go_home(self):
        # আবার মেইন মেনু (HTML) লোড করা
        self.main_window.load_html(self.get_main_html())
        self.main_window.set_title("AI Hub - Select Assistant")

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
                    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
                    color: white; overflow: hidden;
                }
                h1 { margin-bottom: 25px; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); font-size: 28px; }
                .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; width: 90%; max-width: 500px; }
                button { 
                    padding: 15px; font-size: 16px; cursor: pointer; border: none; border-radius: 12px; 
                    transition: all 0.3s ease; font-weight: bold; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.2);
                }
                button:hover { transform: translateY(-3px); box-shadow: 0 8px 15px rgba(0,0,0,0.4); filter: brightness(1.2); }
                .chatgpt { background-color: #10a37f; }
                .gemini { background-color: #1a73e8; }
                .grok { background-color: #000000; border: 1px solid #333; }
                .deepseek { background-color: #4d6cfa; }
                .perplexity { background-color: #20b2aa; }
                .footer { position: absolute; bottom: 10px; font-size: 12px; opacity: 0.6; }
            </style>
        </head>
        <body>
            <h1>AI Super Hub</h1>
            <div class="grid">
                <button class="chatgpt" onclick="pywebview.api.load_url('ChatGPT', 'https://chatgpt.com')">ChatGPT</button>
                <button class="gemini" onclick="pywebview.api.load_url('Gemini', 'https://gemini.google.com')">Gemini</button>
                <button class="deepseek" onclick="pywebview.api.load_url('DeepSeek', 'https://chat.deepseek.com')">DeepSeek</button>
                <button class="perplexity" onclick="pywebview.api.load_url('Perplexity', 'https://www.perplexity.ai')">Perplexity</button>
                <button class="grok" style="grid-column: span 2;" onclick="pywebview.api.load_url('Grok', 'https://grok.com')">Grok (xAI)</button>
            </div>
            <p class="footer">Developed by Rasel</p>
        </body>
        </html>
        """

def start_app():
    hub = AI_Hub()
    
    # মেইন উইন্ডো তৈরি
    hub.main_window = webview.create_window(
        'AI Hub - Select Assistant', 
        html=hub.get_main_html(), 
        js_api=hub, 
        width=1100, 
        height=750
    )

    # রাইট ক্লিক মেনুতে 'Back to Home' বাটন যোগ করা (উইন্ডোজের জন্য)
    # অথবা আপনি কিবোর্ডের Alt+H চাপলে হোমে ফেরার ফাংশনালিটি চাইলেও যোগ করা যায়।
    # সহজ করার জন্য আমরা GUI-তেই একটি ব্যাক বাটন যোগ করার অপশন রাখছি।
    
    webview.start(gui='edge', user_agent=USER_AGENT, debug=True)

if __name__ == '__main__':
    start_app()
