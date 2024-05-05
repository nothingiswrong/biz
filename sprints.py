from collections import deque

sprint_capacity = 20 #количество часов в таске
tasks = { #таски задаем в формате id таска: [длительность в часах, стоимость]
    0: [3, 10],
    1: [7, 4],
    2: [5, 2],
    3: [12, 41],
    4: [3, 3],
    5: [4, 8]
}
#дальше делем поиск в ширину через очередь, в очередь кладем элементы в формате:
# [id таска, множество уже взятых тасков,  стоимость уже взятых тасков, часы взятых тасков]
queue = deque(list(map(lambda t: [t, set(), 0, 0], list(tasks.keys()).copy())))
maxim = {}
max_quantity = 0
max_tasks = []

#пока очередь не пуста, достаем из нее элементы
#если для текущего количества часов мооы уже находили набор тасков с лучщей,
# стоимостью, то это состояние и все из него вытекающие мы рассматривать не будем
while queue:
    task_id, proceeded, q, w = queue.popleft()
    cur_task = tasks[task_id]
    #добавляем к посчитанным стоимостям и часам стоимость и часы текущего таска
    #
    q += cur_task[1]
    w += cur_task[0]
    if maxim.get(w, -1) >= q or w > sprint_capacity: # если часы превышают макс. часы в спринте или для нашего количества часов мы находили стоимость лучше,
        continue                                     # то мы игнорируем это состояние и все из него вытекающие и переходим к следующему
    maxim[w] = max(maxim.get(cur_task[1], -1), q)   #обновляем макс стоимость для количества часов w
    proceeded.add(task_id)
    if q + cur_task[0] > max_quantity:
        max_quantity = q
        max_tasks = proceeded.copy()
    for t in tasks.keys():
        if t not in proceeded:                      #перебираем не взятые таски и добавляем в очередь
            queue.append([t, {*proceeded.copy()}, q, w])

print(max_quantity, max_tasks)
