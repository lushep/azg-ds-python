chickweight['time'].unique()
# Since chickens have a short lifespan, time probably represents number of days

print(
    'Min chick weight:', chickweight['weight'].min(),
    '\nMax chick weight:', chickweight['weight'].max()
)