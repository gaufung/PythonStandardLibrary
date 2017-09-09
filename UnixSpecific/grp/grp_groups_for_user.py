
import grp

username = 'gaufung'
group_names = set(
    g.gr_name
    for g in grp.getgrall()
    if username in g.gr_mem
)
print(username, 'belongs to:', ', '.join(sorted(group_names)))