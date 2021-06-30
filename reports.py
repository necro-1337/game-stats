import export


def count_games(file_name):
    temp_list = export.export_file(file_name)
    counter = 0
    for i in temp_list:
        counter += 1
    return counter


def decide(file_name, year):
    temp_list = export.export_file(file_name)
    for i in temp_list:
        for j in i[2:3]:
            print(j)
            if int(j) == year:
                return True
    else:
        return False


def get_latest(file_name):
    temp_list = export.export_file(file_name)
    norm_list = []
    counter = 0
    for i in temp_list:
        for j in i:
            norm_list.append(j)
    for i in norm_list[2::5]:
        if int(i) > counter:
            counter = int(i)
    get_index = norm_list.index(str(counter))
    return norm_list[get_index - 2]


def count_by_genre(file_name, genre):
    temp_list = export.export_file(file_name)
    counter = 0
    for i in temp_list:
        for j in i:
            if j == genre:
                counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    temp_list = export.export_file(file_name)
    position = []
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            if temp_list[i][j] == title:
                position.append((i + 1, j + 1))
    try:
        return position[0][0]
    except IndexError:
        raise ValueError


def sort_abc(file_name):
    temp_list = export.export_file(file_name)
    only_titles = []
    for i in temp_list:
        for j in i[::5]:
            only_titles.append(j)
    return sorted(only_titles)


def get_genres(file_name):
    temp_list = export.export_file(file_name)
    genres = []
    for i in temp_list:
        for j in i[3::5]:
            genres.append(j)
    genres = set(genres)
    return sorted(genres)


def when_was_top_sold_fps(file_name):
    temp_list = export.export_file(file_name)
    fps_list = []
    norm_fps_list = []
    for i in temp_list:
        if i[3] == "First-person shooter":
            fps_list.append(i)
    for i in fps_list:
        for j in i:
            norm_fps_list.append(j)
    counter = 0
    for i in norm_fps_list[1::5]:
        if float(i) > counter:
            counter = float(i)
    top_sold_index = norm_fps_list.index(str(counter))
    return norm_fps_list[top_sold_index + 1]