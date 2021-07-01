# here we use the plot functionality that comes naturally with pandas 
(
    chickweight
    .assign(previous_weight = lambda x: x.groupby('chick')['weight'].shift(1))
    .assign(weight_increase = lambda x: x['weight']- x['previous_weight'])
    .fillna(0)
    .groupby('time')
    ['weight_increase'].mean()
    .plot(title='Average growth over time')
)
