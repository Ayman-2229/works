# Styles and Components Mapping

This document lists the CSS selectors defined in `styles.css` and their corresponding UI components or source files in the project. This will help you easily identify and edit styles related to each component.

---

## General Page

- **CSS Selector:** `body`
- **Description:** Overall page background, font color, and font family.
- **Corresponding File:** `main.py` (overall app layout)

---

## App Title

- **CSS Selector:** `.app-title`, `.app-title h1`, `.app-title p`
- **Description:** Styles for the main app title and subtitle.
- **Corresponding File:** `main.py` (app title section)

---

## Upload Section

- **CSS Selector:** `.stFileUploader`
- **Description:** Styles for the file uploader UI.
- **Corresponding File:** `main.py` (file uploader UI)

---

## Dataframe Styling

- **CSS Selector:** `[data-testid="stDataFrame"]`
- **Description:** Styling for displayed dataframes.
- **Corresponding Files:** `main.py`, `components/file_parser.py` (dataframe display)

---

## Buttons

- **CSS Selector:** `button`
- **Description:** Styles for buttons used across the app.
- **Corresponding Files:** `main.py`, `components/budget_coach.py`, `components/ai_categorizer.py` (buttons in various components)

---

## Sidebar

- **CSS Selector:** `section[data-testid="stSidebar"]`
- **Description:** Sidebar background styling.
- **Corresponding File:** `main.py` (sidebar UI)

---

## Success and Info Boxes

- **CSS Selector:** `.stAlert`
- **Description:** Styling for alert and info message boxes.
- **Corresponding Files:** `main.py`, `utils/visuals.py` (alert and info messages)

---

# Notes

- The CSS selectors mostly target Streamlit UI elements and custom app components.
- For detailed UI changes, refer to the corresponding Python files listed above.
- This mapping helps centralize style editing and understanding of UI structure.
