# **LineFormatter**

A lightweight command-line tool for generating and simplifying the equation of a line from a point and a gradient (slope).
Useful for math homework and speeding up coordinate geometry problems.

---

## ✨ Features

* Converts point-slope info *(x₁, y₁, m)* into:

  * **Slope-intercept form**: `y = mx + c`
  * **Standard form**: `Ax + By = C`
* Automatically simplifies:

  * Fractions
  * Signs (no ugly `+ -4`)
  * Negative intercepts
  * Common divisors (e.g. `2x - 4y = 8 → x - 2y = 4`)
* Handles cases like:

  * Fraction slopes (e.g. `0.5 → 1/2`)
  * Zero intercept
  * Negative gradients
* Clean output formatting

---

## 🧠 Example usage

Run:

```bash
python LineFormatter.py
```

Input:

```
Enter x1: 3
Enter y1: -2
Enter the gradient (m): 0.5
```

Output:

```
Equation of the line:
Slope-intercept form: y = 1/2x - 7/2
Standard form: x - 2y = 7
```

---

## 📦 Requirements

* Python 3.x
* Uses only standard library (`fractions`)

---

## 🧠 Why I made it

Rearranging line equations manually and simplifying fractions repeatedly was getting repetitive and annoying while doing homework, so I wrote a script to do the formatting for me automatically.

---

## 🚀 Future ideas

* Vertical line handling (`x = constant`)
* Support for two-point input
* Option to output LaTeX format for school reports

---

## 🤝 Contributions
PRs welcome. Suggestions for improvement or edge-case testing appreciated.

