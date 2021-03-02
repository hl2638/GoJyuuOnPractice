# class State:
#     WELCOME = -1
#     MAIN = 0
#     SHOW_TABLE = 1
#     SHOW_KANA = 2
#     QUIZ = 3
#     HELP = 4
#
#
# class MainMenuChoice:
#     HELP = 0
#     DISPLAY_TABLE = 1
#     SEARCH_KANA = 2
#     QUIZ = 3
#     CHAT_BOT = 4

SHOW_HIRA = 0
SHOW_KATA = 1

welcomeText = """
欢迎来到小猫咪学五十音小助手\n
这是一个帮助小猫咪学五十音的工具\n
喵~（本程序中的喵均已经过语法检查）
"""

# mainMenuText = """
# ==========
# 要做什么呢喵~
# 输入对应的数字就可以哦
# 0 查看帮助
# 1 查看五十音图
# 2 搜索假名
# 3 小测验
# 4 聊天机器猫
# ==========
# """
#
# mainMenuInputErrorText = """
# 不明白你说了什么喵~再试一次吧
# """

kanaTableMap = [
    ['a', 'i', 'u', 'e', 'o'],
    ['ka', 'ki', 'ku', 'ke', 'ko'],
    ['sa', 'shi', 'su', 'se', 'so'],
    ['ta', 'chi', 'tsu', 'te', 'to'],
    ['na', 'ni', 'nu', 'ne', 'no'],
    ['ha', 'hi', 'hu', 'he', 'ho'],
    ['ma', 'mi', 'mu', 'me', 'mo'],
    ['ya', None, 'yu', None, 'yo'],
    ['ra', 'ri', 'ru', 're', 'ro'],
    ['wa', None, None, None, 'wo']
]