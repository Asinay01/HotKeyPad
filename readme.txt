1. Распаковать и установить драйвер
2. Подключаем кейпад
3. Запускаем прогу только от имени администратора

Пока нажимаете кнопочки кейпада, на клаве лучше ничего не жать
Конфиг загружается при запуске программы и переподключении кейпада
В конфиге обязательно хоткеи заключаются в [скобки], все буквы маленькие
Текстовые хоткеи пишутся без скобок и работают только с английскими буквами
Внимательнее с запятыми и кавычками
Не забываем указывать: это хоткей, или эмуляция набора текста
На некоторых устройствах кнопка left windows может работать некорректно, заменяем на right windows, даже если он у вас слева

Ниже приведен пример рабочего конфига config.json, под ним - шпаргалка с текстовым значением поддерживаемых кнопок

{
    "1": [["left windows", "d"], "hotkey"],
    "2": [["ctrl", "shift", "esc"], "hotkey"],
    "3": [["enter"], "hotkey"],
    "4": ["lox", "text"],
    "5": ["a44at", "text"],
    "6": [["left windows", "left shift", "right"], "hotkey"],
    "7": ["only eng text is supported", "text"],
    "8": [["ctrl", "f1"], "hotkey"],
    "9": [["ctrl", "f2"], "hotkey"],
    "10": [["ctrl", "f3"], "hotkey"],
    "11": [["next track"], "hotkey"],
    "12": [["previous track"], "hotkey"],
    "13": [["play/pause media"], "hotkey"],
    "14": [["volume down"], "hotkey"],
    "15": [["volume up"], "hotkey"],
    "16": [["volume mute"], "hotkey"]
}

Supported keys:

control-break processing
backspace
tab
clear
enter
shift    #лучше используйте левый или правый
left shift
right shift
ctrl     #и тут тоже
left ctrl
right ctrl
alt
pause
caps lock
esc
spacebar
page up
page down
end
home
left
up
right
down
select
print
execute
print screen
insert
delete
help
0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
left windows
right windows
applications
sleep
*
+
separator
-
decimal
/
f1
f2
f3
f4
f5
f6
f7
f8
f9
f10
f11
f12
num lock
scroll lock
left menu
right menu
browser back
browser forward
browser refresh
browser stop
browser search key
browser favorites
browser start and home
volume mute
volume down
volume up
next track
previous track
stop media
play/pause media
start mail
select media
,
.
play
zoom
clear
