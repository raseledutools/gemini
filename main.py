name: Gemini EXE Builder

on: [push]

jobs:
  build:
    runs-on: windows-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip' # দ্রুত বিল্ড হওয়ার জন্য ক্যাশ অন করা হলো

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pyinstaller pywebview[gui]

      - name: Check if main.py exists
        run: dir # ফোল্ডারে ফাইলগুলো আছে কিনা তা দেখার জন্য (Debug)

      - name: Build EXE with PyInstaller
        run: |
          pyinstaller --onefile --noconsole --name "Gemini_Rasel" main.py

      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: Gemini-Software
          path: dist/Gemini_Rasel.exe
