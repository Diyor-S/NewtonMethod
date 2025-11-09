# Independent Work №2: Approximate Solution of Nonlinear Equation Systems

## General Concept
This independent work focuses on the approximate solution of nonlinear equation systems using Newton's method. The student's variant number V is equal to their number in the stream list in the LMS system.

## Task Requirements

### 1. Methods for Approximate Solution of Nonlinear Equation Systems
Provide brief information about existing methods for approximate solution of nonlinear equation systems.

### 2. Newton's Method for Nonlinear Equation Systems
Provide detailed information about Newton's method for approximate solution of nonlinear equation systems.

### 3. Analytical and Approximate Solution
Approximately solve the given nonlinear equation system using Newton's method with given accuracy ε. Solve one solution analytically.

### 4. Programming Implementation
Create a program for this method (programming language is optional). Find the remaining solutions through the program. Provide the program code and screenshots of the solutions obtained by the program.

### 5. Defense of Independent Work
During the defense of the independent work, the student must personally demonstrate obtaining the solution through the program.

---

## Problem Statement

For **Variant V = 18**, solve the following nonlinear equation system with accuracy **ε = 0.0018**:

### System of Equations:

$$
\begin{cases}
\frac{19}{2} \cdot x^2 + \frac{20}{4} \cdot y^2 - \frac{21}{5} \cdot x \cdot y = 18 \\
\frac{20}{5} \cdot x^2 + \frac{21}{3} \cdot y^2 + \frac{23}{4} \cdot x \cdot y = 18
\end{cases}
$$

### Simplified Form:

$$
\begin{cases}
9.5x^2 + 5y^2 - 4.2xy = 18 \\
4x^2 + 7y^2 + 5.75xy = 18
\end{cases}
$$

---

## 1. Methods for Approximate Solution of Nonlinear Equation Systems

Nonlinear equation systems of the form **F(x) = 0**, where **F: ℝⁿ → ℝⁿ**, require iterative methods for their solution since analytical solutions are rarely available. The main approaches include:

### Fixed-Point Iteration Method
This method transforms the system **F(x) = 0** into an equivalent form **x = G(x)** and constructs the iterative sequence **xₖ₊₁ = G(xₖ)**. Convergence is guaranteed when the spectral radius of the Jacobian of **G** is less than 1 in the neighborhood of the solution. The method is simple to implement but has slow linear convergence.

### Newton's Method (Newton-Raphson)
The most widely used method, which linearizes the system at each iteration using the Jacobian matrix. It exhibits quadratic convergence near the solution, making it highly efficient when a good initial approximation is available. However, it requires computation of the Jacobian at each iteration.

### Quasi-Newton Methods
These methods (such as Broyden's method) approximate the Jacobian matrix instead of computing it explicitly, reducing computational cost. They maintain superlinear convergence while avoiding expensive derivative calculations, making them practical for large-scale problems.

### Successive Over-Relaxation (SOR)
An extension of the Gauss-Seidel method that introduces a relaxation parameter to accelerate convergence. It decomposes the Jacobian matrix and iteratively refines the solution. The method is particularly effective for systems arising from discretized partial differential equations.

### Gradient Descent and Conjugate Gradient Methods
These methods minimize the residual norm **||F(x)||²** by treating the system as an optimization problem. They are robust but typically exhibit slower convergence compared to Newton-type methods. They are useful when the Jacobian is difficult to compute or singular.

### Continuation (Homotopy) Methods
These methods construct a continuous path from an easy-to-solve problem to the target problem using a parameter **t ∈ [0,1]**. They can handle difficult initial value problems and avoid local minima, though they require solving a sequence of systems along the path.

---

## 2. Newton's Method for Nonlinear Equation Systems

### Mathematical Foundation

Newton's method extends the scalar Newton-Raphson method to systems of equations. For a system **F(x) = 0** where **F: ℝⁿ → ℝⁿ**, the method linearizes **F** at the current approximation **xₖ** using a first-order Taylor expansion:

**F(xₖ + Δx) ≈ F(xₖ) + J(xₖ)Δx**

where **J(xₖ)** is the Jacobian matrix with elements **Jᵢⱼ = ∂Fᵢ/∂xⱼ** evaluated at **xₖ**.

### Iterative Algorithm

The method generates a sequence of approximations through the following steps:

1. **Start** with an initial guess **x₀** (preferably close to the solution)
2. **Compute** the Jacobian matrix **J(xₖ)** at the current point
3. **Solve** the linear system: **J(xₖ)Δxₖ = -F(xₖ)**
4. **Update** the solution: **xₖ₊₁ = xₖ + Δxₖ**
5. **Check** convergence: if **||F(xₖ₊₁)|| < ε** or **||Δxₖ|| < ε**, stop; otherwise return to step 2

### Convergence Properties

**Convergence Rate:** When the initial approximation is sufficiently close to the solution and the Jacobian is non-singular at the solution, Newton's method exhibits **quadratic convergence**, meaning the error satisfies:

**||xₖ₊₁ - x*|| ≤ C||xₖ - x*||²**

This rapid convergence is the method's primary advantage, often requiring only 3-5 iterations for high precision.

**Convergence Conditions:**
- The Jacobian **J(x*)** must be non-singular at the solution
- The initial guess **x₀** must be sufficiently close to the solution
- The function **F** must be continuously differentiable

### Advantages and Disadvantages

**Advantages:**
- Quadratic convergence rate near the solution
- Well-established theoretical foundation
- Effective for well-conditioned problems
- Straightforward implementation

**Disadvantages:**
- Requires explicit computation of the Jacobian matrix (n² derivatives)
- Needs a good initial approximation for convergence
- May diverge if started far from the solution
- Computationally expensive for large systems (requires solving a linear system at each iteration)
- Fails when the Jacobian becomes singular or ill-conditioned

### Practical Considerations

In practice, modified versions of Newton's method are often employed:
- **Damped Newton's method** introduces a step size parameter to ensure global convergence
- **Inexact Newton methods** use iterative solvers for the linear system instead of direct methods
- **Finite difference approximations** can replace analytical Jacobian computation when derivatives are difficult to obtain