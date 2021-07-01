(
    chickweight
    .assign(diff = lambda df: df['weight'] - df.groupby('chick')['weight'].shift())
    .fillna(0)
    .groupby(['time', 'diet'])
    .agg(mean_weight_increase=pd.NamedAgg(column='diff', aggfunc='mean'))
    .unstack()
    ['mean_weight_increase']
    .plot(title='Average Growth over Time', ylabel='Growth')
);