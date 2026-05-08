# ASCII Art Generator 🎨

A command-line tool that transforms any text into stylized ASCII art using hundreds of font styles — powered by Python and pyfiglet.

---

## 🚀 Features

- Convert any text into ASCII art instantly
- Choose from **hundreds of available fonts**
- **Random font mode** — get a surprise style every time
- Clean error handling and user friendly messages
- Lightweight — runs entirely in the terminal

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Library:** pyfiglet

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ascii-art-generator.git
cd ascii-art-generator
```

2. Install dependencies:
```bash
pip install pyfiglet
```

---

## 📖 Usage

### Random Font Mode
```bash
python figlet.py
```

### Specific Font Mode
```bash
python figlet.py -f slant
python figlet.py --font banner
```

---

## 💡 Example Output

```
Using random font: slant

Input: Hello

    __  __     ____
   / / / /__  / / /___
  / /_/ / _ \/ / / __ \
 / __  /  __/ / / /_/ /
/_/ /_/\___/_/_/\____/
```

---

## 📁 Project Structure

```
ascii-art-generator/
│
├── figlet.py       # Main CLI application
├── README.md       # Project documentation
└── requirements.txt
```

---

## 📦 Requirements

```
pyfiglet
```

---

## 🔮 Future Improvements

- Add color output support using `colorama`
- Save ASCII art output to a `.txt` file
- Add a `--list` flag to display all available fonts
- Build a web interface version

---

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
