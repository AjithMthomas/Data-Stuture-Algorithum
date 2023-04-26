import pandas as pd

dictionary = {
    "Employee": {
        "dave": {'id': 1, 'branch': 'backend', 'gender': 'male'},
        "mary": {'id': 2, 'branch': 'frontend', 'gender': 'female'}
    }
}
dictionar = pd.DataFrame(dictionary['Employee']).T
print(dictionar)


