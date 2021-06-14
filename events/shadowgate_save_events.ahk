; This script ensures consistency between all five shadowgate alphabet files. Don't forget to setup the '#IfWinActive' below, and don't move this script outside of the events folder!
; With this AutoHotkey script active, make changes only to 'shadowgate_rename_events.txt' in your preferred text editor.
; Press CTRL+S with 'shadowgate_rename_events.txt' already saved, and it will distribute any and all changes you've made to each shadowgate alphabet file.
; Unfortunately, 'shadowgate_pilgrimage_events.txt' is not covered by this script, and it shares many similarities with the alphabet files (mainly the menu events that perform destination browsing).

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.

; Change WINDOWNAME to the displayed window's entire name. For example, if using default windows notepad: shadowgate_rename_events - Notepad
#IfWinActive WINDOWNAME

^s::
Send ^s
ShadowgateArray := Array("a", "b", "c", "d", "e")
For i in ShadowgateArray
{
	Shadowgate := ShadowgateArray[i]
	FileCopy, shadowgate_rename_events.txt, shadowgate_%Shadowgate%_events.txt, 1
	FileRead, SA, shadowgate_%Shadowgate%_events.txt
	SAReplace := StrReplace(SA, "rename", Shadowgate)
	FileDelete, shadowgate_%Shadowgate%_events.txt
	FileAppend, %SAReplace%, shadowgate_%Shadowgate%_events.txt
	Sleep 100
}
return