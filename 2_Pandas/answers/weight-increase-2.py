(
    chickweight
    .assign(previous_weight = lambda x: x.groupby('chick')['weight'].shift(1))
    .assign(weight_increase = lambda x: x['weight']- x['previous_weight'])
    .fillna(0)
    .drop(columns='previous_weight')
)

