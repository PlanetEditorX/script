@echo off
echo ===================================================================================================== >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"
echo %date:~0,10%-%time:~0,8% document-copy is start >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"

xcopy "C:\Users\Dear X\Desktop\学习\" D:\Study\Sync\civil\学习\ /s /v /y /d /exclude:document-copy-exclude.txt >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"

xcopy "C:\Users\Dear X\Desktop\2023年教程\" D:\Study\Sync\civil\2023年教程\ /s /v /y /d /exclude:document-copy-exclude.txt >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"

xcopy "C:\Users\Dear X\Documents\script\" D:\Study\Sync\script\ /s /v /y /d /exclude:document-copy-exclude.txt >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"

:: 压缩大文件夹
for /r "D:\Study\Sync\civil\" %%a in (*.pdf *.docx) do (
	if exist %%a.zip.001 (
		del /f /s /q  %%a.zip.*
	)
	:: 压缩超过20MB的文件
	if %%~za gtr 20971520 (
		C:
		cd "C:\Users\Dear X\scoop\apps\7zip\current\"
		.\7z.exe a -v20m %%a.zip %%a
		del /f /s /q  %%a
	)
) >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"

::����git�ű�
C:
cd "C:\Users\Dear X\Documents\script"
start document-git.vbs

::pause

::xcopy命令
::https://learn.microsoft.com/zh-cn/windows-server/administration/windows-commands/xcopy

::������������ΪANSI��ʽ
echo ===================================================================================================== >> "C:\Users\Dear X\Documents\script\CopyAndGit.log"
