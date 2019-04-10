# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt
import test

p, n = test.import_experiment_data('data.tsv')
'''''
connective = p
for idx, num in enumerate(p):
    connective[idx] = (p[idx] * (4 ** (idx + 1))) ** (1/(idx + 1))
'''''
# Initialize the plot
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(111)
ax1.set_title('p_bar against n')
# ax2.set_title('connective constant against n')
# Plot the data
ax1.scatter(n, p)
# ax2.scatter(connective, n)

plt.tight_layout()
# Show the plot
plt.savefig('p_n_fig.png')