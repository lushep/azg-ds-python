new_avg_weight_by_time = (
    new_chickweight
    .groupby(['time'])
    [['weight_increase']]
    .mean()
    .reset_index()
)
new_avg_weight_by_time.plot('time', 'weight_increase', kind = 'scatter' , title = 'weight increase over time',legend = False);

new_avg_weight_by_diet_time = (
    new_chickweight
    .groupby(['diet', 'time'])
    [['weight_increase']]
    .mean()
    .reset_index()
)



# +
fig, ax = plt.subplots()

colors = ['blue','red','green','orange']

for diet in range(1,5):
    (
    new_avg_weight_by_diet_time
    .loc[lambda df: df['diet'] == diet]
    .plot('time', 'weight_increase', ax = ax, c = colors[diet - 1], label = f'diet {diet}')
    );
    
# -

ax.set_xticks(range(2, 22, 2))
ax.set_xlabel('time')
ax.set_ylabel('weight gain')
ax.set_title('something really strange occurs at timestep 14')
ax.legend(loc='upper left');
