
# Stocks Telegram Bot 📈🤖

A Python-based Telegram bot that provides users with real-time stock market information and alerts, built using the `python-telegram-bot` library and integrated with the **Nobitex** API for data processing.

---

## 🚀 Features
- **Real-Time Stock Updates**: Fetches live stock market data.  
- **Price Alerts**: Notifies users when stocks hit predefined thresholds.  
- **User-Friendly Commands**: Intuitive commands for easy interaction.  
- **Redis Integration**: Efficient caching for quick responses.  
- **Job Queue**: Automated tasks for alerts and updates.  

---

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Bot Commands](#bot-commands)
- [Contributing](#contributing)
- [License](#license)
- [Feedback & Support](#feedback--support)
- [Acknowledgments](#acknowledgments)

---

## 🛠️ Getting Started

Follow these instructions to set up and run the bot on your local machine.

### Prerequisites
- [Python](https://www.python.org/) (version 3.10 or later)
- [Redis](https://redis.io/) (for caching and job queue)
- API key for **Nobitex**

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/The-Samyar/stocks-telegram-bot.git
   cd stocks-telegram-bot
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Configure the `.env` file:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     NOBITEX_API_KEY=your_nobitex_api_key
     REDIS_HOST=localhost
     REDIS_PORT=6379
     ```

4. Start the Redis server:
   ```bash
   redis-server
   ```

5. Run the bot:
   ```bash
   poetry run python bot.py
   ```

---

## 🤖 Bot Commands

The bot supports the following commands:

- `/start` - Welcome message and instructions for usage.  
- `/help` - List of available commands.  
- `/price <symbol>` - Get the current price of a stock or cryptocurrency.  
- `/alert <symbol> <price>` - Set a price alert for a stock or cryptocurrency.  
- `/remove_alert <alert_id>` - Remove an existing alert.  
- `/list_alerts` - List all active alerts.  

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐ Acknowledgments

- Powered by the **Nobitex** API.  
- Built with the **python-telegram-bot** library.  
- Special thanks to the open-source community!

---

### 🙌 Let's Build Together!  
If you find this project helpful, give it a ⭐ and share it with others!
