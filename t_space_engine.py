# =============================================================
# THE T-SPACE THEORY: COMPUTATIONAL ENGINE
# Developed by: DefinitelyNotNaL
# Legal Concept Fixation: February 21, 2026
# =============================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib import cm

# ===============================
# CONFIGURATION
# ===============================

ITERATIONS = 35              # Growth steps (Axis X - Time)
BRANCH_PROB = 0.2            # Probability of quantum divergence
E_OBS_INITIAL = 5.0          # Initial Observation Energy (E_obs)
GRAVITY_FACTOR = 0.03        # Impact of Causal Depth (Axis Z)
DRY_LIMIT = 6                # Steps without energy before "withering"
ENERGY_DECAY = 0.98          # Energy dissipation per step
MAX_BRANCHES = 2             # Max new branches per node

# ===============================
# NODE ARCHITECTURE
# ===============================

class Node:
    def __init__(self, x, y, z, parent=None, energy=E_OBS_INITIAL):
        self.x = x
        self.y = y
        self.z = z
        self.parent = parent
        self.children = []
        self.energy = energy
        self.dry_counter = 0
        self.alive = True
        self.depth = 0 if parent is None else parent.depth + 1

    def m_trunk(self):
        """
        Causal Inertia (M_trunk) — increases with the established history
        """
        return self.depth + 1

    def update_energy(self):
        """
        Entropy logic: Energy decays unless observed
        """
        if self.energy > 0:
            self.energy *= ENERGY_DECAY
            self.dry_counter = 0
        else:
            self.dry_counter += 1
            if self.dry_counter > DRY_LIMIT:
                self.alive = False


# ===============================
# GROWTH LOGIC (T-SPACE DYNAMICS)
# ===============================

def grow_tree():
    root = Node(0, 0, 0)
    nodes = [root]

    for t in range(ITERATIONS):
        new_nodes = []

        for node in nodes:
            if not node.alive:
                continue

            node.update_energy()

            if not node.alive:
                continue

            # Relativistic Time Dilation: Time (delta_x) slows as Causal Depth (z) increases
            delta_x = 1 / (1 + GRAVITY_FACTOR * node.z)

            # Branching Logic: Probability of creating a new Y-vector
            if random.random() < BRANCH_PROB:

                branches = random.randint(1, MAX_BRANCHES)

                for _ in range(branches):
                    m_inertia = node.m_trunk()

                    # Navigator's Formula: delta_y = E_obs / M_trunk
                    delta_y = node.energy / m_inertia

                    # Quantum directionality
                    direction = random.choice([-1, 1])

                    new_x = node.x + delta_x
                    new_y = node.y + direction * delta_y
                    new_z = node.z + random.uniform(0, 1)

                    child = Node(new_x, new_y, new_z,
                                 parent=node,
                                 energy=node.energy)

                    node.children.append(child)
                    new_nodes.append(child)

        nodes.extend(new_nodes)

    return nodes


# ===============================
# VISUALIZATION ENGINE
# ===============================

def plot_t_space(nodes, color_mode="energy"):
    fig = plt.figure(figsize=(12, 8), facecolor='#111111')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#111111')

    for node in nodes:
        if node.parent is not None:
            # Color mapping based on Theory parameters
            if color_mode == "energy":
                color_value = node.energy
                color = cm.plasma(color_value / E_OBS_INITIAL)
            elif color_mode == "depth":
                color_value = node.z
                color = cm.viridis(color_value / max(n.z for n in nodes))

            alpha = 1.0 if node.alive else 0.1  # Dead branches become transparent

            ax.plot(
                [node.parent.x, node.x],
                [node.parent.y, node.y],
                [node.parent.z, node.z],
                color=color,
                alpha=alpha,
                linewidth=1
            )

    # Labeling based on the T-Space Manifesto
    ax.set_xlabel("X (Linear Time / Trunk)", color='white')
    ax.set_ylabel("Y (Quantum Probability / Branches)", color='white')
    ax.set_zlabel("Z (Causal Depth / Roots)", color='white')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')

    plt.title("T-SPACE THEORY SIMULATION: THE MULTIVERSE ARCHITECTURE", color='cyan', fontsize=14)
    plt.show()


# ===============================
# EXECUTION
# ===============================

if __name__ == "__main__":
    t_nodes = grow_tree()
    plot_t_space(t_nodes, color_mode="energy")
