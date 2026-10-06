# E‑Commerce & Price‑Comparison Web App

A beginner‑friendly **Python Flask** project that showcases a simple e‑commerce storefront with price‑comparison features. The app demonstrates:

- Clean, responsive UI built with vanilla CSS (glassmorphism, modern typography)
- Product catalog loaded from a JSON file
- Individual product pages
- An API endpoint that returns price information for comparison
- Clear project structure ready to be pushed to GitHub

## Project Structure

```
 e‑commerce‑price‑comparison/
 ├── app.py                 # Flask application entry point
 ├── products.json          # Sample product data
 ├── requirements.txt       # Python dependencies
 ├── README.md              # This file
 ├── static/
 │   └── style.css          # UI styling (glassmorphism, gradients)
 └── templates/
     ├── base.html          # Base HTML layout
     ├── index.html         # Home page – product grid
     └── product.html       # Product detail page
```

## Getting Started

1. **Clone the repository** (or copy the project folder).
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   python app.py
   ```
4. Open your browser at `http://localhost:5000`.

## Design Highlights

- **Typography**: Google Font *Inter* for a clean, modern look.
- **Glassmorphism cards** with subtle blur and translucent backgrounds.
- **Responsive grid** that adapts to mobile, tablet, and desktop.
- **Hover animations** for product cards and buttons.

Feel free to extend the app – add a shopping cart, integrate real vendor APIs, or improve the UI.
