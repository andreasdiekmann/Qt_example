@echo off

REM Erstellen der Python-Module aus ui-Dateien

REM In das Arbeitsverzeichnis wechseln
cd /d %~dp0

REM Konfiguration des Python-Interpreters
set PYDIR="C:\Program Files\WinPython-64bit-3.4.4.3\python-3.4.4.amd64"

echo Erstellen der Python-Module:

for %%f in (*.ui) do (

	echo  - %%~nf.py
	
	REM ggf. alte Datei löschen
	IF exist ..\%%~nf.py del ..\%%~nf.py

	REM neue Datei schreiben
	%PYDIR%\python %PYDIR%\Lib\site-packages\PyQt4\uic\pyuic.py %%f >> ..\%%~nf.py

)

echo.
echo Fertig

pause