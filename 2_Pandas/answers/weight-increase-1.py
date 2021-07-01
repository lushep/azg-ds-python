
(
    chickweight
    .assign(previous_weight = lambda x: x.groupby('chick')['weight'].shift(1))
)

