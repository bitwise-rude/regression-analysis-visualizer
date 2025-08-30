
---
# Regression Analysis Simulator and Visualizer

This project is a **Python-based regression visualizer** built with **Pygame**.
It simulates **linear regression analysis** by plotting data points on a grid and displaying the **best-fit line**.

---

##  Features

* Draws a **graph-paper style grid** (with x and y axes).
* Scatters given **data points (X, Y)** on the screen.
* Labels each data point with its coordinates.
* Computes the **line of best fit** using the least-squares method.
* Plots the regression line dynamically on the graph.

---

##  File Structure

* `main.py` → The main program (this file).
* `constants.py` → Stores screen dimensions, colors, scales, and other constants.
* `data.py` → Contains the sample dataset (`X`, `Y`) for plotting.

---

##  How It Works

1. The program initializes a **Pygame window**.

2. It draws **axes and a grid**.

3. Data points from `data.py` are scattered on the screen.

4. Using **linear regression formula**:

   * Slope:

     $$
     m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
     $$

   * Intercept:

     $$
     b = \bar{y} - m\bar{x}
     $$

   * Best fit line:

     $$
     y = mx + b
     $$

5. The program finds the **endpoints of the line segment** within the range of `X`.

6. The line is plotted over the data points.

---

## ▶ Running the Program
### Requirements

* Python 3.x
* Pygame (`pip install pygame`)

### Run

```bash
python main.py
```

---

##  Example Output

* A window opens with:

  * Red **axes**.
  * White **data points** (with labels).
  * A blue **best-fit regression line**.

---

##  Use Case (Exam Context)

This project demonstrates:

* **Scatter plots** in statistics.
* **Linear regression (Least Squares Approximation)**.
* **Graphical representation of statistical data**.

It can be extended for:

* Multiple datasets.
* Real-time regression visualization.
* Non-linear regression methods.

