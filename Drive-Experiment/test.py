infile = file('dikb-update_backup_may2016.py')
newopen = open('dikb-update.py', 'w')

for line in infile :
     if 'a.assert_by_default' not in line:
            newopen.write(line) 
