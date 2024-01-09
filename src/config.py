themes = {
    "theme1": {
        "hover_color": "#2f2f50",
        "background_color": "#22223B",
        "text_color": "#9A8C98",
        "button_color": "#4e4e87",
        "edge_color": "#2e2e50",
        "outer_color": "white",
        "win_0_color": "red",
        "win_1_color": "blue"
    },

    "theme2": {
        "hover_color": "#ffed7a",
        "background_color": "#F2D974",
        "text_color": "#534E52",
        "button_color": "#fff67a",
        "edge_color": "#e3cd72",
        "outer_color": "white",
        "win_0_color": "red",
        "win_1_color": "blue"
    },

    "theme3": {
        "hover_color": "#bf3b3b",
        "background_color": "#f24b4b",
        "text_color": "#f2f0d8",
        "button_color": "#ff5a4f",
        "edge_color": "#f26b6b",
        "outer_color": "white",
        "win_0_color": "red",
        "win_1_color": "blue"
    },
    
    "debug_theme": {
        "hover_color": "gray",
        "background_color": "white",
        "text_color": "black",
        "button_color": "gray",
        "edge_color": "gray",
        "outer_color": "white",
        "win_0_color": "red",
        "win_1_color": "blue"
    }
}

current_theme = "theme1"

FIRST_LETTER = "X"
ZERO_LETTER = "0"
BOARD_HEIGHT = 3
BOARD_LENGTH = 3
WIN_COMBINATIONS = (
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6}
)