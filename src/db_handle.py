import sqlite3

def save_game(info):
    con = sqlite3.connect("saves.sqlite")
    cur = con.cursor()
    cur.execute("""INSERT INTO saves(game_pos, local_zero_pos, local_first_pos, global_first_pos, global_zero_pos, local_end, global_end, current_global_field, zero_turn,
    local_ends,
    any_field, current_outer_label, local_field) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", info)
    con.commit()
    con.close()

def get_data(id):
    con = sqlite3.connect("saves.sqlite")
    cur = con.cursor()
    result  = cur.execute("""select * from saves where id = ?""", (id + 1,)).fetchall()
    con.close()
    return result

def format_data(data, change_to):
    if change_to in ("game_pos", "local_pos"):
        res = data[2:-2].split('], [')
        new_data = []
        for i in res:
            try:
                new_data.append(list(map(int, i.split(', '))))
            except:
                new_data.append(list(map(int, i.split())))
        return new_data

    elif change_to in ("global_pos"):
        try:
            new_data = list(map(int, data[1:-1].split(', ')))
        except:
            new_data = list(map(int, data[1:-1].split()))

        return new_data

    elif change_to in ("local_ends"):
        try:
            new_data = set(map(int, data[1:-1].split(', ')))
        except:
            try:
                new_data = set(map(int, data[1:-1].split()))
            except:
                new_data = set()

        return new_data
