file_name = "/home/ubuntu/PycharmProjects/Kmeans/venv/Data/seeds.csv"
test = Kmeans(file_name,k=5)
print("seeds数据集","迭代次数:",test.loop_for_n_times(n=10000))
test.show_result()

print('\n')

file_name = "/home/ubuntu/PycharmProjects/Kmeans/venv/Data/HTRU_2.csv"
test = Kmeans(file_name,k=2)
print("HTRU数据集","迭代次数:",test.loop_for_n_times(n=10000))
test.show_result()