@echo off
pyinstaller --windowed ^
            --noconfirm ^
            --icon="%GITHUB%\coffeegrindsize\build_tools\coffeegrindsize.ico" ^
            --add-data="%GITHUB%\coffeegrindsize\build_tools\coffeegrindsize.ico;." ^
            --name "coffeegrindsize" ^
            --hidden-import cmath ^
            %GITHUB%\coffeegrindsize\coffeegrindsize.py
