import numpy as np
import matplotlib.pyplot as plt

def simulate_quantum_rattle(iterations=1000, causal_depth_z=1.0):
    """
    Симуляция аномального дребезжания в T-Space.
    X - Линейное время (ствол)
    Y - Квантовая вероятность (ветви) 
    Z - Каузальная плотность (корни/гравитация)
    """
    # Начальные координаты в 5D-проекции
    x, y, z = [0], [0], [causal_depth_z]
    
    # Коэффициент блокировки времени (горизонт событий)
    # В классике тут всё застывает. В T-Space - нет.
    time_flow_rate = max(0, 1 - (1 / causal_depth_z)) 
    
    for _ in range(iterations):
        # 1. Смещение по X (зависит от каузальной плотности)
        new_x = x[-1] + time_flow_rate * 0.1
        
        # 2. Дребезжание по Y (Quantum Rattle)
        # Если время течет медленно, вероятность флуктуирует сильнее!
        rattle_amplitude = 1.0 / (time_flow_rate + 0.1) 
        new_y = y[-1] + np.random.normal(0, rattle_amplitude * 0.05)
        
        # 3. Каузальное давление по Z
        new_z = causal_depth_z # фиксируем для теста горизонта
        
        x.append(new_x)
        y.append(new_y)
        z.append(new_z)
        
    return np.array(x), np.array(y), np.array(z)

# Визуализация предсказания
x_vals, y_vals, _ = simulate_quantum_rattle(causal_depth_z=1.0001) # Почти на горизонте

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label='T-Space Particle Path', color='#ff00ff')
plt.title("Quantum Rattle: Behavior at dT_x ≈ 0 (Event Horizon)")
plt.xlabel("Linear Time (Axis X: The Trunk)")
plt.ylabel("Probability Branching (Axis Y: The Branches)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

print("Прогноз: На горизонте событий наблюдается 'вертикальное' мерцание без движения во времени.")
