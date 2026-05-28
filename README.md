# MindCode Academy

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/UI-Flet%20%28Flutter%29-purple.svg)](https://flet.dev)
[![License](https://img.shields.io/badge/License-Privacy%20Protected-green.svg)](#)

**MindCode Academy** is a cross-platform mobile application designed for interactive programming language learning. The concept combines a rigorous motivation system (gamification) with a built-in architecture for an AI-Mentor tasked with generating and verifying practical code assignments.

---

## 🔥 Key Features

* **Dynamic Customization (Color Picker):** Users can change the accent colors of the interface on the fly while maintaining UI depth and contrast (Material 3 / Dark Mode design language).
* **Gamification & Penalty System:** Implements strict discipline control. Submitting a correct solution awards **+25 XP**, while skipping tasks deducts **-30 XP**. If the experience rating drops critically low, the ProgressBar dynamically switches its color to red.
* **AI-Mentor Integration:** Features a pre-configured layout and logic to support seamless API integration (e.g., Google Gemini) for syntax analysis, code reviews, and rendering bug reports directly on the screen.
* **Legal Compliance:** Includes an integrated interactive *Privacy Policy* modal, which regulates local data management and secures the source code transmission process during analysis.

---

## 🛠 Tech Stack

* **Core Language:** Python 3.11+
* **UI Framework:** Flet (powered by the Flutter engine for native UI rendering)
* **State Management:** Non-linear state updates (asynchronous component re-rendering without application restarts)

---

## 📂 Repository Structure

```text
├── app.py                # Main executable application script
└── README.md             # Project documentation
