import webview
import sys

def create_window():
    # এখানে টাইটেল এবং URL দেওয়া হয়েছে
    # width এবং height সেট করা হয়েছে যাতে উইন্ডোটি সুন্দর দেখায়
    window = webview.create_window(
        'Gemini Rasel', 
        'https://gemini.google.com',
        width=1200,
        height=800,
        resizable=True,
        confirm_close=True
    )
    
    # gui='edge' ব্যবহার করা হয়েছে উইন্ডোজের WebView2 ইঞ্জিন নিশ্চিত করতে
    webview.start(gui='edge')

if __name__ == '__main__':
    try:
        create_window()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
