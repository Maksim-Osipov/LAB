import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
a = []
file = open("exp.txt", "r")
for line in file:
    line = line.strip() #удаляю символ \n в конце каждой строки
    a.append(line) #добавляю строку файла в массив
a = a[2:4002] #удаляю строки 0, 1 и 4002, потому что на них не числа, а текст
for i in range(4000):
    a[i] = int(a[i]) #преобразую каждый символ массива в число, не нашла способ сделать это красивее
file.close()

def Histogram(k, color): #функция, которая зависит только от тау (k) и цвета (каждая гистограмма своего цвета)
    print(f"tau = {k}")
    arr = [] #массив, в который будет записываться сумма каждых тау отсчетов (тау = 1, 10, 20, 40 (см ниже))
    n = 4000 #количество отсчетов
    for i in range(int(n/k)):
        h = 0
        for j in range(k):
            h+=a[j+i*k] #h - это сумма k подряд идущих чисел
        arr.append(h)
    lam = np.mean(arr) #параметр, который используется в рсапределении Пуассона (см теорию), равен среднему значению массива данных
    print(f"среднее число регистрируемых частиц = {lam}\nсреднеквадратичное отклонение = {np.sqrt(lam)}погрешность среднeго значения = {np.sqrt(lam/k)}\nсредняя интенсивность регистрируемых частиц в секунду = {lam/k}")
    sigma = [] #масиив отклонений от среднего
    for i in range(int(n/k)):
        sigma.append(abs(arr[i] - lam))
    sigma_mean = np.mean(sigma)
    print(f"среднее отклонение в эксперименте = {sigma_mean}") #в прошлом принте считала сигму на корень из n, в этом по определению как средее отклонение от среднего (по модулю)
    counter = 0 #счетчик, чтобы послитать долю случаев, когда значения попадают в интервал от n-сигма до n+сигма
    for i in range(int(n/k)):
        if abs(arr[i] - lam) < sigma_mean:
            counter +=1
    print(f"доля случаев, когда отклонение числа отсчётов от среднего значения не превышает стандартного отклонения = {counter/(n/k)}")
    k_values = np.arange(0, max(arr)+1) #массив, который используется для построения распределения Пуассона
    pmf_values = poisson.pmf(k_values, lam) #функция, которая выдает массив значений, которые соответствуют точкам из k_values
    plt.hist(arr, bins=max(arr) - min(arr), density=True, align="left", color=color, edgecolor="black") #построение гистограммы, параметры: массив данных, границы массива, нормализация, расположение столбцов, цвет столбцов, цвет границ
    plt.plot(k_values, pmf_values, 'bo-', color='#00FF00') #отрисовка распределения Пуассона
    plt.xlabel('Количество событий')
    plt.ylabel('Частота')
Histogram(10, "cornflowerblue")
Histogram(20, '#EE82EE')
Histogram(40, '#EE9A49')
plt.show() #на одном рисунке будет 3 гистограммы
Histogram(1, '#3A5FCD')
plt.show()
Histogram(10, "cornflowerblue")
plt.show()
Histogram(20, '#EE82EE')
plt.show()
Histogram(40, '#EE9A49')
plt.show()