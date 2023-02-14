import numpy as np
import scipy.stats as stats

# Определение выборки
mothers_height = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]
daughters_height = [173, 175, 162, 174, 175, 168, 155, 170, 160]

# Расчет средних значений
mean_mothers_height = np.mean(mothers_height)
mean_daughters_height = np.mean(daughters_height)

# Расчет отклонения
std_mothers_height = np.std(mothers_height, ddof=1)
std_daughters_height = np.std(daughters_height, ddof=1)

# Расчет количества элементов выборки
n_mothers = len(mothers_height)
n_daughters = len(daughters_height)

# Calculate the t-statistic
t_statistic, p_value = stats.ttest_ind_from_stats(mean_mothers_height, std_mothers_height, n_mothers, mean_daughters_height, std_daughters_height, n_daughters, equal_var=False)

# Оценка p-value
if p_value < 0.05:
    print("Нулевая гипотеза опровергнута. Имеются существенные отличия в росте матерей и дочерей")
else:
    print("Нулевая гипотеза подтверждена. Нет существенных отличий в росте матерей и дочерей.")
