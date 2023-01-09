def group_by_owners(files):
    files2 = {}
    for f,o in files.items():
        files2.setdefault(o,[]).append(f)
    return files2
    
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}   
print(group_by_owners(files))

