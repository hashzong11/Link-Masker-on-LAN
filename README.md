🔗 LAN Link Masker (Flask)

A simple link masking tool built with Python’s Flask framework.
It runs on your Local Area Network (LAN), allowing devices connected to the same Wi-Fi or network to access short masked links that redirect to real URLs.

🚀 Features

Mask long URLs into short, easy-to-remember aliases

Works on any device connected to the same LAN

Lightweight and fast (powered by Flask)

Easily customizable (add your own aliases in a dictionary)

⚙️ How It Works

Define aliases in a Python dictionary, for example:

"yt" → https://youtube.com
"gh" → https://github.com


Run the Flask server on 0.0.0.0 so it’s accessible across your LAN.

Other devices on the same Wi-Fi can open:

http://192.168.1.5:5000/yt → YouTube

http://192.168.1.5:5000/gh → GitHub

🛠️ Installation & Usage

Clone the repo:

git clone https://github.com/your-username/lan-link-masker.git
cd lan-link-masker


Install dependencies:

pip install flask


Run the server:

python app.py


Find your LAN IP (e.g., 192.168.1.5) and open in browser:

http://192.168.1.5:5000/yt

📌 Example

Visiting: http://192.168.1.5:5000/yt
→ Redirects to: https://youtube.com

Visiting: http://192.168.1.5:5000/gh
→ Redirects to: https://github.com

🔮 Future Improvements

Web interface to add/remove masked links dynamically

Database support instead of hardcoded dictionary

Custom error pages for unknown aliases

📄 License

This project is licensed under the MIT License – feel free to use and modify
