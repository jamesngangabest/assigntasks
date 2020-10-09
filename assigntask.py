from random import shuffle
task_list = ['task_1', 'task_2', 'task_3', 'task_4', 
             'task_5', 'task_6',  'task_7','task_8',
             'task_9', 'task_10', 'task_11', 'task_12',
             'task_13', 'task_14', 'task_15', 'task_16']

shuffle(task_list)
print ('task_list')
personA_tasks = task_list[0:4]
personB_tasks = task_list[4:8]
personC_tasks = task_list[8:12]
personD_tasks = task_list[12:]

print ('personA_tasks')
print ('personB_tasks')
print ('personC_tasks')
print ('personD_tasks')