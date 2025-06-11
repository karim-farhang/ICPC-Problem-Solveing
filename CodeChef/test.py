pas = 'you will never know'
name = input('please enter a variable name:\n')
val = input('please enter a value for the variable :\n')
exec(f'{name} = {val}')
print(f'the value of your variable is now: {eval(name)}')
