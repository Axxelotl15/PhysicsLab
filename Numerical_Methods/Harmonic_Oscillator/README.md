# Harmonic Oscillator

My first computational physics project.

Topics explored:

- Euler Method
- Symplectic Euler Method
- Energy Conservation
- Phase Space
- Numerical Stability

---

# Harmonic Oscillator: Euler vs Symplectic Euler

## Objective

To investigate how different numerical integration methods simulate a simple harmonic oscillator and how they affect energy conservation.

## Physical System

The harmonic oscillator is described by:

dx/dt = v

dv/dt = -ω²x

The exact solution conserves total energy and traces a closed orbit in phase space.

## Methods Investigated

### 1. Standard Euler Method

Update equations:

x(n+1) = x(n) + dt·v(n)

v(n+1) = v(n) - dt·ω²·x(n)

Observation:

* Energy increases with time.
* Phase-space trajectory spirals outward.
* Numerical solution becomes unphysical.

### 2. Symplectic Euler Method

Update equations:

v(n+1) = v(n) - dt·ω²·x(n)

x(n+1) = x(n) + dt·v(n+1)

Observation:

* Energy remains bounded.
* Motion remains oscillatory.
* Long-term behavior is much closer to the true physical solution.

## Lessons Learned

* Small numerical errors can accumulate over time.
* Stability depends on the integration method.
* Preserving the geometric structure of a physical system is often more important than local accuracy.
* Symplectic methods are particularly useful for Hamiltonian systems because they preserve phase-space structure.

## Concepts Explored

* Harmonic Oscillator
* Numerical Integration
* Euler Method
* Symplectic Euler Method
* Energy Conservation
* Phase Space
* Stability Analysis
* Eigenvalues
* Hamiltonian Systems
