import numpy as np

tmp_data = []

# "sepal_length","sepal_width","petal_length","petal_width","class"
with open('data.txt', 'r') as f:
  for line in f.readlines()[1:]:
    tmp = line.split(',')
    for ind in range(len(tmp)):
      if '\n' in tmp[ind]:
        tmp[ind] = tmp[ind].replace('\n', '')
      else:
        tmp[ind] = float(tmp[ind])
    tmp_data.append(tmp)


print(tmp_data[0][1:41][:4])
iris_data = np.empty([120, 4])
print(tmp_data[1:41][:3])

iris_data[:40, :] = tmp_data[0][1:41][:4]
print(iris_data)