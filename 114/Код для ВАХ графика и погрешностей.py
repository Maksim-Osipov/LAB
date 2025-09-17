import numpy as np
from matplotlib import pyplot as plt

# Опыт 1, l = 30
u1 = np.array([0.2202, 0.2416, 0.3345, 0.3954, 0.4856, 0.6264, 0.68, 0.87, 1.12])
i1_normal = 0.5*np.array([0.13, 0.15, 0.2, 0.28, 0.29, 0.37, 0.4, 0.51, 0.66])




# Опыт 2, l = 50
u2 = np.array([0.3223, 0.3414, 0.3856, 0.4265, 0.5554, 0.6302, 0.7204, 0.8806, 1.1516, 3.1617])
i2_normal = 0.5*np.array([0.11, 0.12, 0.14, 0.15, 0.2, 0.22, 0.26, 0.31, 0.4, 1.11])




# Опыт 3, l = 20
u3 = np.array([0.1415, 0.1665, 0.1810, 0.2115, 0.2317, 0.2664, 0.3006, 0.3676, 0.4708, 0.6809])
i3_normal = 0.5*np.array([0.13, 0.14, 0.16, 0.19, 0.21, 0.23, 0.26, 0.32, 0.36, 0.59])



# Функция для построения МНК через начало координат (x = k*y, так как теперь U = R*I)
def fit_through_origin(i, u, color, marker, label):
    # Метод наименьших квадратов через начало координат (x = k*y)
    k = np.sum(i * u) / np.sum(i * i)

    # Построение точек
    plt.scatter(i, u, color=color, marker=marker, s=60, alpha=0.7, label=label)

    # Построение линии регрессии через (0,0)
    i_fit = np.linspace(0, max(i) * 1.1, 100)
    u_fit = k * i_fit
    plt.plot(i_fit, u_fit, color=color, linestyle='--', alpha=0.8)

    return k


# Общий график с тремя наборами точек и линиями МНК через начало координат
plt.figure(figsize=(12, 8))

# Опыт 1 - синие точки (теперь U = R*I)
k1 = fit_through_origin(i1_normal, u1, 'blue', 'o', 'Опыт 1 (l=30)')

# Опыт 2 - красные точки
k2 = fit_through_origin(i2_normal, u2, 'red', 's', 'Опыт 2 (l=40)')

# Опыт 3 - зеленые точки
k3 = fit_through_origin(i3_normal, u3, 'green', '^', 'Опыт 3 (l=20)')

# Добавляем точку (0,0) для наглядности
plt.scatter(0, 0, color='black', marker='o', s=50, zorder=5)

# Настройки графика (оси поменялись местами)
plt.xlabel('Сила тока, I (А)', fontsize=12)
plt.ylabel('Напряжение, U (В)', fontsize=12)
plt.title('Зависимость напряжения от силы тока для проводников разной длины', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.xlim(-0.0005, max(max(i1_normal), max(i2_normal), max(i3_normal)) * 1.1)
plt.ylim(-0.05, max(max(u1), max(u2), max(u3)) * 1.1)
plt.tight_layout()

plt.show()

# Вывод коэффициентов (теперь k = R)
print("Коэффициенты аппроксимации (U = R·I):")
print("Опыт 1 (l=30): U = {:.4f}·I".format(k1))
print("Опыт 2 (l=50): U = {:.4f}·I".format(k2))
print("Опыт 3 (l=20): U = {:.4f}·I".format(k3))
print()

# Сопротивления (R = k)


# Погрешности измерений

r1 = 1 * k1 * (1 + k1 / (10 * 10 ** 6))
r2 = 1 * k2 * (1 + k2 / (10 * 10 ** 6))
r3 = 1 * k3 * (1 + k3 / (10 * 10 ** 6))

# Вывод сопротивлений (R = U/I = 1/k)
print("Сопротивления:")
print("Опыт 1 (l=30): R = {:.2f} Ом".format(r1))
print("Опыт 2 (l=50): R = {:.2f} Ом".format(r2))
print("Опыт 3 (l=20): R = {:.2f} Ом".format(r3))
print()

r1_eror_random = (1 / np.sqrt(len(u1))) * np.sqrt(np.mean(u1 ** 2) / np.mean(i1_normal ** 2) - r1 ** 2)
r2_eror_random = (1 / np.sqrt(len(u2))) * np.sqrt(np.mean(u2 ** 2) / np.mean(i2_normal ** 2) - r2 ** 2)
r3_eror_random = (1 / np.sqrt(len(u3))) * np.sqrt(np.mean(u3 ** 2) / np.mean(i3_normal ** 3) - r3 ** 2)

r1_eror_stat = r1 * np.sqrt(((1 / 1000) / (300 / 1000)) ** 2 + (0.4 / 99) ** 2)
r2_eror_stat  = r2 * np.sqrt(((1/1000)/(300/1000))**2 + (0.4/99)**2)
r3_eror_stat  = r3 * np.sqrt(((1/1000)/(300/1000))**2 + (0.4/99)**2)

r1_error = np.sqrt(r1_eror_random**2+r1_eror_stat**2)
r2_error = np.sqrt(r2_eror_random**2+r2_eror_stat**2)
r3_error = np.sqrt(r3_eror_random**2+r3_eror_stat**2)


print(r1,  r1_eror_random, r1_eror_stat,  r1_error)
print(r2,  r2_eror_random, r2_eror_stat,  r2_error)
print(r3,  r3_eror_random, r3_eror_stat,  r3_error)

data = np.array([35,37,36,36,36,35,35,37,37])
data = data/100
mean = np.mean(data)
std = np.std(data)
eror_mean = std /(np.sqrt(len(data)))
eror_micrometr = 0.01/2
eror_full = np.sqrt(eror_mean**2+eror_micrometr**2)
print(mean, std, eror_mean, eror_full)
s = np.pi * mean**2 /4
eror_s = 0.5*mean * eror_mean * np.pi
#ФИНАЛ
print(s, eror_s/s)


print('_'*10*6)
rho_1 = r1*s/(0.3)
rho_2 = r2*s/(0.5)
rho_3 = r3*s/(0.2)

print(rho_1, rho_2, rho_3)

eror_rho_1 = np.sqrt((r1_error/r1)**2+(eror_full/mean)**2+2*(0.01/0.3)**2)
eror_rho_2 = np.sqrt((r2_error/r2)**2+(eror_full/mean)**2+2*(0.01/0.5)**2)
eror_rho_3 = np.sqrt((r3_error/r3)**2+(eror_full/mean)**2+2*(0.01/0.2)**2)


print('_'*10*6)



print(eror_rho_1*100)
print(eror_rho_2*100)
print(eror_rho_3*100)