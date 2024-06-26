@echo off
set SrcDir=D:\Download\animal
set DaysAgo=10
forfiles /p %SrcDir% /s /m *.* /d -%DaysAgo% /c "cmd /c rd /s /q @path"
forfiles /p %SrcDir% /s /m *.* /d -%DaysAgo% /c "cmd /c del /f /q /a @path"