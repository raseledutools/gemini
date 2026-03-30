import webview
import sys

# তোমার SAE Book ওয়েবসাইটের লিঙ্ক
URL = 'https://raseledutools.github.io/sae-book/'

def create_app():
    # উইন্ডো তৈরি করা
    window = webview.create_window(
        'Essential tools - Rasel Mia', 
        URL,
        width=1280, 
        height=800,
        resizable=True,
        confirm_close=True
    )

    # ব্রাউজারের মতো নেভিগেশন বার ইনজেক্ট করা (CSS এবং JS দিয়ে)
    def inject_navigation_bar():
        custom_css = """
        #custom-nav-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 50px;
            background-color: #202124;
            display: flex;
            align-items: center;
            padding: 0 15px;
            z-index: 999999;
            border-bottom: 1px solid #3c4043;
            color: white;
            font-family: sans-serif;
            box-sizing: border-box;
        }
        .nav-btn {
            background: none;
            border: none;
            color: #e8eaed;
            padding: 8px;
            margin-right: 10px;
            cursor: pointer;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }
        .nav-btn:hover {
            background-color: #3c4043;
        }
        .nav-btn svg {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        .page-title {
            margin-left: 10px;
            font-size: 14px;
            color: #bdc1c6;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        /* পেজের কন্টেন্ট যেন বারের নিচে না ঢাকা পড়ে */
        body {
            margin-top: 50px !important;
        }
        """

        custom_html = """
        <div id="custom-nav-bar">
            <button class="nav-btn" onclick="window.history.back()" title="Back">
                <svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
            </button>
            <button class="nav-btn" onclick="window.history.forward()" title="Forward">
                <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </button>
            <button class="nav-btn" onclick="window.location.reload()" title="Reload">
                <svg viewBox="0 0 24 24"><path d="M17.65 6.35A7.958 7.958 0 0012 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/></svg>
            </button>
            <div class="page-title">SAE Book Hub | Google Gemini</div>
        </div>
        """

        # CSS ইনজেকশন
        window.evaluate_js(f"var style = document.createElement('style'); style.innerHTML = `{custom_css}`; document.head.appendChild(style);")
        # HTML ইনজেকশন
        window.evaluate_js(f"var div = document.createElement('div'); div.innerHTML = `{custom_html}`; document.body.prepend(div.firstChild);")

    # অ্যাপ স্টার্ট হলে নেভিগেশন বার ইনজেক্ট করবে
    webview.start(inject_navigation_bar, window)

if __name__ == '__main__':
    create_app()
