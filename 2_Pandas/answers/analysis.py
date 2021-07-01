
pltr = (
    chickweight
    .assign(delta=lambda df: df.groupby('chick')['weight'].transform(lambda df: df.diff()))
    .dropna()
)

agg = (
    pltr
    .groupby(['time', 'diet'])
    .apply(lambda df: pd.Series({'mean_delta': np.mean(df['delta'])})).reset_index()
)


fig, ax = plt.subplots(figsize=(10, 8))

pltr.plot('time', 'delta', kind='scatter', legend=False, ax=ax)

for diet, diet_df in agg.groupby('diet'): 
    diet_df.plot('time', 'mean_delta', label=f'diet {diet}', ax=ax, legend=False)

ax.set_xticks(range(2, 22, 2))
ax.set_xlabel('time')
ax.set_ylabel('weight gain')
ax.set_title('something really strange occurs at timestep 14')
ax.legend(loc='upper left');
