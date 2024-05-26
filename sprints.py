from collections import deque

def local_search():
    sprint_capacity = 20  # количество часов в таске
    tasks = {  # таски задаем в формате id таска: [длительность в часах, стоимость]
        0: [3, 10],
        1: [7, 4],
        2: [5, 2],
        3: [12, 41],
        4: [3, 3],
        5: [4, 8]
    }
    # дальше делем поиск в ширину через очередь, в очередь кладем элементы в формате:
    # [id таска, множество уже взятых тасков,  стоимость уже взятых тасков, часы взятых тасков]
    queue = deque(list(map(lambda t: [t, set(), 0, 0], list(tasks.keys()).copy())))
    maxim = {}
    max_quantity = 0
    max_tasks = []

    # пока очередь не пуста, достаем из нее элементы
    # если для текущего количества часов мооы уже находили набор тасков с лучщей,
    # стоимостью, то это состояние и все из него вытекающие мы рассматривать не будем
    while queue:
        task_id, proceeded, q, w = queue.popleft()
        cur_task = tasks[task_id]
        # добавляем к посчитанным стоимостям и часам стоимость и часы текущего таска
        #
        q += cur_task[1]
        w += cur_task[0]
        if maxim.get(w, -1) >= q or w > sprint_capacity:  # если часы превышают макс. часы в спринте или для нашего количества часов мы находили стоимость лучше,
            continue                                     # то мы игнорируем это состояние и все из него вытекающие и переходим к следующему
        maxim[w] = max(maxim.get(cur_task[1], -1), q)    # обновляем макс стоимость для количества часов w
        proceeded.add(task_id)
        if q + cur_task[0] > max_quantity:
            max_quantity = q
            max_tasks = proceeded.copy()
        for t in tasks.keys():
            if t not in proceeded:                      # перебираем не взятые таски и добавляем в очередь
                queue.append([t, {*proceeded.copy()}, q, w])

    print(max_quantity, max_tasks)


local_search()


def f():
    pass


def tabu_search(tasks, max_effort):
    l = 15
    tabu_list = deque()
    best_value = 0
    sprint = []
    best_sprint = []

    def is_tabu(tasks):
        tasks = sorted(tasks)
        for t in tabu_list:
            if len(t) != len(tasks):
                continue
            t = sorted(t)
            res = all(t[i]['effort'] != tasks[i]['effort'] or t[i]['value'] != tasks[i]['value'] for i in range(len(t)))
            if res:
                return True

        return False


    for task in tasks:
        s = sum(t['effort'] for t in sprint)
        new_sprint = []
        if s + task['effort'] <= max_effort and not is_tabu(sprint + task):
            new_sprint = sprint + task
        else:
            #выбрать первые n тасков, выбросив которые дешевле текущего и, выбросив которые мы уместим текущий
            #если таких нет, то идем дальше
            pass
        s = sum(t['value'] for t in sprint) > best_value
        if s > best_value:
            best_value = s
            best_sprint = sprint.copy()
