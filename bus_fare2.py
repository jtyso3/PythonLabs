print(f'Total monthly bus fare for {total_trips} trips = ${grand_total:,.2f}.')
print('{:<14}{:>5}{:>12}{:>5}{:>14}{:>6}'.format('Type', 'Trips', '', 'Fares', '', 'Total'))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6.2f}'.format('Regular', reg_trips, '$', reg_fare, '$', reg_total))
print('{:<14}{:>5}{:>12}{:>5.2f}{:>14}{:>6,.2f}'.format('Rush', rush_trips, '$', rush_fare, '$', rush_total))
